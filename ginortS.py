"""
A given string contains alphanumeric characters only.

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
"""
s = input()
sl = [i for i in list(s) if i.islower()]
su = [i for i in list(s) if i.isupper()]
s_number = [i for i in list(s) if i.isdigit()]
so = [i for i in s_number if int(i) % 2 != 0]   # int(i) will encounter a string input
se = [i for i in s_number if int(i) % 2 == 0]

print(''.join(sorted(sl) + sorted(su) + sorted(so) + sorted(se)))



theList = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468"
print(*sorted(input(), key=theList.index), sep="")


print(*(sorted(input(),
    key=lambda x: (x.isdigit(),
                   x.isdigit() and int(x) % 2 == 0,
                   x.isupper(), x.islower(), x))), sep='')
