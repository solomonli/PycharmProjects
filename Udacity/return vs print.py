'''
def multiply(*args):
    z = 1
    for num in args:
        z *= num
    print(z)

multiply(4, 5)
'''


def multiply(*args):
    z = 1
    for num in args:
        z *= num
    return z

multiply(4, 5)
