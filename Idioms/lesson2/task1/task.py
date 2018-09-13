# see http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#testing-for-truth-values

import random



has_money = random.choice([False, True])
print('has_money', has_money)

if has_money == True:
    print("Nice guy..")
else:  # if not has_money
    print("Poor guy..")


