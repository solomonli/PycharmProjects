print("The (integer) length of a chocolate bar: ", end='')
N = int(input())
print("The (integer) width of a chocolate bar: ", end='')
M = int(input())
print("The desired (integer) segments of the chocolate bar: ", end='')
K = int(input())

if K % M == 0 or K % N == 0:
    print("Misson possible!")
else:
    print("Mission impossible!")
