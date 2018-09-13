# import pprint

words = input().split()
lengths = list(map(len, words))
d = {l: lengths.count(l) for l in sorted(set(lengths))}

for length, amount in d.items():
    print('{}: {}'.format(length, amount))

# pprint.pprint(d)
# I didn't get desired result with pprint; maybe I can refer to the Jupyter note
