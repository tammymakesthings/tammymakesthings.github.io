# SPDX-FileCopyrightText: Copyright (c) 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense

##########################################################################################
# TO-DO LIST:
# - MIDI stuff
#   - [X] Send a MIDI on event on a key press
#   - [X] Send a MIDI off event on a key release
#   - [X] Light up buttons while they're being pressed
#   - [X] Screen to display note and the encoder
#   - [X] Send a MIDI Pitch Bend  message with knob
# Other Stuff
#   - [X] Read the sensors
#   - [X] Temperature value to pitch-bend
#   - [X] IMU sensor to MIDI messages
#   - [X] Redo UI with DisplayIO
#   - [X] Redo UI and sensor code with asyncio
#   - [ ] Replace sensors with a joystick or potentiometers
#   - [ ] Generate corresponding audio tones from the device speaker as well as the
#         MIDI notes.
#   - [ ] Refactoring
#       - [ ] Update docstring comments
#########################################################################################

try:
    from typing import Optional, Union
except ImportError:
    pass


import asyncio
import math

# Setup Code
import time

import adafruit_bmp280
import adafruit_icm20x
import board
import displayio
import terminalio
from adafruit_debouncer import Debouncer
from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.roundrect import RoundRect
from adafruit_display_text import label
from adafruit_macropad import MacroPad
from busio import I2C
from micropython import const
from rainbowio import colorwheel

MIDI_NOTES_OCTAVE_A: List[int, ...] = [60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79]
MIDI_NOTES_OCTAVE_B: List[int, ...] = [48, 50, 52, 53, 55, 57, 59, 60, 62, 64, 65, 56]

MIDI_NOTE_VELOCITY: int = 120

KEY_NONE: int = const(0)
KEY_PRESSED: int = const(1)
KEY_RELEASED: int = const(2)


##############################################################################
# Shared state object for our coroutines
##############################################################################
class MacroPadMidiState:
    def __init__(self, macropad: MacroPad, i2c_bus: busio.I2C) -> None:
        self.macropad: MacroPad = macropad
        self.i2c_bus: busio.I2C = i2c_bus
        # self.imu_sensor = adafruit_icm20x.ICM20649(i2c_bus)
        # self.temp_sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c_bus)
        self.splash: Optional[displayio.Group] = None
        self.note_text_label: Optional[label.Label] = None
        self.encoder_text_label: Optional[label.Label] = None
        self.encoder_switch_text_label: Optional[label.Label] = None

        self.key_event_description: str = "---"
        self.note_list: List[int] = MIDI_NOTES_OCTAVE_A
        self.note_octave: str = "A"
        self.last_octave: str = "A"

        self.encoder_val: int = 0
        self.encoder_sw: bool = False
        self.pitch_bend: Union[int, float] = 0
        self.last_note_time: float = 0
        self.last_encoder_position: int = 0
        self.last_encoder_switch_time: float = 0

        self.accel_x: float = 0.0
        self.accel_y: float = 0.0
        self.accel_z: float = 0.0
        self.gyro_x: float = 0.0
        self.gyro_y: float = 0.0
        self.gyro_z: float = 0.0

        self.last_accel_x: float = 0.0
        self.last_accel_y: float = 0.0
        self.last_accel_z: float = 0.0
        self.last_gyro_x: float = 0.0
        self.last_gyro_y: float = 0.0
        self.last_gyro_z: float = 0.0

        self.temp: float = 0.0
        self.pressure: float = 0.0
        self.altitude: float = 0.0

        self.note_velocity: int = 0


##############################################################################
# Helper Routines
##############################################################################


