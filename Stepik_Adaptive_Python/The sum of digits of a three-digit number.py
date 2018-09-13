
def num2sum(x):
    digits = [int(i) for i in str(x)]
    return sum(digits)

print("Please input a three-digit integer: ", end='')
n = int(input())

print(num2sum(n))

'''
n = input()
print(sum(int(i) for i in n))
'''
