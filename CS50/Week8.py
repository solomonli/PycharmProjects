import sys
import cs50

for i in range(65, 65 + 26):        # we can convert characters to ASCII
    print("{} is {}".format(chr(i), i))

print(sys.argv)

if len(sys.argv) == 2:
    print("hello, {}".format(sys.argv[1]))
else:
    print("hello, world")


for i in range(len(sys.argv)):
    print(sys.argv[i])

# print()
'''
for s in sys.argv:
    for c in s:
        print(c)
    print()
'''
'''
# prompt user for x
print("x is ", end="")
x = cs50.get_int()

# prompt user for y
print("y is ", end="")
y = cs50.get_int()

# perform calculations for user
print("{} plus {} is {}".format(x, y, x + y))
print("{} minus {} is {}".format(x, y, x - y))
print("{} times {} is {}".format(x, y, x * y))
print("{} divided by {} is {}".format(x, y, x / y))
print("{} divided by {} (and floored) is {}".format(x, y, x // y))
print("remainder of {} divided by {} is {}".format(x, y, x % y))
'''

if len(sys.argv) != 2:
    print("missing command-line argument")
    exit(1)

print("hello, {}".format(sys.argv[1]))
exit(0)

x = 1
y = 2

print("x is {}".format(x))
print("y is {}".format(y))
print("Swapping...")
x, y = y, x
print("Swapped.")
print("x is {}".format(x))
print("y is {}".format(y))

