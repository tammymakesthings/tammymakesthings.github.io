Thoughts on CircuitPython for 2020
==================================

category

:   circuitpython

tags

:   circuitpython

date

:   2020-01-07

Over on the [Adafruit
blog](https://blog.adafruit.com/2020/01/01/what-do-you-want-from-circuitpython-in-2020-circuitpython2020-circuitpython/),
they asked \"what do you want from
[CircuitPython](https://circuitpython.org/) in 2020. For those that
aren't familiar with it, CircuitPython is a project to allow programming
of embedded microcontrollers in Python. It's pretty much wonderful, and
I've been using it for almost all of my hardware hacking of late.

So here in no particular order are my thoughts for
*\#CircuitPython2020*.

Projects you'd like to build
----------------------------

I have two projects currently in flight, which I'd like to kick into
gear and finish in 2020:

-   An as-yet unnamed gizmo to provide breathing support and pulse-ox
    monitoring for people (especially kids) having asthma attacks.
    Finishing this is going to require porting one of the MAXIM
    [MAX3010x](https://www.maximintegrated.com/en/products/interface/sensor-interface/MAX30102.html)
    Arduino drivers. This is something I'm working on.
-   [dbagparker](https://github.com/tammymakesthings/dbagparker), a
    simple project which uses a distance sensor to tell you how far away
    from the wall you are when parking your car. I started designing
    this for Arduino, but I think I'm going to redesign for a
    CircuitPython board instead.

I have a few other ideas for stuff I'd like to work on, but I'd like to
finish at least one of these first.

Things you think could be easier
--------------------------------

Overall, CircuitPython is fantastic, and I definitely find it much
easier and faster to build stuff than I did with Arduino/C. Some of that
is my greater fluency with Python, but the dev/test cycle is just much
more intuitive with CircuitPython. Still and all, there are a couple of
things I think could be made easier:

-   *Dependency management*: I don't necessarily think we should
    recreate the whole `pip` ecosystem, but making sure the right
    libraries are installed on my boards and keeping those libraries
    updated is still a chore. The
    [CircUp](https://github.com/adafruit/circup) tool helps with the
    updating part, but I'd like a way that my CircuitPython programs
    could know what libraries they need and make sure those are
    automatically installed.
-   *Firmware updates*: Downloading the CircuitPython .uf2 images for
    all of the boards in my collection, resetting each one to get it
    into UF2 mode, making sure I copy the right firmware image to it,
    and then resetting again and updating libraries is a laboriously
    manual process. In my ideal world, there would be a workflow where I
    could run a listener script on my computer (maybe in
    [Mu](https://codewith.mu/)) and then plug in a board, hit the double
    reset button, and have the script automatically download and flash
    the newest firmware image, wait for the board to reset, and then
    automatically update all of the libraries. When you have 10 or 20
    CircuitPython devices, this would make firmware updates waaaaaay
    faster.

Library improvements
--------------------

`displayio` is a fantastic way to create UIs on boards with OLED
displays, but it's taken me a long time and a lot of trial and error to
figure out how to use it. I understand the flexibility that its paradigm
of `Displays` and `TileGrids` and `Groups` provides, but I'd love a
simpler layer for very common tasks, such as "fill the screen with a
solid color and write some text on top of it." I'd also love it if there
was a way for the library to know the device resolution and to describe
the UI in a resolution-independent way, so if I switch my project from a
[PiBadge](https://www.adafruit.com/product/4200) to a [Circuit
Playground Express](https://www.adafruit.com/product/3333) with a [TFT
Gizmo](https://www.adafruit.com/product/4367), I didn't have to rewrite
all of my UI code.

In closing
----------

I think CircuitPython is an amazing tool which makes the world of
microcontrollers and hardware hacking so much more accessible for people
who want to move beyond [MakeCode](https://makecode.adafruit.com/). The
ecosystem has grown by leaps and bounds in 2019, and I'm excited to see
what 2020 brings. I'm also excited to increase my level of contribution
in 2020, and if you use CircuitPython and love it you should think about
[contributing](https://circuitpython.org/contributing) too!
