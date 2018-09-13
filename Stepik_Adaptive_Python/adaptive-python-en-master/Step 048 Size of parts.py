n = int(input())

detectors = [int(input()) for _ in range(n)]

counts = [detectors.count(i) for i in [0, 1, -1]]

print(*counts)
# https://docs.python.org/3/library/functions.html#print

print(counts)
