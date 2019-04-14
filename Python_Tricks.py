'''
READING THE BOOK "PYTHON TRICKS"

Assertions declare some """conditions as impossible""" in your code. They are not a mechanism for handling run-time errors.
'''

with open('hello.txt', 'w') as f:
    f.write('hello, world!')


list()
# []
_
# []

# "_" to indicate a temporary value, something you don't care


# LITERAL STRING INTERPOLATION (Python 3.6+)
name = 'Tom'
f'Hello, {name}!'
# 'Hello, Tom!'

a = b = 5
f'Five plus five is {a+b}, not {2 * (a+b)}.'
# 'Five plus five is 10, not 20'


def greet(name, question):
    return f"Hello, {name}! How's it {question}?"


greet('Tom', 'going')
# "Hello, Tom! How's it going?"


def get_speak_func(text, volume):

    def whisper():
        return text.lower()

    def yell():
        return text.upper()

    if volume > 0.5:
        return yell
    else:
        return whisper


get_speak_func('hey', 0.7)()
# get_speak_func('hey', 0.7)    please try this to find "<function __main__.get_speak_func.<locals>.yell()>"


def make_adder(n):
    def add(x):
        return x + n
    return add


plus_3 = make_adder(3)
plus_3(4)


class Adder:

    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return self.n + x


plus_4 = Adder(4)
plus_4(3)


callable(plus_3)
callable(plus_4)
callable('hello')

add = lambda x, y: x + y
add(3, 5)

(lambda x, y: x + y)(3, 5)

tuples = [(1, 'd'), (2, 'b'), (3, 'c'), (4, 'a')]
sorted(tuples, key=lambda x: x[1])

sorted(range(-10, 11), key=lambda x: x**2)


def make_adder2(n):
    return lambda x: x + n


plus_5 = make_adder2(5)
plus_5(5)


def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper


def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper


@strong
@emphasis
def greeting():
    return 'Hello!'


print(greeting())


def trace(func):
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() '
              f'with {args}, {kwargs}')

        original_result = func(*args, **kwargs)

        print(f'TRACE: {func.__name__}() '
              f'returned {original_result}')

        return original_result

    return wrapper


@trace
def say(name, line):
    return f'{name}: {line}!'


print(say('Jane', 'Come'))

############################################
def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper


@uppercase
def greet():
    '''
    input nothing
    :return: the pre-set string
    '''
    return 'Hi, there!'


print(greet(), greet.__name__, greet.__doc__, sep='\n')

# see the problem of the decrator UPPERCASE?
############################################
import functools


def uppercase(func):
    @functools.wraps(func)      # a cool line!
    def wrapper():
        return func().upper()
    return wrapper


@uppercase
def greet():
    """
    input nothing
    :return: the pre-set string
    """
    return 'Hi, there!'


print(greet(), greet.__name__, greet.__doc__, sep='\n')

# yeah!~~


def foo(required, *args, **kwargs):
    print(required)

    if args:
        print(args)

    if kwargs:
        print(kwargs)


foo('Hey!', 2, 2, key1='a', key2='b')

# hey
# (2, 2)
# {'key1': 'a', 'key2': 'b'}

def foo(x, *args, **kwargs):
    new_args = args + ('extra', )
    kwargs[name] = 'Alice'
    bar(x, *new_args, **kwargs)
# demonstrated a way to edit a function's arguments

import functools


