class Complex:
    def create(self, real_part, imag_part):
        self.r = real_part
        self.i = imag_part

"Current position {latitude} {longtitude}".format(latitude="60N",
                                                  longtitude="12E")

"Reticulating spline {} of {}".format(4, 23)

g = [1, 11, 21, 1211, 111221]
g.reverse()

import sys

def convert(s):
    """Convert to an integer."""
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("conversion error: {}".format(str(e)),
              file=sys.stderr)
        raise


from math import log

def string_log(s):
    v = convert(s)
    return log(v)


def sqrt(x):
    """
    using the method of Heron of Alexadria
    :param x: the number for which the square root is to be computed
    :return: the square roof of x
    :raises:
        ValueError: If x is negative.
    """

    if x < 0:
        raise ValueError("Cannot compute square root "
                         "of negative number {}".format(x))

    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess

import sys

def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
        print("This is never printed.")
    except ValueError as e:
        print(e, file=sys.stderr)

    print("Program execution continues normally here.")


if __name__ == '__main__':
    main()

country_capital = {'Germany':'Berlin', 'France':'Paris'}
ii = country_capital.items()
type(ii)


def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")
first(['1st', '2nd', '3rd'])
first({'1st', '2nd', '3rd'})
first(set())

