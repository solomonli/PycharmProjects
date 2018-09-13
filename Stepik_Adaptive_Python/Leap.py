print("Please enter a year: ", end='')
Y = int(input())

if Y % 4 == 0 and Y % 100 != 0 or Y % 400 == 0:
    print("Leap")
else:
    print("Regular")

'''
n = int(input())
print('Leap' if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0) else 'Regular')
'''
