def is_leap(year):
    leap = False
    
    if year % 4 != 0:
        leap = False

    elif year % 100 != 0:
        leap = True

    elif year % 400 != 0:
        leap = False

    else:
          leap = True
    
return leap
Wikipedia page was referred to.

Input 5, output 12345. Cannot use a string method.
if __name__ == '__main__':
    n = int(input())
    string = ''
    
    for i in range(n):
        string += str(i+1)
        
    print(string)
    

List comprehension
if __name__ == '__main__':
    x = y = z = 2
    n = 5	those inputs are customizable
    
print([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n])

Print the runner-up score.

Sample Input 
5
2 3 6 6 5

Sample Output
5

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())     # input e.g. '1 2 3 4 5'      # map return a map object
    
