def is_leap(year):
    """
    Wikipedia page was referred to

    :param year: int
    :return: boolean
    """
    if year % 4 != 0:
        leap = False

    elif year % 100 != 0:
        leap = True

    elif year % 400 != 0:
        leap = False

    else:
        leap = True
    
    return leap


if __name__ == '__main__':
    """
    input 5, output 12345. The quiz doesn't allow a string method.
    """
    n = int(input())
    string = ''
    
    for i in range(n):
        string += str(i+1)
        
    print(string)
    

if __name__ == '__main__':
    """
    List comprehension
    """
    x = y = z = 2
    n = 5	# those inputs are customizable
    
    print([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n])


if __name__ == '__main__':
    """ Print the runner-up score.

    Sample Input 
    5
    2 3 6 6 5
    
    Sample Output
    5
    """
    n = int(input())
#     arr = map(int, input().split())     # input e.g. '1 2 3 4 5' 

    arr = list(map(int, input().split()))   # risky to omit list()
    m = max(arr)    # max() doesn't work on map object, sum() does
  
    while max(arr) == m:
        arr.remove(m)
    
    print(max(arr))
    

if __name__ == '__main__':
    """
    Given the names and grades for each student in a Physics class of N students, 
    store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

    Note: If there are multiple students with the same grade, 
    order their names alphabetically and print each name on a new line.
    
    python students = [['Harry', 37.21], ['Berry', 37.21], 
                        ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    """
    name = []; score = []

    for _ in range(int(input())):

        #     name = input()
        #     score = float(input())
        # d[score] = name   # dict may not be a good idea because name/score (if as keys) may duplicate

        name.append(input())
        score.append(float(input()))

    lowest = min(score)
    score_2 = score.copy()

    while min(score_2) == lowest:
        score_2.remove(lowest)

    second_lowest = min(score_2)
    ss = [name[i] for i in range(len(name)) if score[i] == second_lowest]
    ss.sort()

    for i in ss:
        print(i)


if __name__ == '__main__':
    """
    You have a record of  students. Each record contains the student's name, 
    and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. 
    The user enters some integer  followed by the names and marks for  students. 
    You are required to save the record in a dictionary data type. The user then enters a student's name. 
    Output the average percentage marks obtained by that student, correct to two decimal places.
    """
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

