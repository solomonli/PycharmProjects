n = int(input())

i = 1
summands = []
while n >= i:
    summands.append(i)
    n -= i
    i += 1
# print(summands); print(n)
# you can try n = 250

if n > 0:   # the remaining part
    summands[-1] += n

print(*summands)
print("Length = {}".format(len(summands)))
# different from print(summands)

# the whole idea is nice: index from 1, then deduct the index from the n
