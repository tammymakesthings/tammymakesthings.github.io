Literate Emacs Configuration in org-mode
========================================

category

:   tools

tags

:   emacs, tooling, org-mode

date

:   2020-04-28

If you use [emacs](https://www.gnu.org/software/emacs/) at all, you'll
quickly discover that it's much more than just a text editor. Emacs is a
software development platform, too, and as such it's nearly endlessly
customizable. One result of this extensibility is that, if you use
`emacs` very much, your customization file (named `.emacs.d/init.el`)
tends to grow and quickly becomes hard to manage.

Enter [org-mode](https://orgmode.org/). Originally begun as an outlining
tool, `org-mode` has acquired a ton of additional functionality,
including the capability for [literate
programming](https://https://en.wikipedia.org/wiki/Literate_programming).
In a nutshell, literate programming allows you to combine code and
documentation into a single file. With `emacs` and `org-mode`, you can
combine snippets of code and documentation into a single `.org` file,
and then
[tangle](https://orgmode.org/manual/Extracting-Source-Code.html) that
file to produce the code which `emacs` actually runs and documentation
(in HTML, [LaTeX](https://www.latex-project.org), or other formats).

You can see my `emacs` configuration [on
github](https://github.com/tammymakesthings/emacs_d). My emacs
configuration is located in the file
[init.org](https://github.com/tammymakesthings/emacs_d/blob/master/init.org).
You can look at that file if you want details, but what I'd like to show
you here is a step-by-step guide to creating your own `emacs`
configuration with `org-mode`, including automatically tangling your
`init.org` file when it's modified.

Ready? Let's go!

1.  Install Emacs. Instructions for various platforms are
    [here](https://www.gnu.org/software/emacs/manual/html_node/efaq/Installing-Emacs.html).
    As of 04/2020, you should install Emacs 26. A version of org-mode is
    bundled with Emacs, so no installation is needed there.

2.  If you have an existing `.emacs.d` directory, rename it and create
    an empty one. This directory should live in your home directory (on
    Linux and MacOS X systems). On Windows systems, consult [this
    guide](https://www.gnu.org/software/emacs/manual/html_node/efaq-w32/Location-of-init-file.html)
    to work out where your home directory lives.

3.  Inside the `.emacs.d` directory, create a file named `init.el`.
    Paste in the following code to that file:

    ``` {.lisp}
    ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    ;; This file replaces itself with the actual configuration at first run.
    ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

    ;; We can't tangle without org!
    (require 'org)

    (defvar user/init-org-file (concat user-emacs-directory "init.org"))
    (defvar user/init-el-file  (concat user-emacs-directory "init.el"))

    (find-file user/init-org-file)
    (org-babel-tangle)
    (load-file user/init-el-file)
    (byte-compile-file user/init-el-file)
    ```

    This "seed" init file will cause `emacs` to load the `init.org`
    file, "tangle" it to produce a new `init.el` and byte-compile the
    new `init.el` file for faster execution.

4.  Also inside the `.emacs.d` directory, create a new file called
    `init.org`. This file will contain all your emacs customizations and
    documentation. Inside your `init.org` you can put as much
    documentation as you want (following the `org-mode` [markup
    syntax](https://orgmode.org/guide/Markup.html). You can also put
    Emacs Lisp code blocks, which will be extracted into the `init.el`
    file when your `init.org` is tangled. Each code block should begin
    with a line like this:

        #+begin_src emacs-lisp

    And end with a line like this:

        #+end_src

    These markers tell Emacs and `org-mode` how to extract the code.
    I'll talk about what should go into this file in a moment.

5.  Copy `init.el` to `init.el.firstrun`. This step is optional, but
    since tangling the org file overwrites the seed `init.el` I like to
    keep a copy around.

6.  Check your `.emacs.d` into source code control. If you're using
    `git`, you'll want to do something like this after you've created
    your repo and checked in your `init.org` and `init.el` files, since
    the contents of `init.el` are automatically overwritten:

    `git update-index --assume-unchanged init.el`

7.  Once you've created your `init.org` file, launch Emacs. Emacs will
    read your `init.org`, tangle it and create a new `init.el`
    (replacing the seed created in step 3), compile it to `init.elc` and
    then load it.

8.  After this initial compliation, I find it's a good idea to exit and
    restart emacs.

So, what goes in your `init.org` file? I like to start with the
following, in order:

-   **An emacs mode-line and header block for the org file.** This tells
    Emacs what kind of file it is, and includes some `org-mode` options
    useful if you decide to typeset your configuration with LaTeX. The
    first few lines of my `init.org` look like this:

        -*- mode: org; fill-column: 78; -*-
        #+TITLE: Emacs configuration file
        #+AUTHOR: Tammy Cravit
        #+DATE: Time-stamp: <2020-04-05 10:08:30 tammy>
        #+BABEL: :cache yes
        #+LATEX_HEADER: \usepackage{parskip}
        #+LATEX_HEADER: \usepackage{inconsolata}
        #+LATEX_HEADER: \usepackage[utf8]{inputenc}
        #+PROPERTY: header-args :tangle init.el

-   **The emacs mode-line and header block.** This block will be copied
    verbatim into the top of your `init.el`. Its jobs are to make sure
    Emacs reads the `init.el` file properly and will remind people (ok,
    it'll remind you) to make edits to `init.org` and not to `init.el`.

        #+begin_src emacs-lisp
        -*- mode: org; fill-column: 78; -*-
        #+TITLE: Emacs configuration file
        #+AUTHOR: Tammy Cravit
        #+DATE: Time-stamp: <2020-04-05 10:08:30 tammy>
        #+BABEL: :cache yes
        #+LATEX_HEADER: \usepackage{parskip}
        #+LATEX_HEADER: \usepackage{inconsolata}
        #+LATEX_HEADER: \usepackage[utf8]{inputenc}
        #+PROPERTY: header-args :tangle init.el
        #+end_src

    If you *do* plan on using LaTeX to typeset your documentation, you
    should also install the
    [Inconsolata](https://fonts.google.com/specimen/Inconsolata) font.

-   **The auto-tangling code.** This bit of [Emacs
    lisp](https://www.gnu.org/software/emacs/manual/html_node/elisp/)
    magic -- which is included into your `init.el` file and thereby
    automatically loaded -- tells Emacs to automatically tangle
    `init.org` and produce a new `init.el` file every time the
    `init.org` file is saved.

        #+begin_src emacs-lisp
          ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
          ;; Automatically tangle init.org on save to produce init.el
          ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

          (defvar user/init-org-file (concat user-emacs-directory "init.org"))
          (defvar user/init-el-file  (concat user-emacs-directory "init.el"))

          (defun tangle-init ()
            "If the current buffer is 'init.org' the code-blocks are
          tangled, and the tangled file is compiled."
            (when (equal (buffer-file-name)
                         (expand-file-name user/init-org-file ))
              ;; Avoid running hooks when tangling.
              (let ((prog-mode-hook nil))
                (org-babel-tangle)
                (byte-compile-file user/init-el-file))))

          (add-hook 'after-save-hook 'tangle-init)
        #+end_src

-   **The rest of your Emacs configuration.** I like to structure this
    part of the file with headings for each functional area, and to
    intersperse descriptions of each customization or group of
    customizations in with the code blocks. Here's an example of a bit
    of the UI customization from my `init.org`:

        *** UI Customizations

        Show the full path in the title bar.

        #+begin_src emacs-lisp
          (setq-default frame-title-format "%b (%f)")
        #+end_src

        Disable the font popup menu.

        #+begin_src emacs-lisp
          (global-set-key (kbd "s-t") '(lambda () (interactive)))
        #+end_src

        ***** Frame Size/Position

        Set the initial window size and position if we're running in a GUI. If
        we only have one monitor (like on an undocked laptop) we'll start the
        window maximized.

        #+begin_src emacs-lisp
        (if window-system
          (progn
            (if (eq tlc/number-of-displays 1)
                ;; One monitor - make the window shorter and mazimize it
                (setq initial-frame-alist '((top . 5) (left . 5) (width . 132)
                                            (height . 28)
                                            (fullscreen . maximized)))
              ;; Multiple monitors - taller window, not maximized
              (setq initial-frame-alist '((top . 15) (left . 15)
                                          (width . 132) (height . 38))))
            (setq default-frame-alist initial-frame-alist)))
        #+end_src

As you can see, the code and documentation can be fluidly and easily
mixed, and documented code listings can be easily produced. This is the
primary payoff of going to all this trouble.

I won't talk about what specifically you should put into your
`init.org`. Everyone sets up Emacs differently for their needs and
preferences. The [Emacs Wiki](https://www.emacswiki.org/) has
[links](https://www.emacswiki.org/emacs/ExampleConfigurations) to some
good examples. You can also look at [my
configuration](https://github.com/tammymakesthings/emacs_d) for
inspiration. But again, remember that my needs and preferences might not
match yours!

One more quick tip: If you want a specific block of code in your
`init.org` file to be written to a file other than `init.org` (for
example, if you want to create specific configurations for specific
systems you use), you can include `:tangle filename.el` at the end of a
`#+begin_src` line. So in my `init.org`, I have code like the following:

    *** Load OS-specific files

    This defines a system-specific file by OS type (Windows, Mac, etc.) so
    specific settings can be overridden.

    #+begin_src emacs-lisp
    (let ((system-file (concat user-emacs-directory
                               "settings-os-" (subst-char-in-string ?/ ?-
                                              (symbol-name system-type)) ".el")))
        (if (file-exists-p system-file)
          (load-file system-file)))
    #+end_src

    ***** System-Specific FIle - Linux

    #+begin_src emacs-lisp :tangle settings-os-gnu-linux.el
      ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
      ;; OS-specific settings - Linux
      ;; Tangled from init.org - do not modify directly
      ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

      (do-some-customization)
      (provide 'settings-os-gnu-linux)
    #+end_src

    ***** System-Specific File - Windows

    #+begin_src emacs-lisp :tangle settings-os-windows-nt.el
      ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
      ;; OS-specific settings - Windows
      ;; Tangled from init.org - do not modify directly
      ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

      (provide 'settings-os-windows-nt)
    #+end_src

If you have some code in your `init.org` that you want to keep but that
you don't want to output to your `init.el` (for example, if you want to
temporarily disable a customization but you don't want to throw it
away), you can write this:

    #+begin_src emacs-lisp :tangle no
    ;; This code will not get written to your init.el file.
    (do-stuff)
    #end_src

So there you have it! I know there's some initial overhead in getting
this set up, but I find that being able to comprehensively document my
code (with formatting and hyperlinks and stuff) makes it MUCH easier to
understand later. And this capability isn't limited to just your Emacs
configuration - you can write code in many languages and tangle out your
source files and documentation automatically! The org-mode
[manual](https://orgmode.org/manual/Working-with-Source-Code.html#Working-with-Source-Code)
has lots more information about how this works.
