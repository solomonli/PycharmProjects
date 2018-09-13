'''print("Please enter a positive integer: ", end='')
N = int(input())

if N < 10:
    print(0)
else:
    print(int(N/10) % 10)
'''

n = input()
num = 0 if len(n) == 1 else n[-2]   # fucking smart
print(num)

'''
# first digit of a two-digit number

print(int(input()) // 10)


# the last digit of a number

print(int(input()) % 10)
'''