def build_ui(display: displayio.Display, state_object: MacroPadMidiState) -> None:

    """
    Build the MacroPad MIDI User Interface

    Args:
        display (displayio.Display): The display object.
        state_object (MacroPadMidiState): The shared state object

    Returns:
        Nothing. Sets the UI objects in the shared state/
    """

    state_object.splash = displayio.Group()
    display.show(state_object.splash)

    title_group = displayio.Group()
    title_group_bg = RoundRect(0, 0, 128, 15, 5, fill=0xFFFFFF)
    title_group.append(title_group_bg)
    title_label = label.Label(
        terminalio.FONT, text="=| MacroPad MIDI |=", color=0x000000
    )
    title_label.x = 7
    title_label.y = 6
    title_group.append(title_label)

    note_group = displayio.Group()
    note_group.append(RoundRect(0, 23, 55, 12, 5, fill=0xFFFFFF))
    note_caption_label = label.Label(terminalio.FONT, text="Note:", color=0x000000)
    note_caption_label.anchor_point = (1.0, 0.5)
    note_caption_label.anchored_position = (55, 28)
    note_group.append(note_caption_label)

    shared_state.note_text_label = label.Label(
        terminalio.FONT, text="ON C#3", color=0xFFFFFF
    )
    shared_state.note_text_label.x = 65
    shared_state.note_text_label.y = 28
    note_group.append(shared_state.note_text_label)

    encoder_group = displayio.Group()
    encoder_group.append(RoundRect(0, 37, 55, 12, 5, fill=0xFFFFFF))

    encoder_caption_label = label.Label(terminalio.FONT, text="PBend:", color=0x000000)
    encoder_caption_label.anchor_point = (1.0, 0.5)
    encoder_caption_label.anchored_position = (55, 41)
    encoder_group.append(encoder_caption_label)
    shared_state.encoder_text_label = label.Label(
        terminalio.FONT, text="-10", color=0xFFFFFF
    )
    shared_state.encoder_text_label.x = 65
    shared_state.encoder_text_label.y = 41
    encoder_group.append(shared_state.encoder_text_label)

    encoder_switch_group = displayio.Group()
    encoder_group.append(RoundRect(0, 51, 55, 12, 5, fill=0xFFFFFF))

    encoder_switch_caption_label = label.Label(
        terminalio.FONT, text="Octave", color=0x000000
    )
    encoder_switch_caption_label.anchor_point = (1.0, 0.5)
    encoder_switch_caption_label.anchored_position = (56, 56)
    encoder_switch_group.append(encoder_switch_caption_label)

    shared_state.encoder_switch_text_label = label.Label(
        terminalio.FONT, text=shared_state.note_octave, color=0xFFFFFF
    )
    shared_state.encoder_switch_text_label.x = 65
    shared_state.encoder_switch_text_label.y = 56
    encoder_switch_group.append(shared_state.encoder_switch_text_label)

    shared_state.splash.append(title_group)
    shared_state.splash.append(note_group)
    shared_state.splash.append(encoder_group)
    shared_state.splash.append(encoder_switch_group)


def handle_key_event(
    state_object: MacroPadMidiState,
    event_type: int,
    key_number: int,
    velocity: int = MIDI_NOTE_VELOCITY,
) -> None:

    """
    Handle a keyboard event.

    Args:
        event_type (int): The event type. KEY_PRESSED, KEY_RELEASED, or KEY_NONE.
        key_number (int): The pressed key number (0-12)
        velocity (int): The pressed key velocity. Defaults to MIDI_NOTE_VELOCITY.
    """

    if event_type == KEY_PRESSED:
        shared_state.key_event_description = "+{} [{}]".format(
            shared_state.key, shared_state.note_list[shared_state.key]
        )
        color_index = int(255 / 12) * shared_state.key
        shared_state.macropad.pixels[shared_state.key] = colorwheel(color_index)
        shared_state.macropad.midi.send(
            shared_state.macropad.NoteOn(
                shared_state.note_list[shared_state.key], velocity
            )
        )
        print(
            "Sent MIDI Note ON message for note number {}".format(
                shared_state.note_list[shared_state.key]
            )
        )
    elif event_type == KEY_RELEASED:
        shared_state.macropad.pixels.fill((0, 0, 0))
        shared_state.key_event_description = "-{} [{}]".format(
            shared_state.key, shared_state.note_list[shared_state.key]
        )
        shared_state.macropad.midi.send(
            shared_state.macropad.NoteOff(shared_state.note_list[shared_state.key], 0)
        )
        print(
            "Sent MIDI Note OFF message for note number {}".format(
                shared_state.note_list[shared_state.key]
            )
        )
    else:
        shared_state.key_event_description = "---"


def last_key_event_type(shared_state: MacroPadMidiState) -> int:
    """
    Get the type of the last key event.

    This currently works by parsing the key event description. Should probably
    be refactored.

    Returns:
        int: The key event type (KEY_PRESSED, KEY_RELEASED, KEY_NONE),
    """

    if shared_state.key_event_description:
        if shared_state.key_event_description[0:3].upper() == "OFF":
            return KEY_RELEASED
        elif shared_state.key_event_description[0:2].upper() == "ON":
            return KEY_PRESSED
        else:
            return KEY_NONE


