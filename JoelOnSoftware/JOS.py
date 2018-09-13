'''

def Cook(i1, i2, f):
    print("get the " + i1)
    f(i1)
    f(i2)


Cook("lobster", "water", lambda x: print("pot " + x))

Cook("chicken", "coconut", lambda x: print("boom " + x))

'''

a = [1, 2, 3]

for i in range(len(a)):
    a[i] *= 2

for i in range(len(a)):
    print(a[i])
