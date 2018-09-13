print('Please enter four positive integers: ')
a = int(input())
b = int(input())
c = int(input())
d = int(input())

for row in range(a, b+1):
    for col in range(c, d+1):
        print(row*col)
    print()
# undone

'''
Write a program, which gets four numbers aa, bb, cc and dd as input, each on its own line. The program should output a fragment of multiplication table for all numbers of the interval [a;b][a;b] by all numbers of the interval [c;d][c;d].

Numbers aa, bb, cc and dd are natural ones and do not exceed 10, a≤ba≤b, c≤dc≤d.

Follow the output format from the example, use '\t' (tab character) to separate elements inside the line. Adding a space instead of line break is performed by the "end" parameter of the print function:

print(x, end=" ")
Please output the numbers from the specified intervals themselves in the left column and the top row (as headers).

Sample Input 1:
7
10
5
6
Sample Output 1:
	5	6
7	35	42
8	40	48
9	45	54
10	50	60
'''
