from functools import reduce


def heron(sides):
    p = sum(sides) / 2
    s = p * reduce(lambda x, y: x * y, [p - i for i in sides])
    return s ** 0.5

print(heron([int(input()) for _ in range(3)]))

'''
Apply REDUCE function of two arguments cumulatively to the items of sequence, from left to right, 
so as to reduce the sequence to a single value. 
For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5). 
The left argument, x, is the accumulated value and the right argument, 
y, is the update value from the sequence. 
If the optional initializer is present, it is placed before the items of the sequence
 in the calculation, and serves as a default when the sequence is empty. 
If initializer is not given and sequence contains only one item, the first item is returned.
'''
