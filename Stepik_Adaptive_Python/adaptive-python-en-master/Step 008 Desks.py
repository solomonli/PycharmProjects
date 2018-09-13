from math import ceil

students = [int(input()) for _ in range(3)]     # take three inputs to form a list!
# desks = sum(ceil(s/2) for s in students)
desks = ceil(sum(students) / 2)
print(desks)

# students = [20, 21, 22]  # 32
# students = [16, 18, 20]  # 27
