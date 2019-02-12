def foo(x, *args, **kwargs):
    new_args = args + ('extra', )
    kwargs[name] = 'Alice'
    bar(x, *new_args, **kwargs)


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

print_vector(*tuple_vector)
print_vector(*list_vector)

genexpr = (x**3 for x in range(3))

print_vector(*genexpr)

dict_vec = {'y': 10, 'z': 20, 'x': 30}

print_vector(*dict_vec)
print_vector(**dict_vec)

