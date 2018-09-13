# List loops
finances = [10, -5, 15]



income = [100, 50, 777]
expenses = [90, 55, 762]

n = len( income )
for i in range(n):
    in_, out = income[i], expenses[i]
    print( "balance: ", in_-out ) 
