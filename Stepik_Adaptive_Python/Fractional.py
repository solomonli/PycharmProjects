import re

N = input()      # e.g. '17.89'
fN = float(N)

print((fN - fN % 1), "{:.3f}".format(fN % 1))

match = re.search(r'[.]\d+', N)     # [] reaches the literal dot

# https://developers.google.com/edu/python/regular-expressions

if match:
    print(match.group()[1])
