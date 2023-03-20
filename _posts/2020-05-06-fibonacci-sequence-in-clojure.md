The Fibonacci Sequence in Clojure
=================================

category

:   programming

tags

:   programming, clojure, math, algorithms

date

:   2020-05-06

I was playing around this morning, and I decided to see what I could
find about implementing the [Fibonacci
sequence](https://en.wikipedia.org/wiki/Fibonacci_number) in Clojure.
For those unfamiliar with the Fibonacci sequence, which is named for a
13th-century [Italian
mathematician](https://en.wikipedia.org/wiki/Fibonacci), it is a
deceptively simple mathematical sequence where each term is constructed
by the following rules:

-   If **n=0**, then **fib(n) = 0**
-   If **n=1**, then **fib(n) = 1**
-   Otherwise, **fib(n) = fib(n-1) + fib(n-2)**

Traditionally, **fib(n)** is constrained to the set of positive
integers.

This sequence doesn't at first seem earth--shatteringly complex or
interesting, but it turns out to describe all sorts of things in nature,
such as the arrangement of leaves on stems, petals on flowers, and the
family trees of bees. It also shows up in many other places in the
fields of mathematics, computer science, and even music.

Implementing the Fibonacci sequence in various programming languages is
a common exercise. A common solution uses
[recursion](https://en.wikipedia.org/wiki/Recursion_(computer_science)).
A simple recursive solution to calculate the Fibonacci sequence in
Clojure might look like this:

``` {.clojure}
(defn recursive-fibonacci
    "Recursive implementation of the Fibonacci sequence."
    [n]
    (cond
      (= n 0) 0
      (= n 1) 1
      :else (+ (recursive-fibonacci (- n 1))
               (recursive-fibonacci (- n 2)))))

(map recursive-fibonacci [0 1 2 3 4 5 6 7 8 9])
```

You might implement something like this and think your job is done. But
the recursive solution has two big problems: It's *verrrry* slow, and if
you give it a very big value of `n`, the Java Virtual Machine in which
your Clojure code is running will eventually run out of heap space and
crash. So let's look at a couple other ways we could solve this problem
in Clojure.

Tail Recursion
--------------

[Tail recursion](https://en.wikipedia.org/wiki/Tail_call) allows the
runtime to reuse memory locations for each subsequent call to our
function. In Clojure, this is accomplished by the `recur` form, which
might look like this:

``` {.clojure}
(defn tail-recursive-fibonacci
    "Tail-recursive version of the fibonacci sequence."
    [n]
    (if (> n 1)
        (loop [x 1
               fib0 0
               fib1 1]
            (if (< x n)
                (recur
                  (inc x)
                  fib1
                  (+ fib0 fib1))
                fib1))
    n))

(map tail-recursive-fibonacci [0 1 2 3 4 5 6 7 8 9])
```

What's happening here? The
[recur](https://clojuredocs.org/clojure.core/recur) form in Clojure
implements tail recursion. So, let's look at what happens if we invoke
`(tail-recursive-fibonacci 6)`:

-   On entry, `n=6` (so we do the looping thing instead of just
    returning n)
-   Now we go through the loop:
    -   `x = 1, fib0 = 0, fib1 = 1`
    -   `x = 2, fib0 = 1, fib1 = 1`
    -   `x = 3, fib0 = 1, fib1 = 2`
    -   `x = 4, fib0 = 2, fib1 = 3`
    -   `x = 5, fib0 = 3, fib1 = 5`
    -   `x = 6, fib0 = 5, fib1 = 8`
-   We've got our answer, `(tail-recursive-fibonacci 6) = 8`.

This is more memory-efficient and won't crash if you give it a bigger
number for `n`, but let's look at a couple of more idiomatic ways to
solve the problem.

lazy-seq
--------

A [lazy sequence](https://clojuredocs.org/clojure.core/lazy-seq)
essentially creates an iterable
[sequence](https://clojure.org/reference/sequences) whose values are
calculated as needed and then cached. This is more efficient than a
recursive function, and also runs faster. We can create a lazy sequence
using the [lazy-seq](https://clojuredocs.org/clojure.core/lazy-seq)
form.

The lazy sequence version of the Fibonacci sequence looks like this:

``` {.clojure}
(def lazy-sequence-fibonacci
    "Create a lazy sequence version of the Fibonacci sequence."
    (
     (fn fib [a b] (lazy-seq (cons a (fib b (+ a b)))))
      0 1))

(take 10 lazy-sequence-fibonacci)
```

Something to notice here is that we're using `def` instead of `defn`.
This is because we're not creating a function; rather, we're creating a
sequence that provides the next element each time we access it. (That's
also why I've switched my sample invocations from here out to use `take`
instead of `map` - ClojureScript was giving me errors in the browser. I
guess you can't `take` something that's not "seqable" in ClojureScript.)

lazy-cat
--------

Clojure also provides the
[lazy-cat](https://clojuredocs.org/clojure.core/lazy-cat) form, which is
a shortcut that essentially does a
[concat](https://clojuredocs.org/clojure.core/concat) inside of a
`lazy-seq` to collect our results. Here's what the Fibonacci sequence
looks like with `lazy-cat`:

``` {.clojure}
(def lazy-cat-fibonacci
    (lazy-cat [0 1]
        (map + (rest lazy-cat-fibonacci) lazy-cat-fibonacci)))

(take 10 lazy-cat-fibonacci)
```

iterate
-------

One more example. This one uses the
[iterate](https://clojuredocs.org/clojure.core/iterate) form. `iterate`
takes a sequence, and on each iteration it returns the next value from
the sequence and also a
[closure](https://en.wikipedia.org/wiki/Closure_(computer_programming))
that will return the *next* element. It looks like this:

``` {.clojure}
(def seq-iterate-fibonacci
    (map first (iterate (fn [[a b]] [b (+ a b)]) [0 1])))

(take 10 seq-iterate-fibonacci)
```

### Comparing Performance

To be honest, I'm new enough to Clojure that I'm not sure I totally
understand the relative advantages and disadvantages of `lazy-seq`,
`lazy-cat` and `iterate`, and why you'd use one versus the others. (I'm
going to try to work it out, and then I'll do another blog post!) But I
did time the execution speed of these various methods, collecting the
first 80 Fibonacci numbers from each. Here's what I got running my [test
code](https://tammymakesthings.com/code/fib.clj) in the
[REPL](https://clojure.org/guides/repl/introduction):

    Clojure 1.10.1
    user=> (load-file "fib.clj")
    ***********************************************************************
    *          Fibonacci Sequence - Clojure Implementation Tester         *
    ***********************************************************************
    => recursive fibonacci - 50  repetitions:
    "Elapsed time: 0.036135 msecs"

    => tail recursive fibonacci - 50  repetitions:
    "Elapsed time: 0.004389 msecs"

    => lazy-seq fibonacci - 50  repetitions:
    "Elapsed time: 0.004584 msecs"

    => lazy-cat fibonacci - 50  repetitions:
    "Elapsed time: 0.003567 msecs"

    => iterate fibonacci - 50  repetitions:
    "Elapsed time: 0.004653 msecs"

    true
    user=>

There wasn't a lot of performance variation in my tests, except that the
recursive implementation was consistently a LOT slower (913% slower, in
this test run.)

Even if I don't yet understand the reasons for picking between these
various ways of solving the same problem, I do have a better
understanding of the tools at my disposal.
