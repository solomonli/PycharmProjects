import math

h, a, b = int(input()), int(input()), int(input())
# height, ascend, descend

d = math.ceil((h - a) / (a - b)) + 1
# count from the 1st night, then +1

print(d)
