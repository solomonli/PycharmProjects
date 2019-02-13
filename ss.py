"""
Every class needs a __repr__!
If you don’t add a __str__ method, Python falls back on the result of __repr__ when looking for __str__.
Therefore, Dan Bader recommends that you always add at least a __repr__ method to your classes.


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

tt = datetime.date.today()
tt          # datetime.date(2019, 2, 13)
str(tt)     # '2019-02-13'
repr(tt)    # 'datetime.date(2019, 2, 13)'
type(tt)    # datetime.date


def __repr__(self):
    return f'Car({self.color!r}, {self.mileage!r})'
# Please note that I’m using the !r conversion flag to make sure the output string uses
# repr(self.color) and repr(self.mileage)
# instead of str(self.color) and str(self.mileage).



