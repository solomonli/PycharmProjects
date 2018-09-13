'''
print('Please type in a string of any length: ')
msg = input()   # try something like aaaccccddaaabbc

d = {}

for i in range(0, len(msg)):
    if msg[i] not in d.keys():
        d[msg[i]] = 1
    else:
        d[msg[i]] += 1

s = ''

for i in d.keys():
    s += i + str(d[i])

print(s)
'''
import re


def replace(matchobj):
    return matchobj.groups()[1] + str(len(matchobj.groups()[0]))

string = input()
string = re.sub(r'((\w)\2*)', replace, string)
print(string)
