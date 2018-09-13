class Robot:
    def __init__(self, name=None):
        self.name = name

    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")

'''
https://www.python-course.eu/python3_object_oriented_programming.php
'''

# if __name__ == "__main()__":
x = Robot()
y = Robot()
y1 = y
print(x == y, y == y1)

x.name = 'Tiida'
x.build_year = '2007'
print(x.name)
print(x.__dict__)

Robot.brand = 'Toyota'
print(x.brand, y.brand)

y.country = 'Japan'

print(x.__dict__, y.__dict__)
print(Robot.__dict__)

def hi(obj):
    print("hi! I am " + obj.name)

# hi(x)

x.say_hi()
y.say_hi()
z = Robot("HRV")
z.say_hi()