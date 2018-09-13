'''
print("Please enter an integer for the feet the snail drops down: ", end='')
B = int(input())

print("Please enter an integer for the feet the snail climbs up (it should be larger than the above integer): ", end='')
A = int(input())

print("Please enter an integer for the height of the vertical pole (it should be larger than the above integer): ", end='')
H = int(input())

day, night, progress = 0, 0, 0

while progress < H:
    if day == night:
        progress += A
        day += 1
        # print("{}th day".format(day))
        # print("By end of Day, cumulative progress {}".format(progress))
    else:
        progress -= B
        night += 1
        # print("{}th night".format(night))
        # print("By end of Night, cumulative progress {}".format(progress))

print("Current 'theoretical' progress is: {}".format(progress))
print("Total time elapsed: {} daylights and {} nights".format(day, night))
'''

import math


h, a, b = int(input()), int(input()), int(input())      # this is a cool way
d = math.ceil((h - a) / (a - b)) + 1
print(d)
