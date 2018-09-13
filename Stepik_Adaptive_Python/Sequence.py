sqc = ''
print("Please tell me how many numbers you would like to see: ", end='')
N = int(input())

i = 1
while len(sqc) <= N:
    sqc += str(i)*i
    i += 1

print(' '.join(sqc[:N]))
