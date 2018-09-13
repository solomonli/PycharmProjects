# sequence = [30, 32, 43, 65, -32, 0, 54, 34, -23, 11, 9]
# n = 11
# sequence = [30, 32, 43, 65, -32, 54, 34, -23, 11, 9]
# n = 10


n, *sequence = map(int, input().split())
answer = [sequence[i] + sequence[-1-i] for i in range(n // 2)]
if n % 2 == 1:
    answer.append(sequence[n // 2])
print(*answer)

# int(str(5/2)) will give you that specific error
'''
Write a program, which turns a sequence of integers x1,x2,…,xn
into the sequence (x1+xn),(x2+xn−1),(x3+xn−2),…(x1+xn),(x2+xn−1),(x3+xn−2),… of length ⌈n/2⌉.

Input format: input is a positive integer n<10^6, next go the n integers separated by spaces, 
corresponding to x1,…,xnx1,…,xn.

Output format: the output should be the ⌈n/2⌉ space-separated integers, 
corresponding to the sequence (x1+xn),(x2+xn−1),(x3+xn−2),… 
In the case if number n is an odd one, x (n+1)/2 (i.e. the middle number in the array) 
should serve as the last element of the sequence.

Sample Input:
10 30 32 43 65 -32 54 34 -23 11 9
Sample Output:
39 43 20 99 22 
'''
