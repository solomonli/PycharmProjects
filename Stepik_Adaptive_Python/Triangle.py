sides = [int(input()) for _ in range(3)]

p = sum(sides)

print('YES' if all([2*s < p for s in sides]) else 'NO')

'''
The basic triangle inequality is
a<b+c, b<c+a, c<a+b

or equivalently
{max(a,b,c)}<s      - semi-parameter

'''
