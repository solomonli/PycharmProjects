"""
Every class needs a __repr__!
If you don’t add a __str__ method, Python falls back on the result of __repr__ when looking for __str__.
Therefore, Dan Bader recommends that you always add at least a __repr__ method to your classes.

__repr__ goal is to be unambiguous
__str__ goal is to be readable
see the datetime example below
"""
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):  # don't forget 'self'
        return f'a {self.color} car'    # don't forget 'self'


my_car = Car('red', 43211)

print(my_car)
str(my_car)
f'{my_car}'
'{}'.format(my_car)

"""
Conversation with Marc:

x, *y = map(str, range(5))
x, *_ = map(str, range(5))

about the built-in fuction isinstance()
w = 2; 
isinstance(w, int); type(w) == int
"""
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return '__str__ of class Car'

    def __repr__(self):
        return '__repr__ of class Car'


my_car = Car('silver', 56546)

print(my_car)   # __str__
str(my_car)     # __str__
f'{my_car}'     # __str__
my_car          # __repr__
[my_car]        # __repr__
str([my_car])   # __repr__

import datetime

td = datetime.date.today()
td          # datetime.date(2019, 2, 13)
str(td)     # '2019-02-13'
repr(td)    # 'datetime.date(2019, 2, 13)'
type(td)    # datetime.date


def __repr__(self):
    return f'Car({self.color!r}, {self.mileage!r})'
# Please note that I’m using the !r conversion flag to make sure the output string uses
# repr(self.color) and repr(self.mileage)
# instead of str(self.color) and str(self.mileage).


# Here’s a complete example for Python 3, including an optional __str__ implementation:

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return f'a {self.color!r} {__class__.__name__} with ' \
            f'{self.mileage!r} mileage'

    def __str__(self):
        return f'a {self.color} car'

"""
Assertations vs. Exceptions

They should be distinct, but are often confused.The generally accepted defintion of assertaion is 
"A statement of something that MUST be true. If it is not, then your program is broken. 
You cannot recover from a broken program. Fix the bugs!"

An exception, by contrast, is thrown when a condition required for the correct functioning of a method isn't met. 
An exception may be caught and recovered from.

For example, should the user specify a non-existant file, our program may well throw a FileNotFoundException. 
Clearly we can catch it and ask the user for another file name.

By contrast, should the list of free pages plus the list of used pages not equal the list of all pages, we're screwed. 
Some fundamental method in our operating system did something wrong and we have no idea of what else might be wrong. 
So we can't recover.

Assertions should be turned off in the production release.
"""


class NameTooShortError(ValueError):
    pass


def validate(name):
    if len(name) < 10:
        raise NameTooShortError(name)
##################################


class BaseValidationError(ValueError):
    pass

class NameTooShortError(BaseValidationError):
    pass

class NameTooLongError(BaseValidationError):
    pass

class NameTooCuteError(BaseValidationError):
    pass
# For example, this allows users of your package to write try…except statements that
# can handle all of the errors from this package without having to catch them manually:

try:
    validate(name)
except BaseValidationError as err:
    handle_validation_error(err)

################################### To review Handling Exceptions
# https://docs.python.org/3/library/exceptions.html
# https://docs.python.org/3.7/tutorial/errors.html
# https://www.programiz.com/python-programming/exceptions

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except (ValueError, RuntimeError, TypeError, NameError):    # here only the ValueError may be triggered
        print("Oops!  That was no valid number.  Try again...")




