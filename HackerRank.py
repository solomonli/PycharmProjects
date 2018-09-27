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
#     arr = map(int, input().split())     # input e.g. '1 2 3 4 5' 
    arr = list(map(int, input().split()))   # risky to omit list()
    m = max(arr)    # max() doesn't work on map object, sum() does
  
    while max(arr) == m:
        arr.remove(m)
    
    print(max(arr))
    
    
Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]