def trace(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        print(f, args, kwargs)
        result = f(*args, **kwargs)
        print(result)
    return decorated_function


@trace
def greet(greeting, name):
    return f'{greeting}, {name}!'


greet('Hello', 'Bob')


def print_vector(x, y, z):
    print(f'<{x}, {y}, {z}>')


print_vector(0, 1, 5)

tuple_vector = (1, 2, 4)
list_vector = [1, 2, 4]

print_vector(*tuple_vector)     # unpacking function arguments
print_vector(*list_vector)

genexpr = (x**3 for x in range(3))

print_vector(*genexpr)  # perfect example to unpack an iterator

dict_vec = {'y': 10, 'z': 20, 'x': 30}

print_vector(*dict_vec)     # keys
print_vector(**dict_vec)    # values

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
# repr(self.color) and repr(self.mileage) instead of str(self.color) and str(self.mileage).


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

"""
The try statement works as follows:

First, the try clause (the statement(s) between the try and except keywords) is executed.
If no exception occurs, the except clause is skipped and execution of the try statement is finished.
If an exception occurs during execution of the try clause, the rest of the clause is skipped. 
Then if its type matches the exception named after the except keyword, the except clause is executed, 
and then execution continues after the try statement.
If an exception occurs which does not match the exception named in the except clause, 
it is passed on to outer try statements; if no handler is found, 
it is an unhandled exception and execution stops with a message as shown above.
"""

# The raise statement allows the programmer to force a specified exception to occur. For example:
raise NameError('HiThere')

# how to make shallow copies
new_list = list(original_list)
new_dict = dict(original_dict)
new_set = set(original_set)


import copy
copy.copy()
copy.deepcopy()

from collections import namedtuple

Car = namedtuple('Car', 'color mileage')        # creates a blueprint (like a class)

my_car = Car('red', 123456)
my_car.color
# 'red'

my_car
# Car(color='red', mileage=123456)

my_car.color = 'blue'
# AttributeError: can't set attribute

ElectricCar = namedtuple('ElectricCar', Car._fields + ('charge', ))
ElectricCar('silver', 1243, 35.5)
# ElectricCar(color='silver', mileage=1243, charge=35.5)

"""some Built-in Helper Methods"""
my_car._asdict()
# OrderedDict([('color', 'red'), ('mileage', 123456)])

json.dump(my_car._asdict())
# '{"color": "red", "mileage": 123456}'

my_car._replace(color='blue')       # it makes a shallow copy of a tuple and replaces some of the fields
# Car(color='blue', mileage=123456)
my_car      # the my_car instance remains unchanged
# Car(color='red', mileage=123456)

Car._make(['black', 987])     # create a namedtuple instance from a sequence or iterable
# Car(color='black', mileage=987)

"""
Class variables vs. Instance variables:
CVs are in the blueprint and they apply to all the instances by default. 
MODIFING A CLASS VARABLE AFFECTS ALL OBJECT INSTANCES AT THE SAME TIME. 
"""

class Dog:
    num_leg = 4     # Class variable

    def __init__(self, name):
        self.name = name        # Instance variable

jack = Dog('Jack'); jill = Dog('Jill')
jack.name, jill.name        # print the names

jack.num_leg, jill.num_leg, Dog.num_leg     # (4, 4, 4)

Dog.name        # AttributeError: type object 'Dog' has no attribute 'name'

Dog.num_leg = 6
jack.num_leg, jill.num_leg, Dog.num_leg     # (6, 6, 6)

Dog.num_leg = 4; jack.num_leg = 6
jack.num_leg, jill.num_leg, Dog.num_leg     # (6, 4, 4)     Jill was updated due the overridden blueprint

jack.num_leg, jack.__class__.num_leg        # (6, 4)        the instance and the class

class CountedObject:
    num_instances = 0

    def __init__(self):
        self.__class__.num_instances += 1

CountedObject.num_instances, CountedObject().num_instances, CountedObject().num_instances, \
CountedObject().num_instances, CountedObject.num_instances
# (0, 1, 2, 3, 3) The counter works!

"""
class BuggyCountedObject:
    num_instances = 0

    def __init__(self):
        self.num_instances += 1

BuggyCountedObject.num_instances, BuggyCountedObject().num_instances, BuggyCountedObject().num_instances, \
BuggyCountedObject().num_instances, BuggyCountedObject.num_instances
# (0, 1, 1, 1, 0) a buggy counter!
"""

# Instance, Class, and Static Methods Demystified


class MyClass:
    """
    MyClass was setup in such a way that each method's implementation returns a tuple containing information
    we can use to trace what's going on and which part of the class or object that method can access.
    """
    def method(self):
        return 'instance method called', self
        # “By the way, instance methods can also access the class itself through the self.__class__ attribute.
        # This makes instance methods powerful in terms of access restrictions—they can
        # freely modify state on the object instance and on the class itself.”
        # [Solomon] I don't quite understand this part

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


obj = MyClass()

obj.method()    # ('instance method called', <__main__.MyClass at 0x10bfb7358>)
MyClass.method(obj)     # ('instance method called', <__main__.MyClass at 0x10bfb7358>)

obj.classmethod()   # ('class method called', __main__.MyClass)

obj.staticmethod()  # 'static method called'

MyClass.classmethod()   # ('class method called', __main__.MyClass)
MyClass.staticmethod()  # 'static method called'
MyClass.method()    # TypeError: method() missing 1 required positional argument: 'self'


class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'


Pizza(['cheese', 'tomatoes'])

import numpy as np
np.random.rand()
