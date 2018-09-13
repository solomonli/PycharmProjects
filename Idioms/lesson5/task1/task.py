# Dictionary loops
prices = {'bread': 2, 'water':1, 'beer':2.5, 'apples':0.6 }

print( "goods:", list( prices.keys() ) )

average = sum(prices.values()) / len( prices)  
print( "average price:", average)



# hint: https://www.tutorialspoint.com/python/dictionary_get.htm
import random
if random.choice([True, False]):  # to do or not to do ;)
    del prices['beer']

if 'beer' in prices:
    beer_price = prices['beer']
else:
    beer_price = None

print(beer_price)



