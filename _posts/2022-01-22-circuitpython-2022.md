---
title: "Tammy's CircuitPython 2022 Thoughts"
tags: [circuitpython, circuitpython community, state of circuitpython]
categories: [CircuitPython]
date: 2022-01-22
---

Over on the [Adafruit Blog][blog], there's a call for thoughts about the
state of [CircuitPython][circuitpython], a recap of 2021, and our
thoughts about 2022. Although my 2021 got sort of blown out of the water
by the pandemic and my Major Health Crisis(tm), I'm renewing my focus

for 2022. So although I'm not recapping the dumpster fire that was 2021
for me, I'll share a few thoughts about the current state of play, what
I'd like to see in 2022, and a few of the places I'm putting my focus.

## CircuitPython and Microcontrollers: Holy Cow

To say that it's an amazing and wondrous time to be a maker is, to put
it mildly, a bit of an understatement. The variety of hardware that's
available, and what you can get compared to the cost, are staggering.

Consider this: the [Circuit Playground Bluefruit][cpybluefruit] has about 30
times the processing power of my first home computer, includes a raft of
sensors and connectivity, and costs $25 (about 1/65th of the price of
that first computer). There are both cheaper and more capable micros out
there than the Bluefruit, of course. In fact, the array of
microcontrollers and sensors and other building blocks available today
is staggering; sometimes it's hard to know which one to use!

I really think that CircuitPython has been, and continues to be, a
game-changer for the hardware maker community. [Python][python] is
accessible, well-documented and overall well supported, and I think writing
code in Python and copying a script file to your device feels like a lower
barrier to entry than the [Arduino][arduino] or [FreeRTOS][freertos]
workflows.

That flexibility and range of options is not without its attendant
challenges, though. I find it's sometimes hard to pick a board for my
projects. Should I use a Circuit Playground? An ItsyBitsy? Which one?
The [SAMD][itsysamd]? The [nRF52840][itsynrf]? Or maybe I should try
the new hotness and use an [RP2040][itsyrp2040].I guess having
too many good choices to pick from is a good problem to have...

## Things I'd Like to Work On In 2022

Here in no particular order are some of the things I'd like to work on
in 2022:

- **CircuitPython Dependency Management Tools**: [CircUp][circup]
  helps a lot with keeping the libraries on my CircuitPython boards updated, but it's
  less of a help for me in getting the right libraries installed in the first place.
  In a perfect world, my CircuitPython scripts could include metadata ("I'll be
  running on a Circuit Playground Bluefruit and I need the following libraries"),
  and there'd be an automated way to install those things and their dependencies.
  Something like [pyproject.toml][pyproject] but for CircuitPython. I started a hacky Python script to do some of this, and I'd like to see if I can refactor it into something that could be added to CircUp.

- **Twitch Maker Streaming!**: I love the fact that [Twitch][twitch]
  has grown so far beyond just video games. I follow a number of musicians
  on Twitch, as well as folks cooking, coding, doing magic...the list goes on.
  I'm planning to start streaming maker content on Twitch (hopefully by the end of
  February) with a focus on doing stuff with CircuitPython.
  [My Twitch stream][mytwitch] is aiming to be live
  by the end of February, so follow now if you're interested.

- **CircuitPython Hardware for Music**: I'm really interested in exploring sound
  synthesis, MIDI, and the other musical capabilities of CircuitPython and
  microcontrollers. I've seen some cool projects out there already, but
  I'd like to explore what's possible.

- **CircuitPython for Magic**: One of my friends,
  [infoXczar][infoxczar], performs magic on Twitch. I've been
  brainstorming with him, and I think there are some cool opportunities at the
  intersection of magic, microcontroller technology, and devices that can
  communicate with the Internet. I'd like to explore that.

- **Getting Better With `displayio_`**: There's a lot of documentation out there
  now, but I still feel like there's room for some tutorials which draw all of them together. I don't know if it's documenting my own projects from thought process through execution, or if it's a more focused beginner's "here's how to make sense of all these docs and get started" guide, but I'd like to figure that out.

- **Contributing More to the Community**: I'd like to make some contributions
  to the CircuitPython libraries this year. I'd also like to see if there are opportunities to contribute to the core of CircuitPython itself, since
  I've improved my C/C++ skills since the last time I looked at that. But
  whatever the details, part of the renewed focus on what matters to me is
  going to be finding ways to get a lot more active in the community.

- **Design a CircuitPython Board**: This one is a bit of a stretch goal, but
  I'm working on filling in gaps in my basic electronics knowledge (and updating what I do know for the new world we live in). I'd like to get better at PCB design
  and working with SMT parts, and one way I'd like to do that is to
  design a CircuitPython-compatible board and make at least one. It
  doesn't have to be better than boards on the market, and it
  doesn't have to be practical to manufacture in quantity, but I
  think designing and building a one-off board would be an interesting
  challenge and a good excuse to really learn [KiCAD][kicad].

So, there we have it! It's an exciting time to be a part of the
CircuitPython maker community, and I'm looking forward to getting more
involved in 2022.

[arduino]: https://arduino.cc/
[blog]: https://blog.adafruit.com/2022/01/01/circuitpython-in-2022-circuitpython2022-circuitpython/
[circuitpython]: https://circuitpython.org/
[circup]: https://github.com/adafruit/circup
[cpybluefruit]: https://www.adafruit.com/product/4333
[freertos]: https://freertos.org/
[infoxczar]: https://twitch.tv/infoxczar
[itsynrf]: https://www.adafruit.com/product/4481
[itsyrp2040]: https://www.adafruit.com/product/4888
[itsysamd]: https://www.adafruit.com/product/3800
[kicad]: https:///www.kicad.org/
[mytwitch]: https://twitch.tv/tammymakesthings
[pyproject]: https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/
[python]: https://python.org/
[twitch]: https://twitch.tv/
