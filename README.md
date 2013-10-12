I started solving the problems in [[http://projecteuler.net/|Project Euler]] to exercise my mind, augment my knowledge in general algorithms and maths in general, and to gain practice with specific programming languages, their standard libraries, and the many specialised libraries available out there.

Most of the problems so far have been solved using [[http://www.python.org/|Python]] and [[http://cython.org/|Cython]] even if there are analytical (paper and pencil) solutions to them.

Unlike many of the programs found on the posts readable after you provide the solution on the [[http://projecteuler.net/|project's]] web site, mine are written so that they would work if the specific conditions, like ranges, sums versus products versus single items, change. I also have tried to keep it simple and readable, which means very functional, some procedural, and no OO (at one time I thought I would never say something like that).

Unlike many of the mentioned programs, with every new problem I've gone back to similar or related problems and refactored the relevant code into libraries that are reused accross problems, and I've optimized the library code as harder problems have required it. The individual solutions are written in a way in which the code can be reused (which is what I did before deciding that refactoring to libraries was better).

Modesty set aside, I think that the result of my effort is a library that can be used for tasks from homework to my own professional work.

So far I've approached the problems this way:

# In order.
# Always take a look at the latest published problem, but leave it for later if it seems too hard. The reason for this is provided in the hints at [[http://projecteuler.net/|Project Euler]]: new problems tend to build upon knowledge gained with previous problems (and, in my case, previous code).
# If I get bored, I browse for a problem I that I want to solve or that I find easy to solve and have a take at it.
# I always devise a strategy in my head before coming back to the computer. When I sit at the keyboard, I already know what I'm going to write, except, perhaps, for the workings of a library I haven't used lately.

Since I've already broken shared code while solving new problems, I decided to incorporate either assertions or unit tests (some form of automation) to verify that all problems are solved correctly before publishing changes.

Finally, it makes little sense to look at my code unless you've already solved the problems, you're only interested in the reusable parts, or you have interest in reviewing what I have written.
