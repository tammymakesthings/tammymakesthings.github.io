A Simple Portable Prototyping Station
=====================================

category

:   tools

tags

:   tooling, prototyping, electronics, hardware

date

:   2020-05-05

On [twitter](https://twitter.com/maker_tammy/status/1240781242745806851)
recently, I posted some photos of a little portable prototyping station
I threw together.

[Henry Moore](https://twitter.com/HenryMoore_1) asked for some details
and a parts list, so I thought I'd throw together a quick blog post
about it.

Design Goals
------------

My goals for designing this little prototyping station were:

1.  I wanted something that could be relatively portable, so I could
    take it into my living room or otherwise away from my worktable.
2.  I wanted something tailored to the kinds of stuff I build.
3.  I wanted lots of prototyping space (I'm currently working through
    the book [The Art of
    Electronics](https://www.amazon.com/dp/B01BYJO2JU/) and doing some
    of the experiments.
4.  As much as possible, I wanted something I could build with parts I
    already had on hand. This forced some of my component choices in
    ways you might not experience if you're buying new stuff.

With that in mind, here's what I came up with:

![ProtoStation - Hardware
overview](https://tammymakesthings.com/images/protostation/protostation_overview.jpg)

Pretty handy, huh? Let's talk a bit about what's onboard.

The Hardware
------------

The base of the protoboard was something I found on Amazon (linked in
the parts list below). I could have easily designed something custom fit
and 3-D printed it, but I was going for speed here and my Fusion 360 and
OpenSCAD skills would have made that take longer than I'd have liked.

### Microcontroller

![ProtoStation -
Microcontroller](https://tammymakesthings.com/images/protostation/protostation_metrom4.jpg)

In the upper left area is a microcontroller, since I do lots of stuff
with microcontrollers. (Really, who doesn't, anymore?) I threw an
[Adafruit Metro M4
Express](https://learn.adafruit.com/adafruit-metro-m4-express-featuring-atsamd51)
into this spot because I had it handy and it's powerful enough to handle
most all of the things I want to prototype. Like everything else on the
prototyping station, it's held on with foam double-sided tape, so I can
easily swap it out for something else if I want to later.

### Power Distribution

![ProtoStation - Power distribution
block](https://tammymakesthings.com/images/protostation/protostation_pwrdist.jpg)

The next area of the board is my power distribution block. I had a tiny
little breadboard lying around, so I ran a bunch of stuff over to it:

-   The 3.3VDC and 5VDC outputs from the Metro M4 Express;
-   The 3.3VDC output from the I2C/SPI interface (see below);
-   4.5V DC from an Adafruit AA Battery holder (connected to the board
    with a JST breadboard adapter);
-   Enough extra space to jumper in the output from my benchtop
    adjustable power supply.

This way I can jumper whatever power I want into the breadboard's power
buses, depending on what I'm working on and what's available. (If I'm
not connected to USB, the Metro M4 and the I2C interface aren't
providing power, obviously.)

### I2C/SPI Interface

![ProtoStation - I2C/SPI
Interface](https://tammymakesthings.com/images/protostation/protostation_ft232.jpg)

Next up is my I2C/SPI interface, so I can test sensor-based stuff and
whatnot easily. I used an [Adafruit
FT232H](https://www.adafruit.com/product/2264) here because it was what
I had handy, but an [Excamera I2Cmini](https://i2cdriver.com/mini.html)
or any other similar device would work here too. Again, I jumpered the
power outputs of this over to the power distribution block so I could
use them if wanted.

### Prototyping Area

![ProtoStation - Prototyping
area](https://tammymakesthings.com/images/protostation/protostation_proto.jpg)

And lastly, the breadboards for prototyping space. Again, I used what I
had handy. To simplify the connections between the prototyping area and
the power distribution block, I've jumpered the positive and negative
rails at the top of the breadboards together. I've left the bottom rails
un-jumpered and unconnected to the top ones, because sometimes I run the
I2C signals (`SDA` and `SCL`) or SPI signals (`MISO` and `MOSI`) along
here.

Ideas For the Future
--------------------

It might be nice to custom design and print a base that fits and has
better mounting for all the components. Everything here is held on with
double-sided tape, but designing something with the right screw holes
would be nicer aesthetically.

Something else I'd probably do if I respin this is to create some more
space for more breadboards. Some is good, more is better, right?

Finally, I'd like to include a couple of other things -- a function
generator, a small 3.3V and 5V regulated power supply, a LiPo battery
and charger. None of these is essential, but they'd be useful add-ons.
But then, at that point I'm basically redesigning the old [Heathkit
ET-3100](https://www.vintage-computer.com/heathkit3100.shtml) and it
might just be easier to buy one of those and add microcontrollers.

So there you have it - my quick-and-dirty portable prototyping station.
If you build your own version, let me know! I'd love to see what you
come up with.

Parts List
----------

-   **Base board**. I used [this
    one](https://www.amazon.com/gp/product/B07C7FQDPG/) from Amazon, but
    you have lots of options here.
-   **Solderless breadboards**. I used two of something like
    [these](https://www.amazon.com/dp/B07LFD4LT6/) and two of something
    like [these](https://www.amazon.com/dp/B07KGQ7H8B/).
-   **Microcontroller**. Mine was the
    [Adafruit](https://www.adafruit.com/) [Metro M4
    Express](https://www.adafruit.com/product/4000). (I've linked to the
    current board, but mine is older and doesn't include WiFi.)
-   **I2C/SPI Interface**. I used the Adafruit [FT232H
    Breakout](https://www.adafruit.com/product/2264).
-   **Battery Holder**. I used [this
    one](https://www.adafruit.com/product/3287), which also required a
    [JST breadboard adapter](https://www.adafruit.com/product/1862).
-   **Double-sided tape**. I used [Scotch foam mounting
    tape](https://www.amazon.com/gp/product/B003W0R4PE/) and stacked up
    multiple layers of tape as needed to make everything fit.
