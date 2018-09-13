def num2sum(x):
    digits = [int(i) for i in str(x)]
    return sum(digits)


def find_num(n):
    count = 0
    for x in range(n):
        if num2sum(x) == num2sum(n):
            count += 1
    return count


print("Please enter a positive integer: ", end='')
lmt = int(input())
print(find_num(lmt))
