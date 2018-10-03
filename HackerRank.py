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
    name, score = [], []

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
    vowels = 'AEIOU'
    stuart = kevin = 0
    l = len(string)

    for i in range(l):
        if string[i] in vowels:
            kevin += l - i
        else:
            stuart += l - i

    if stuart > kevin:
        print('Stuart ' + str(stuart))
    elif stuart == kevin:
        print('Draw')
    else:
        print('Kevin ' + str(kevin))


if __name__ == '__main__':
    s = input()
    minion_game(s)

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
    l, N = [], int(input())

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


def merge_the_tools(string, k):
    """
    Sample Input
    AABCAAADA
    3

    Sample Output
    AB
    CA
    AD

    :param string: str
    :param k: 3 lines of output, will be dividable by string length
    :return: substrings with unique values
    """
    # l, n = [], len(string)
    # hop = int(n / stride)
    #
    # for i in range(0, n, stride):
    #     l.append(string[i:i+stride])
    #
    # ll = []
    #
    # for item in l:
    #     ll.append(set(list(item)))
    #
    # # lll = []
    # # for item in ll:
    # #     lll.append(set(item))

# for i in range(0, len(string), k):
#     print(''.join(OrderedDict.fromkeys(string[i:i+k])))
#
# for i in range(0, len(string), k):
#     print(''.join(dict({string[i:i+k]:None})))

    import textwrap
    from collections import OrderedDict

    list1 = textwrap.wrap(string, k)
    # devides string into n equal parts of size k
    list2 = []

    for i in list1:
        # removes duplicate characters from string and append it to list 2
        list2.append(''.join(OrderedDict.fromkeys(i)))
        # has to be "OrderedDict.fromkeys", see "d = OrderedDict.fromkeys('abcaa')"

    for i in list2:
        print(i)


if __name__ == '__main__':
    string, stride = input(), int(input())
    merge_the_tools(string, k)

if __name__ == '__main__':
    """
    Sample Input
    2
    1 2
    
    Sample Output
    3713081631934410656
    """
    n = int(input())
    integer_list = list(map(int, input().split()))
    print(hash(tuple(integer_list)))


# print("Hello {} {}! You just delved into python.".format(a, b))

def mutate_string(string, position, character):
    """
    Sample Input
    abracadabra
    5 k

    Sample Output
    abrackdabra
    """
    return string[:position] + character + string[position+1:]


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

if __name__ == '__main__':
    s = input()
    print(any(i for i in s if i.isalnum()))
    print(any(i for i in s if i.isalpha()))
    print(any(i for i in s if i.isdigit()))
    print(any(i for i in s if i.islower()))
    print(any(i for i in s if i.isupper()))
 
thickness = 5 #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

def wrap(string, max_width):
    l = ' '.join(textwrap.wrap(string, max_width))
    string_linebreak = textwrap.fill(l, max_width)
    return string_linebreak

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    
n, m = map(int, input().split())    # input "9 27"
pattern = [('.|.' * (2 * i + 1)).center(m, '-') for i in range(n // 2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))

n = int(input())
w = len("{0:b}".format(n))
for i in range(1, n+1):
    print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=w))
    
import string 
print(string.capwords(input(), ' '))
# "solomon 123abc leigh": 'a' won't be capitalized, not like title() does.

print(set('HackerRank'))
# {'r', 'k', 'R', 'e', 'n', 'a', 'c', 'H'}

print(set([1,2,1,2,3,4,5,6,0,9,12,22,3]))
# {0, 1, 2, 3, 4, 5, 6, 9, 12, 22}

print(set((1,2,3,4,5,5)))
# {1, 2, 3, 4, 5}

print(set['H','a','c','k','e','r','r','a','n','k']))
# {'r', 'k', 'e', 'n', 'a', 'c', 'H'}

print(set({'Hacker': 'DOSHI', 'Rank': 616}))
# {'c', 'r', 'n', 'e', 'k', 'a', 'H'}

print(set(enumerate(['H','a','c','k','e','r','r','a','n','k'])))
# {(1, 'a'), (7, 'a'), (9, 'k'), (8, 'n'), (6, 'r'), (3, 'k'), (2, 'c'), (0, 'H'), (4, 'e'), (5, 'r')}

my_set = {'a', 'c', 'b'}
my_set.add((5, 4))
my_set.update([1, 2, 3, 4])
my_set.update({1, 7, 8})
my_set.discard(7); my_set.discard(8)

set1 = set(list(map(int, input().split())))
set2 = set(list(map(int, input().split())))
# ss = set1.symmetric_difference(set2)      same thing to '^'
ss = set1 ^ set2
print('\n'.join(map(str, sorted(ss))))

"""
Sample Input
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5

Sample Output
4
"""
_ = int(input())
s = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    cmd, *num = input().split()
    if cmd == 'pop':
        eval('s.' + cmd + '()')
    else:
        eval('s.' + cmd + '(int(num[0]))')
print(sum(s))

