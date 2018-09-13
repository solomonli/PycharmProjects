# Dictionary loops
prices = {'bread': 2, 'water':1, 'beer':2.5, 'apples':0.6 }

print( "goods:", list( prices.keys() ) )
average = sum(prices.values()) / len( prices)  
print( "average price:", average)

# simple loop
print("\n    Prices of Goods:")
for food in prices: 
    print( food, "costs", prices[food] ) 


# print only goods, which cost less than  average 
print("\n    Below average:")
for food in prices:
    if prices[food] < average:
        print( food, prices[food] )
   



