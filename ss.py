"""
3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10
"""

from itertools import product

k, m = map(int, input().split())
l = []

for i in range(k):
    _, *tail = list(map(int, input().split()))
#     tail = list(map(int, input().split()))[1:]
    l.append(tail)

results = map(lambda x: sum(element ** 2 for element in x) % m, product(*l))

print(max(results))
