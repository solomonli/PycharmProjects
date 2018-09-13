class Animal:
    def __init__(self, name, color):  # technically, it's called 'instantiation'
        self.name = name
        self.color = color


class Cat(Animal):
    def purr(self):
        print("Purr...")

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)


class Dog(Animal):  # inherit from a superclass Animal
    legs = 4

    def bark(self):
        print("Woof!")  # here return won't yield the desired result

fido = Dog("Fido", "brown")


class Student:
    def __init__(self, name):
        self.name = name

    def sayHi(self):
        print("Hi from " + self.name)

s1 = Student("Amy")


def main():
    print(felix.color)
    print(fido.name)
    fido.bark()
    print(fido.legs)    # from a instance of class
    print(Dog.legs)    # from class itself
    s1.sayHi()


if __name__ == "__main__":
    main()


class A:
    def method(self):
        print(1)


class B(A):
    def method(self):
        print(2)

B().method()    # If a class inherits from another with the same attributes or methods, it overrides them.


class A:
    def method(self):
        print("A method")


class B(A):
    def another_method(self):
        print("B method")


class C(B):
    def third_method(self):
        print("C method")

c = C()
c.method()    # Inheritance can also be indirect.
# One class can inherit from another, and that class can inherit from a third class.
c.another_method()
c.third_method()


class A:
    def a(self):
        print(1)


class B(A):
    def a(self):
        print(2)


class C(B):
    def c(self):
        print(3)


c = C()
c.a()    # this is a tricky problem; plz read the code carefully


class A:
    def spam(self):
        print(1)


class B(A):
    def spam(self):
        print(2)
        super().spam()
        # The function super is a useful inheritance-related function that refers to the parent class.
        # It can be used to find the method with a certain name in an object's superclass.

B().spam()


class Vector2D:
    def __init__(self, x, y):    # __xx__ called magic method
        self.x = x
        self.y = y

    def __add__(self, other):    # operator overloading
        return Vector2D(self.x + other.x, self.y + other.y)
        # Once it's defined, we can add two objects of the class together.

first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)

"""
More magic methods for common operators:
__sub__ for -
__mul__ for *
__truediv__ for /
__floordiv__ for //
__mod__ for %
__pow__ for **
__and__ for &
__xor__ for ^
__or__ for |

The expression x + y is translated into x.__add__(y). 
However, if x hasn't implemented __add__, and x and y are of different types, 
then y.__radd__(x) is called. 
"""


class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)

"""
Python also provides magic methods for comparisons.
__lt__ for <
__le__ for <=
__eq__ for ==
__ne__ for !=
__gt__ for >
__ge__ for >=

If __ne__ is not implemented, it returns the opposite of __eq__. 
There are no other relationships between the other operators.
"""


class SpecialString2:
    def __init__(self, cont):
        self.cont = cont

    def __gt__(self, other):
        for index in range(len(other.cont)+1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)

spam = SpecialString2("spam")
eggs = SpecialString2("eggs")
# print(spam); print(eggs)
spam > eggs

"""
There are several magic methods for making classes act like containers.
__len__ for len()
__getitem__ for indexing
__setitem__ for assigning to indexed values
__delitem__ for deleting indexed values
__iter__ for iteration over objects (e.g., in for loops)
__contains__ for in

There are many other magic methods that we won't cover here, 
such as __call__ for calling objects as functions, 
and __int__, __str__, and the like, for converting objects to built-in types. 
"""

import random


class VagueList:
    def __init__(self, cont):
        self.cont = cont

    def __getitem__(self, index):
        return self.cont[index + random.randint(-1, 1)]

    def __len__(self):
        return random.randint(0, len(self.cont)*2)

vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])
# We have overridden the len() function for the class VagueList to return a random number.
# The indexing function also returns a random item in a range from the list, based on the expression.

"""Which magic method call is made by x[y] = z?
x.__setitem__(y, z)"""

"""
a = 42  # Create object <42>
b = a  # Increase ref. count  of <42> 
c = [a]  # Increase ref. count  of <42> 

del a  # Decrease ref. count  of <42>
b = 100  # Decrease ref. count  of <42> 
c[0] = -1  # Decrease ref. count  of <42>
"""
#################################
"""
#Weakly# private methods and attributes have a single underscore at the beginning.
This signals that they are private, and shouldn't be used by external code. 
However, it is mostly only a convention, and does not stop external code from accessing them. 
Its only actual effect is that 
# from module_name import * #
won't import variables that start with a single underscore.
"""


class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):  # The __repr__ magic method is used for string representation of the instance.
        return "Queue({})".format(self._hiddenlist)


queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)  # the attribute _hiddenlist is marked as private,
# but it can still be accessed in the outside code.

"""
#Strongly# private methods and attributes have a double underscore at the beginning of their names. 
This causes their names to be mangled, which means that they can't be accessed from outside the class. 
The purpose of this isn't to ensure that they are kept private, 
but to avoid bugs if there are subclasses that have methods or attributes with the same names.
Name mangled methods can still be accessed externally, but by a different name. 
The method __privatemethod of class Spam could be accessed externally with _Spam__privatemethod.
"""


class Spam:
    __egg = 7

    def print_egg(self):
        print(self.__egg)

s = Spam()
s.print_egg()
print(s._Spam__egg)  # How would the attribute __a of the class b be accessed from outside the class?
# _b__a
# print(s.__egg) this line cannot print

"""
#Methods of objects# we've looked at so far are called by an instance of a class, 
which is then passed to the self parameter of the method.
#Class methods# are different - they are called by a class, 
which is passed to the cls parameter of the method. 
A common use of these are factory methods, which instantiate an instance of a class, 
using different parameters than those usually passed to the class constructor. 
Class methods are marked with a classmethod decorator.
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        # new_square is a class method and is called on the class, rather than on an instance of the class.
        # It returns a new object of the class cls.
        return cls(side_length, side_length)
# Technically, the parameters self and cls are just conventions; they could be changed to anything else.
# However, they are universally followed, so it is wise to stick to using them.
square = Rectangle.new_square(5)
print(square.calculate_area())


class Person:
    def __init__(self, name):
        self.name = name

    @classmethod
    def sayHi(cls):
        print("Hi")

"""
Static methods are similar to class methods, 
except they don't receive any additional arguments; 
they are identical to normal functions that belong to a class. 
They are marked with the staticmethod decorator.
"""


class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True
    # Static methods behave like plain functions,
    # except for the fact that you can call them from an instance of the class.

ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)

"""Properties provide a way of customizing access to instance attributes. 
They are created by putting the property decorator above a method, 
which means when the instance attribute with the same name as the method is accessed, 
the method will be called instead. 
One common use of a property is to make an attribute read-only.
"""


class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def pineapple_allowed(self):
        return False


pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
# pizza.pineapple_allowed = True # this will get an error, "AttributeError: can't set attribute"

"""
Properties can also be set by defining setter/getter functions.
The setter function sets the corresponding property's value.
The getter gets the value.
To define a setter, you need to use a decorator of the same name as the property, 
followed by a dot and the setter keyword.
The same applies to defining getter functions.
"""


class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False

    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter  # a decorator that would be used to add a setter to the property 'pineapple_allowed'
    def pineapple_allowed(self, value):
        if value:
            password = input("Enter the password: ")
        if password == "Sw0rdf1sh!":
            self._pineapple_allowed = value
        else:
            raise ValueError("Alert! Intruder!")

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)

################ to be continued with Regular Expression part
