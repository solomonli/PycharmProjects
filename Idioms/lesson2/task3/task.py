# see http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#testing-for-truth-values

import random



money = random.choice([100, -10, 0])
print('money', money)

if  money != 0:
    print("We have + or - (positive or negative amount of money)")


