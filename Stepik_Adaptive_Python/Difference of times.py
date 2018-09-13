print("Please enter a clock time of hour, minute and second, line by line: ")
h1 = int(input())
m1 = int(input())
s1 = int(input())

print("Please enter a newer clock time of hour, minute and second, line by line: ")
h2 = int(input())
m2 = int(input())
s2 = int(input())

diff = (h2 - h1) * 3600 + (m2 - m1) * 60 + (s2 - s1)
print("The time different between is {} seconds: ".format(diff))

'''
time1 = [int(input()) for _ in range(3)]
time2 = [int(input()) for _ in range(3)]

units = [3600, 60, 1]
diff = sum(units[i] * (time2[i] - time1[i]) for i in range(3))
print(diff)
'''
