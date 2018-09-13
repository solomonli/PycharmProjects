def letters(s, a, b):
    if s.count(a) == 0:
        return 0
    if a in b:
        return 'Impossible'
    count = 0
    while a in s:
        s = s.replace(a, b)
        count += 1
    return count

s, a, b = (input() for _ in range(3))
print(letters(s, a, b))

# As input your program receives the three strings – s, a, b,
# consisting of lowercase letters of the Latin alphabet.
# In a single operation you can exchange all the occurrences of string a in s to the string b.
