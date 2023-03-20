Why Clojure?
============

category

:   programming

tags

:   programming, clojure, programming languages

date

:   2020-05-14

This is going to be the first post in a series about
[Clojure](https://clojure.org/) and how to get started with it. In this
post, I'll talk about what Clojure is, why it's interesting to learn,
and how to get a Clojure environment set up on your system. In
subsequent posts, I'll dive into the basics of Clojure and give you some
pointers for how to get started with it.

What is Clojure?
----------------

Clojure is a [functional
programming](https://en.wikipedia.org/wiki/Functional_programming)
language suitable for general purpose programming tasks. It's a dialect
of [Lisp](https://en.wikipedia.org/wiki/Lisp_(programming_language))
which runs on top of the [Java virtual
machine](https://en.wikipedia.org/wiki/Java_virtual_machine). Clojure
was developed by Rich Hickey in 2007, and is actively maintained by a
community overseen by Rich.

How and why did you learn about Clojure?
----------------------------------------

I admit I'm a bit late to the Clojure party, relatively speaking. I
first heard of Clojure while reading [The Unicorn
Project](https://itrevolution.com/the-unicorn-project/), a novel of
[DevOps](https://en.wikipedia.org/wiki/DevOps) and software development
by Gene Kim. Maxine, the protagonist of the novel, is a fan of Clojure,
and reading the novel convinced me to give it a look.

Some of the things about Clojure that I found interesting included:

1.  **Clojure is a language in the Lisp family.** Although I'm not
    religious about my development tools, as I've [mentioned
    before](https://tammymakesthings.com/posts/2020-03-01-of-emacs-and-tools/),
    I *am* a fan of Emacs, which I've used on and off since college. I
    think you can't really use Emacs for very long without learning at
    least a bit of [Emacs
    Lisp](https://www.gnu.org/software/emacs/manual/html_node/eintr/),
    so I was already familiar with Lisp languages. This does shorten the
    learning curve a bit.
2.  **Clojure provides a REPL, and a lot of development happens there.**
    I've long been a fan of languages with good
    [REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop)s,
    and the way they enable a sort of interactive, exploratory style of
    code development. And the REPL is pretty central to both the "how"
    and "why" of Clojure development.
3.  **Clojure is cross-platform, and sits on top of the JVM**. This
    gives it a lot of power and flexibility. There's also a large and
    active community and ecosystem of Clojure add-ons and stuff. And the
    cross-platform, JVM-based environemnt makes getting an environment
    set up easy.
4.  **Clojure is a functional programming language.** There's a lot of
    reasons why functional programming is a desirable thing, but as
    Maxine notes in [The Unicorn
    Project](https://itrevolution.com/the-unicorn-project/), one of the
    most important is that data in Clojure is immutable. This prevents a
    lot of the bugs that come up in non-functional languages. My general
    agnosticism about tools means I don't necessarily think Clojure is
    the tool for every problem, but I *do* think it's a viable solution
    for a lot of stuff and therefore worth having in my toolbelt.
5.  **Clojure has a browser-based scripting version**. It's called
    [ClojureScript](https://clojurescript.org/), and ClojureScript can
    be compiled to standard Javascript. This gives you a unified and
    coherent platform for client, server, and desktop development.
6.  **Clojure is a new, fun thing that I didn't already know.** Hey, I'm
    a nerd and I have
    [ADHD](https://en.wikipedia.org/wiki/Attention_deficit_hyperactivity_disorder),
    so I'm susceptible to the "ooh, shiny" syndrome. What can I say?

Getting Clojure set up on your system
-------------------------------------

Luckily, getting a Clojure environment set up on your system is
relatively easy, thanks to development environments like
[Leiningen](https://leiningen.org/). Here's what you need to do to get
Clojure running on your system:

1.  **Install prerequisites**. You'll need to make sure you have a Java
    virtual machine on your system. JDK 8 or JDK 11 are the supported
    versions, and changes in later versions will produce random weird
    errors. I found that I needed to use one of [the official Oracle
    builds](https://www.oracle.com/java/technologies/javase-jdk8-downloads.html)
    because the [OpenJDK](https://openjdk.java.net/install/) version is
    missing some SSL certificates, and that breaks the downloading of
    Clojure extensions and libraries. Installing
    [git](https://git-scm.org/) and a good terminal program is also a
    good idea. (I'm using [tilix](https://gnunn1.github.io/tilix-web/)
    on Linux. I suggest [Windows
    Terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701)
    on Windows, and [iTerm2](https://www.iterm2.com/) on OS X.)

2.  **Download and install Leiningen**. This is super easy and mostly
    automated. The [leiningen website](https://leiningen.org/#install)
    has instructions. You'll need to make sure the JDK tools are
    installed and in your path for this to work.

3.  **Check that your setup is working.** Run the command
    `lein version`. You should see a message like this:

        Leiningen 2.9.3 on Java 1.8.0_251 Java HotSpot(TM) 64-Bit Server VM

4.  **Set up your editor/IDE.** I'll talk about this in the next
    section, but using an editor with good Clojure integration is super
    imoportant for a good development experience.

Clojure editor/IDE integration
------------------------------

As I mentioned above, one of the features of Clojure that makes
developing with it so fun -- and powerful -- is that a lot of
development is done in an exploratory fashion with the REPL. We'll see
this in subsequent installments of my tutorial. But what this means is
that you want to configure your editor with good Clojure integration,
including an integrated REPL. Here are some choices you can use:

-   **Emacs** users should install [CIDER](https://cider.mx). There's
    some customization you might want to do, but the CIDER [installation
    guide](https://docs.cider.mx/cider/basics/installation.html) will
    get you going.
-   **Visual Studio Code** users can pick from a few extensions, but the
    most well--integrated and easy-to-install choice I've found is
    [Calva](https://calva.io).
-   **vi/vim** users might want to start
    [here](https://github.com/ctford/vim-fireplace-easy). You might also
    find [tmux](https://github.com/tmux/tmux/wiki) and
    [tmuxinator](https://github.com/tmuxinator/tmuxinator) to be helpful
    tools.
-   **Sublime Text** users would do well to take a look at Greg
    Williams's
    [guide](https://spin.atomicobject.com/2016/04/08/sublime-text-clojure/).
-   **Atom** users might benefit from Jacek Schae's
    [guide](https://medium.com/@jacekschae/slick-clojure-editor-setup-with-atom-a3c1b528b722).
-   If you want a **purpose--built IDE** for Clojure development, take a
    look at [JetBrains Cursive](https://cursive-ide.com/) and
    [Nightcode](https://sekao.net/nightcode/). I haven't used either of
    these, but they seem to be highly regarded.
-   If you use another editor or development tool, you're on your own,
    I'm afraid. But you should look for something that lets you run
    Leiningen commands, has a built--in terminal or shell, and that has
    integration with the Clojure REPL.

Some add-ons for Leiningen
--------------------------

There are a couple of add-ons for Leiningen that I've found are super
helpful from a development perspective:

-   [lein-cprint](https://github.com/greglook/lein-cprint) colorizes the
    output in the Leiningen REPL and makes it easier to read.
-   [debux](https://github.com/philoskim/debux) gives you some easy
    trace-based debugging helpers.
-   [lein-autoreload](https://clojars.org/lein-autoreload) automatically
    reloads the REPL when you make changes to your source files.
-   [rebel-readline](https://github.com/bhauman/rebel-readline) adds
    command history and editing to the Clojure REPL.

You can install these by creating a new file in
`$HOME/.lein/profiles.clj` and adding the following to it:

``` {.clojure}
{
 :user
  {
    :plugins [
      [cider/cider-nrepl "0.24.0"]
      [lein-cprint "1.3.3"]
      [philoskim/debux "0.6.5"]
      [lein-autoreload "0.1.1"]
      [com.jakemccrary/lein-test-refresh "0.24.1"]
    ]

    :dependencies [
      [com.bhauman/rebel-readline "0.1.4"]
    ]

    :aliases {
      "rebl" ["trampoline" "run" "-m" "rebel-readline.main"]
  }
}
```

Once you've created this file, run the command `lein deps` to install
all the bits and pieces.

That's it! You're up and running. If you want to play a bit before my
next tutorial, you can spin up a REPL with `lein repl` and try some of
the examples from the [Programming at the
REPL](https://clojure.org/guides/repl/introduction) guide.
