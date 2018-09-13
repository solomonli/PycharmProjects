sides = [float(input()) for _ in range(3)]

s = sum(sides) / 2  # half parameter

print('YES' if all([i < s for i in sides]) else 'NO')

# all 'True' is cool!
