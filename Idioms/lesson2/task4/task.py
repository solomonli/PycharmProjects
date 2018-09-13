# see http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#testing-for-truth-values

import random



data = random.choice( [  
            [10, 5, 3], 
            [],
            [1]
        ] )
print("data", data)


if len(data) > 0:
    print( "Average is", sum(data)/len(data) )
    
