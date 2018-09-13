print("Please enter two integers: ")
a = int(input())
b = int(input())

if a > b:
    a, b = b, a

lst = list(range(b, a, -3))
print(sum(lst) / len(lst))
