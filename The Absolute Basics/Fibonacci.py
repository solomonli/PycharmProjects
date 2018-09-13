def Fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return Fib(x-1) + Fib(x-2)


print(Fib(0))
print(Fib(1))

FibValue_Cap = int(input('How many Fibonacci values would you like to have: '))

for i in range(FibValue_Cap):
    print(Fib(i+1))

print('All done')
