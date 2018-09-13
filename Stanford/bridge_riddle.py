def f(s):
    s.sort()                                        # sort input in place
    if len(s) > 3:                                  # loop until len(s) < 3
        a = s[0] + s[-1] + min(2*s[1], s[0]+s[-2])  # minimum time according to xnor paper
        return a + f(s[:-2])                        # recursion on remaining people
    else:
        return sum(s[len(s) == 2:])                 # add last times when len(s) <= 3


'''fuck, this line is genius! False means 0!!!'''


if __name__ == '__main__':
    print(f([1]))
