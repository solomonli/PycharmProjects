print("Please type in numbers line by line (0 for cessation): ")
i = int(input())
s = 0

while i != 0:
    s += i
    i = int(input())

print(s)
