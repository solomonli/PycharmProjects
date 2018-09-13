with open('Input step 077 The slice of string.txt', 'r') as file:
    s = file.readline().strip()
    # print(s)
    a, b, c, d = (int(i) for i in file.readline().strip().split())
    print(s[a: b + 1], s[c: d + 1])

# strip =>
'''
        Return a copy of the string S with leading and trailing
        whitespace removed.
        If chars is given and not None, remove characters in chars instead.'''