async def read_sensor_inputs(shared_state: MacroPadMidiState) -> None:
    (
        shared_state.last_accel_x,
        shared_state.last_accel_y,
        shared_state.last_accel_z,
    ) = shared_state.imu_sensor.acceleration
    (
        shared_state.last_gyro_x,
        shared_state.last_gyro_y,
        shared_state.last_gyro_z,
    ) = shared_state.imu_sensor.gyro

    shared_state.temp = shared_state.temp_sensor.temperature
    shared_state.pressure = shared_state.temp_sensor.pressure
    shared_state.altitude = shared_state.temp_sensor.altitude

    shared_state.accel_x = (shared_state.accel_x * 0.9) + (
        shared_state.last_accel_x * 0.1
    )
    shared_state.accel_y = (shared_state.accel_y * 0.9) + (
        shared_state.last_accel_y * 0.1
    )
    shared_state.accel_z = (shared_state.accel_z * 0.9) + (
        shared_state.last_accel_z * 0.1
    )

    shared_state.gyro_x = (shared_state.gyro_x * 0.9) + (shared_state.last_gyro_x * 0.1)
    shared_state.gyro_y = (shared_state.gyro_y * 0.9) + (shared_state.last_gyro_y * 0.1)
    shared_state.gyro_z = (shared_state.gyro_z * 0.9) + (shared_state.last_gyro_z * 0.1)

    shared_state.note_velocity = (
        math.fabs(shared_state.accel_x) * 1000 + math.fabs(shared_state.accel_y) * 1000
    )
    shared_state.note_velocity = int(shared_state.note_velocity / 15.0)
    shared_state.note_velocity = 127 - shared_state.note_velocity

    if shared_state.note_velocity < 0:
        shared_state.note_velocity = 0
    if shared_state.note_velocity > 127:
        shared_state.note_velocity = 127


async def read_keyboard(shared_state: MacroPadMidiState) -> None:
    while True:
        while shared_state.macropad.keys.events:
            shared_state.key_event = shared_state.macropad.keys.events.get()
            if shared_state.key_event:
                shared_state.key = shared_state.key_event.key_number
                shared_state.last_note_time = time.monotonic()

                if shared_state.key_event.pressed:
                    handle_key_event(shared_state, KEY_PRESSED, shared_state.key)
                elif shared_state.key_event.released:
                    handle_key_event(shared_state, KEY_RELEASED, shared_state.key)

        if (time.monotonic() > shared_state.last_note_time + 0.75) and (
            last_key_event_type(shared_state) == KEY_RELEASED
        ):
            shared_state.key_event_description = "---"
        await asyncio.sleep(0)


async def read_encoder(shared_state: MacroPadMidiState) -> None:
    while True:
        shared_state.encoder_val = shared_state.macropad.encoder
        if shared_state.encoder_val is not shared_state.last_encoder_position:
            shared_state.encoder_change = (
                shared_state.encoder_val - shared_state.last_encoder_position
            )
            shared_state.last_encoder_position = shared_state.encoder_change
            shared_state.pitch_bend = min(
                max(shared_state.pitch_bend + shared_state.encoder_change, 0), 15
            )
            print("Sending MIDI pitch bend = {}".format(shared_state.pitch_bend * 1024))
            shared_state.macropad.midi.send(
                shared_state.macropad.PitchBend(shared_state.pitch_bend * 1024)
            )

        await asyncio.sleep(0)


async def read_encoder_switch(shared_state: MacroPadMidiState) -> None:
    while True:
        if shared_state.macropad.encoder_switch:
            if time.monotonic() > shared_state.last_encoder_switch_time + 10:
                shared_state.last_octave = shared_state.note_octave
                if shared_state.note_octave == "A":
                    shared_state.note_octave = "B"
                    shared_state.note_list = MIDI_NOTES_OCTAVE_B
                elif shared_state.note_octave == "B":
                    shared_state.note_octave = "A"
                    shared_state.note_list = MIDI_NOTES_OCTAVE_A
                else:
                    shared_state.note_octave = "A"
                    shared_state.note_list = MIDI_NOTES_OCTAVE_A
                print("Note octave is {}".format(shared_state.note_octave))
                await asyncio.sleep(0.1)
        else:
            await asyncio.sleep(0)


async def update_display(shared_state: MacroPadMidiState) -> None:
    while True:
        shared_state.note_text_label.text = shared_state.key_event_description
        shared_state.encoder_text_label.text = str(shared_state.pitch_bend * 1024)
        if shared_state.note_octave == "A":
            shared_state.encoder_switch_text_label.text = "C4"
        elif shared_state.note_octave == "B":
            shared_state.encoder_switch_text_label.text = "C3"
        else:
            shared_state.encoder_switch_text_label.text = "??"

        await asyncio.sleep(0)


async def event_loop(shared_state: MacroPadMidiState) -> None:
    keyboard_task = asyncio.create_task(read_keyboard(shared_state=shared_state))
    encoder_task = asyncio.create_task(read_encoder(shared_state=shared_state))
    encoder_switch_task = asyncio.create_task(
        read_encoder_switch(shared_state=shared_state)
    )
    update_display_task = asyncio.create_task(update_display(shared_state=shared_state))

    while True:
        await asyncio.gather(
            keyboard_task, encoder_task, encoder_switch_task, update_display_task
        )


##############################################################################
# Global Variables
##############################################################################

shared_state = MacroPadMidiState(macropad=MacroPad(), i2c_bus=board.I2C)
build_ui(display=board.DISPLAY, state_object=shared_state)

asyncio.run(event_loop(shared_state))
