Everything Old Is New Again
===========================

category

:   clojure

tags

:   tools, clojure, technology, programming languages

date

:   2020-04-26

I've been doing some retooling of my blog (while I've been on furlough
from my day job because of COVID-19). I'm now using
[cryogen](https://github.com/cryogen-project/cryogen), a
[Clojure](https://www.clojure.org)-based static site generator, rather
than the [Python](https://www.python.org/)-based
[Pelican](https://blog.getpelican.com) site generator that previously
powered it.

I'll be honest -- the switch was more motivated by my desire to learn
Clojure than by any limitation or dislike of Pelican. And, predictably
(because, after all, it's me we're talking about), I've spent the past
couple of days hacking on the cryogen code to make it work the way I
want to. I can now run the command `lein new-post` in my blog tree to
make a new post (and be prompted for some parameters), for example. Like
I said, my hacking was about 3% motivated by workflow and 97% by the
desire to learn some Clojure.

But along the way, I started thinking about how the pendulum swings in
technology, and how everything old is new again. It's a fascinating
pattern, and I've been in the tech world long enough to see it play out
over and over again. Some examples:

1.  **The Cloud**. When I first started having access to "real
    computers" in college, the holy grail were big mainframes that we
    accessed using PCs or relatively "dumb" terminals. I remember the
    thrill of having accounts on my university's big server systems,
    such as an [IBM 3090](https://en.wikipedia.org/wiki/IBM_3090), a
    [VAX](https://en.wikipedia.org/wiki/VAX_8000) and a big Sun
    Microsystems [SPARCCenter
    2000](https://en.wikipedia.org/wiki/Sun4d#SPARCcenter_2000). Then we
    spent a couple of decades on the whole
    [client/server](https://en.wikipedia.org/wiki/Client–server_model)
    model of putting all the computing power in PCs. And now the
    pendulum is swinging, back toward big servers in "the cloud" --
    really, just a fancy word for "other people's computers" -- accessed
    from our less powerful and less scalable local systems. I'm actually
    writing this post from my iPad, connected to my cloud (Linux) server
    through an
    [ssh](https://en.wikipedia.org/wiki/Secure_Shell)/[mosh](https://mosh.org)
    connection.

2.  **Object-Oriented Programming**. Back in the old days, programming
    languages were "procedural". You wrote routines and strung them
    together to make programs. Languages like
    [COBOL](https://en.wikipedia.org/wiki/COBOL) and
    [FORTRAN](https://en.wikipedia.org/wiki/Fortran) and
    [C](https://en.wikipedia.org/wiki/C_(programming_language))
    dominated. Then we discovered the idea of [object-oriented
    programming](https://en.wikipedia.org/wiki/Object-oriented_programming)

    \- modeling the real world in our programs, creating virtual
    "objects" that had properties and actions associated with them. This
    was good in many ways, and we soon had new languages such as
    [Ruby](https://ruby-lang.org/) and [Python](https://python.org), and
    variants of old ones, like
    [C++](https://en.wikipedia.org/wiki/C%2B%2B) and
    [Objective-C](https://en.wikipedia.org/wiki/Objective-C) and even
    [Object
    Cobol](https://supportline.microfocus.com/documentation/books/sx51/oppubb.htm).
    And while it was true that these new ways of thinking about
    programming enabled us to do all sorts of new and wonderful things,
    they were also not without their downsides. Now [functional
    programming](https://en.wikipedia.org/wiki/Functional_programming)
    is a hot topic again, with new languages like
    [Erlang](https://en.wikipedia.org/wiki/Erlang_(programming_language))
    and [OCaml](https://en.wikipedia.org/wiki/OCaml) joining old
    standards again. ([Clojure](https://en.wikipedia.org/wiki/Clojure)
    is a dialect of
    [Lisp](https://en.wikipedia.org/wiki/Lisp_(programming_language)),
    which has been around since 1958!)

3.  **Artificial Intelligence**. Broadly, this term has swept up a lot
    of stuff involving making computers "smarter".
    [AI](https://en.wikipedia.org/wiki/Artificial_intelligence) has
    undergone waves of popularity followed by disappointment since the
    discipline was first started in the 1950s. [Neural
    networks](https://en.wikipedia.org/wiki/Artificial_neural_network),
    which attempted to simulate the behavior of the brain's individual
    neurons, were at the heart of one such wave. Rule-based [expert
    systems](https://en.wikipedia.org/wiki/Expert_system) were another.
    Now we have [machine
    learning](https://en.wikipedia.org/wiki/Machine_learning) as the
    wave of the future, with all sorts of tech lumped in under that
    umbrella.

In thinking about these cycles, and in making this (non-exhaustive)
list, I think there are a few common threads that drive the pendulum
swings:

-   Technologist and computer people think about problems in need of
    solutions. Procedural programming had challenges, so we came up with
    new paradigms and ways of architecting technology. But of course,
    those will have challenges too, because they were designed by
    humans. So we try to solve this problems, and along the way create
    yet more new problems (or sometimes re-create older ones).
-   Technology people tend to be susceptible to the "[ooh,
    shiny!](https://www.urbandictionary.com/define.php?term=ooh%20shiny)"
    phenomenon. We discover the cool, trendy, hip new thing and everyone
    jumps on the bandwagon. And then, a few years later, the next new
    shiny thing comes along, and the older stuff gets abandoned. I think
    [Classic ASP](https://en.wikipedia.org/wiki/Active_Server_Pages) and
    [PHP](https://en.wikipedia.org/wiki/PHP) are good examples here.
-   We tech people sometimes seek to solve "problems" without fully
    understanding why the thing creating the problem works the way it
    does. The proliferation of
    [NoSQL](https://en.wikipedia.org/wiki/NoSQL) databases is a good
    example. There are good reasons why a document-oriented database
    like [MongoDB](https://en.wikipedia.org/wiki/MongoDB) or a key-value
    database such as [Riak](https://en.wikipedia.org/wiki/Riak) can and
    should be used. But if you try to build an e-commerce application
    solely on MongoDB, you'll quickly discover that order processing in
    a database environment with the property of [eventual
    consistency](https://en.wikipedia.org/wiki/Eventual_consistency) can
    get you into trouble if you're not careful.

That's not to say we should stop innovating, of course. We *do* tend to
come up with new solutions to problems, and in a lot of ways that's
brought about a wonderful world of more and more powerful, capable, and
usable technology. Consider the
[Cray-2](https://en.wikipedia.org/wiki/Cray-2) supercomputer of the
mid-1980s. It took up a large room, cost millions of dollars to buy and
operate, and required special liquid coolant to run without melting into
slag. It was also less powerful than my [iPhone
XS](https://en.wikipedia.org/wiki/IPhone_XS), which cost less than
\$1,000 and fits in my pocket. Decades of innovation allowed us to
miniaturize that amount of computing power, and we can do amazing and
positive things because of it.

What we *should* do, then, is simple: Create the new tools, but don't
forget about the old ones either. And when we're building something,
pick the right tool for the job. You *can* drive a nail with the side of
a chainsaw, and if you hit a tree with a hammer enough times you might
be able to make it fall over. But are those really the right tools for
the job? Just because you have a shiny new hammer, that doesn't make
every problem a nail.

The other thing, which I alluded to in a [previous
post](/posts/2020-03-01-of-emacs-and-tools/), is this: Don't make the
mistake of getting religious about your tools. Right now I'm learning
and using Clojure, and I'm finding it works well for the kinds of
programs I like to write and the way I work. Does that mean everyone
should drop
[C\#](https://en.wikipedia.org/wiki/C_Sharp_(programming_language)) and
Python and Ruby and switch to it? For that matter, does that mean *I*
will stop using other languages and tools? Of course not. Right now, I'm
doing a lot of my programming in
[Emacs](https://en.wikipedia.org/wiki/Emacs), especially since it has
[good tools](https://docs.cider.mx/cider/index.html) for Clojure
programming. Does that mean I'm uninstalling
[VSCode](https://code.visualstudio.com) and
[PyCharm](https://www.jetbrains.com/pycharm/)? Nope. It's an *and*, not
an *or*. Pick the tools that make you productive, but don't assume
everyone else should pick the same tools as you. [Horses for
courses](https://en.wiktionary.org/wiki/horses_for_courses) and all
that.

The pendulum swings back and forth on a lot of these issues, but one
thing is certain. Each swing of the pendulum brings new tools, new
capabilities, new solutions, new possibilities. A large part of why I
enjoy the new tech so much is because I appreciate the foundation it's
built on. So really, the pendulum doesn't arc back and forth so much as
it traces an ever-rising spiral. And that's what makes technology so
exciting!
