'''print("Please enter the dollar (integer): ", end='')
d = int(input())
print("Please enter the cent (integer): ", end='')
c = int(input())
print("Please enter the pizza units (integer): ", end='')
N = int(input())

D = d*N
C = c*N

if C >= 100:
    D += C // 100
    C %= 100

print(D, C)'''

a, b, n = [int(input()) for _ in range(3)]
# # a, b, n = 10, 15, 2  # 20 30
# a, b, n = 2, 50, 4  # 10 0
cost = 100 * a * n + b * n
print(cost // 100, cost % 100)
