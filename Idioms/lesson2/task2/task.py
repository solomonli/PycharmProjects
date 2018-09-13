# see http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#testing-for-truth-values

import random



name = random.choice(["Tom", "", None])
print( name, repr(name) )

if name == "" or name == None:
    name = "Anonymous"

print("Hello, %s!" % name)


