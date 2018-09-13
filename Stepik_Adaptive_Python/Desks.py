print("Please input three positive integers:")
a = int(input())
b = int(input())
c = int(input())

desks = round((a + b + c) / 2)
print("We need {} desks.".format(desks))

'''
from math import ceil

students = [int(input()) for _ in range(3)]
desks = sum(ceil(s/2) for s in students)
print(desks)

# students = [20, 21, 22]  # 32
# students = [16, 18, 20]  # 27
'''
