I started solving the problems in `Project Euler`_ to exercise my mind, to augment my knowledge about algorithms and math, and to gain practice with specific programming languages, their standard libraries, and the many specialised libraries available out there.

.. _`Project Euler`: http://projecteuler.net/

Most of the problems so far have been solved using Python_ and Cython_ even if there are analytical (paper and pencil) solutions to them.

.. _Python: http://www.python.org/
.. _Cython: http://cython.org/

Unlike many of the programs found on the posts readable after you provide the solution on the project_'s web site, mine are written so that they would work if the specific conditions, like ranges or sums versus products versus single items, change. I also have tried to keep the code simple and readable, which means it is mostly functional, some of it procedural, and none of it OO (Who would have thought I would ever say something like that?).

.. _project: http://projecteuler.net/

Unlike many of the mentioned programs, with every new problem I've gone back to similar or related problems and refactored the relevant code into libraries that are reused throughout. I've also optimized the library code as harder problems have required it. The individual solutions are written in a way in which the code can be reused (which is what I did before deciding that refactoring to libraries was better). The result of my effort is a library that can be used for many different tasks, from homework to professional work.

So far I've approached the problems this way:

#. In order.
#. Always take a look at the latest published problem, but leave it for later if it seems too hard. The reason for this is provided in the hints at `Project Euler`_: new problems tend to build upon knowledge gained with previous problems (and, in my case, previous code).
#. If I get bored, I browse for a problem I that I want to solve or that I find easy to solve and have a take at it.
#. I always devise a strategy in my head before coming back to the computer. When I sit at the keyboard, I already know what I'm going to write, except, perhaps, for the workings of a library I haven't used lately.

Because at times I broke existing shared code while solving new problems, I decided to incorporate either assertions or unit tests to verify that all problems are solved correctly before publishing any changes.

Finally, it makes little sense to look at the code unless you've already solved the problems, you're only interested in the reusable parts, or you want to review what I have written for other reasons.

To run the tests just issue::

    python tests.py

at the commandline. The tests won't work with optimizations (``-O``) enabled because of the reliance on Python_ assertions.

Tu solve the problems, run each ``src/eulerXXX.py`` program individually.
