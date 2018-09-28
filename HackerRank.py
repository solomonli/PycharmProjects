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
    n = 5   # those inputs are customizable
    
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
    # arr = map(int, input().split())     # input e.g. '1 2 3 4 5'

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
    You have a record of students. Each record contains the student's name, 
    and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. 
    The user enters some integer followed by the names and marks for students. 
    You are required to save the record in a dictionary data type. The user then enters a student's name. 
    Output the average percentage marks obtained by that student, correct to two decimal places.
    sample inputs:
    3
    Krishna 67 68 69
    Arjun 70 98 63
    Malika 52 56 60
    Malika
    """
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    print('{.:2f}'.format(sum(student_marks[query_name]) / 3))


def minion_game(string):
    """
    Kevin and Stuart want to play the 'The Minion Game'.

    Game Rules

    Both players are given the same string S.
    Both players have to make substrings using the letters of the string S.
    Stuart has to make words starting with consonants.
    Kevin has to make words starting with vowels.
    The game ends when both players have made all possible substrings.

    Scoring
    A player gets +1 point for each occurrence of the substring in the string S.

    For Example:
    String  = BANANA
    Kevin's vowel beginning word = ANA
    Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

    Sample Input
    BANANA

    Sample Output
    Stuart 12

    :param string: str
    :return: str(space)int
    """
    def is_vowel(x):
        """input str (by default in lower case), output boolean"""
        return x in 'aeiou'

    string.lower()
    sl = list(string)
    # sl_bool = list(map(is_vowel, sl))

    word_list = []

    def collect_words(txt):
        for i in range(len(txt)):
            word_list.append(txt[:i + 1])
        return word_list

    word_bank = []

    for i in range(len(string)):
        if is_vowel(string[i]):
            word_bank.append(string[i:])

    sum(map(collect_words, word_bank))


s = input()
print(minion_game(s))


if __name__ == '__main__':
    """
    Sample Input
    12
    insert 0 5
    insert 1 10
    insert 0 6
    print
    remove 6
    append 9
    append 1
    sort
    print
    pop
    reverse
    print

    Sample Output
    [6, 5, 10]
    [1, 5, 9, 10]
    [9, 5, 1]
    """
    l = []
    N = int(input())
    for _ in range(N):
        cmd, *nums = input().split()

        if cmd == 'print':
            eval(cmd + '(l)')
        elif len(nums) == 2:
            eval('l.' + cmd + '(int(nums[0]), int(nums[1]))')
        elif len(nums) == 1:
            eval('l.' + cmd + '(int(nums[0]))')
        else:
            eval('l.' + cmd + '()')
