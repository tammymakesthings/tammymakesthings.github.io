#####################################################################################
# UI Test for PyGameDisplay
#####################################################################################
# I had to make a couple of changes to the Blinka libraries to make this work on
# Linux:
#
# 1. Comment out the "raise NotImplementedError" on line 276 of
#    site-packages/board.py
# 2. Comment out the "raise NotImplementedError" on line 105 of
#    site-packages/microcontroller/pin.py
####################################################################################

try:
    from typing import List
except ImportError:
    pass

import board
import displayio
import pygame
import terminalio
from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.roundrect import RoundRect
from adafruit_display_text import label
from blinka_displayio_pygamedisplay import PyGameDisplay


def build_ui(display: displayio.Display) -> list:
    splash = displayio.Group()
    display.show(splash)

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

    note_text_label = label.Label(terminalio.FONT, text="ON C#3", color=0xFFFFFF)
    note_text_label.x = 65
    note_text_label.y = 28
    note_group.append(note_text_label)

    encoder_group = displayio.Group()
    encoder_group.append(RoundRect(0, 37, 55, 12, 5, fill=0xFFFFFF))

    encoder_caption_label = label.Label(
        terminalio.FONT, text="Encoder:", color=0x000000
    )
    encoder_caption_label.anchor_point = (1.0, 0.5)
    encoder_caption_label.anchored_position = (55, 41)
    encoder_group.append(encoder_caption_label)
    encoder_text_label = label.Label(terminalio.FONT, text="-10", color=0xFFFFFF)
    encoder_text_label.x = 65
    encoder_text_label.y = 41
    encoder_group.append(encoder_text_label)

    encoder_switch_group = displayio.Group()
    encoder_group.append(RoundRect(0, 51, 55, 12, 5, fill=0xFFFFFF))

    encoder_switch_caption_label = label.Label(
        terminalio.FONT, text="EncSw:", color=0x000000
    )
    encoder_switch_caption_label.anchor_point = (1.0, 0.5)
    encoder_switch_caption_label.anchored_position = (56, 56)
    encoder_switch_group.append(encoder_switch_caption_label)

    encoder_switch_text_label = label.Label(terminalio.FONT, text="Off", color=0xFFFFFF)
    encoder_switch_text_label.x = 65
    encoder_switch_text_label.y = 56
    encoder_switch_group.append(encoder_switch_text_label)

    splash.append(title_group)
    splash.append(note_group)
    splash.append(encoder_group)
    splash.append(encoder_switch_group)

    return [splash, note_text_label, encoder_text_label, encoder_switch_text_label]


if __name__ == "__main__":
    display = PyGameDisplay(width=128, height=64, color_depth=2, grayscale=True)
    splash, note_label, encoder_label, encoder_switch_label = build_ui(display)

    try:
        while True:
            pass
    except pygame.error:
        raise SystemExit()
