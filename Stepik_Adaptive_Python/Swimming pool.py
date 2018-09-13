n, m, x, y = [int(input()) for _ in range(4)]   # cool way!

d = min(x, min(n, m) - x, y, max(n, m) - y)
print(d)
