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
    return f'{name}, {line}!'


print(say('Jane', 'Come'))
