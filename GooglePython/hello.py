#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""A tiny Python program to check that Python is working.
Try running this program from the command line like this:
  python3 hello.py
  python3 hello.py Alice
That should print:
  Hello World -or- Hello Alice
Try changing the 'Hello' to 'Howdy' and run again.
Once you have that working, you're ready for class -- you can edit
and run Python code; now you just need to learn Python!
"""

import sys
import os
import random

# Define a main() function that prints a little greeting.


def main():
    # Get the name from the command line, using 'World' as a fallback.
    if len(sys.argv) >= 2:
        name = sys.argv[1]
    else:   # super important to understand this part
        name = 'World'
    print('Hello', name)

    random_num = random.randrange(0, 10)
    while random_num != 5:
        print(random_num)
        random_num = random.randrange(0, 10)
    # run the test until a successful event occurs - geometric distribution

    # The probability distribution of the number X of Bernoulli trials needed to get one success,
        # supported on the set { 1, 2, 3, ...}
    # The probability distribution of the number Y = X − 1 of failures before the first success,
        # supported on the set { 0, 1, 2, 3, ... }

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
