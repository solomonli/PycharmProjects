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


def fun(N):
    width = len(bin(N)) - 2
    for i in range(1, N+1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width = width))
n = int(input())
fun(n)
    
import string 
print(string.capwords(input(), ' '))
# "solomon 123abc leigh": 'a' won't be capitalized, not like title() does.

print(set('HackerRank'))
# {'r', 'k', 'R', 'e', 'n', 'a', 'c', 'H'}

print(set('10'))
# {'0', '1'}

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

list(enumerate(['R', 'a', 'n', 'k']))

s1 | s2; s1 & s2; s1 - s2; s1.difference(s2); s1 ^ s2; s1.symmetric_difference(s2)

"""
.update() or |= 
.intersection_update() or &=
.difference_update() or -=
.symmetric_difference_update() or ^=
"""

# 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 . Here 8 appears only once.
l = list(input().split())
d = {l.count(i) : i  for i in l}
print(d[1])

cycle = int(input())
for _ in range(cycle):
    setA = set(input().split())
    setB = set(input().split())
    print(setA < setB)

super = set(input().split())
print(all(super > set(input().split()) for _ in range(int(input()))))

"""
Sample Input
1+2j

Sample Output
2.23606797749979 
1.1071487177940904
"""
import cmath
z = complex(input())    # A polar coordinate (gamma, ps)
print(abs(z))   # gamma
print(cmath.phase(z))   # ps

pow(a, b, m)    # calculate x**y mod z

a, b, m = [int(input()) for _ in range(3)]
print(pow(a, b), pow(a, b, m), sep='\n')

"""
ord(c) given a string representing one Unicode character, return an integer 
representing the Unicode code point of that character. For example, ord('a') returns
 the integer 97 and ord('€') (Euro sign) returns 8364. This is the inverse of chr().
"""

a, b, c, d = [int(input()) for _ in range(4)]
print(a**b + c**d)

from itertools import product
A = [1, 2]
B = [3, 4]
print(product(A, B))        # <itertools.product object at 0x10c615558>
print(*product(A, B))       # (1, 3) (1, 4) (2, 3) (2, 4)

from itertools import permutations, combinations, combinations_with_replacement
# HACK 2
a, b = input().split()
print(*(''.join(i) for i in permutations(sorted(a), int(b))), sep='\n')
print(*(''.join(i) for i in combinations_with_replacement(sorted(a), int(b))), sep='\n')

# HACK 2
a, b = input().split()
print(*(''.join(j) for i in range(1, int(b)+1) for j in combinations(sorted(a), i)), sep='\n')

"""
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
"""
from collections import Counter

c = Counter(list(input().split()))
n = int(input())
revenue = 0

for i in range(n):
    size, price = input().split()
    if c[size]:     # the friendly Counter dict returns 0 given an unknown key
        c[size] -= 1
        revenue += int(price)

print(revenue)


"""
Sample Input
5 2
a
a
b
a
b
a
b

Sample Output
1 2 4
3 5
"""
from collections import defaultdict
d = defaultdict(list)
n, m = list(map(int, input().split()))
for i in range(n):
    d[input()].append(i + 1)        # defaultdict(list, {'a': [1, 2, 4], 'b': [3, 5]})
for _ in range(m):
    print(' '.join(map(str, d[input()])) or -1)


"""
5
ID         MARKS      NAME       CLASS     # The order of those columns is random but there must be a "MARKS"
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6 
"""
from collections import namedtuple
n = int(input())
Grade = namedtuple('Grade', input().split())    # Grade(MARKS='55', CLASS='8', NAME='Glenn', ID='4')
marks = [int(Grade._make(input().split()).MARKS) for _ in range(n)]
print(sum(marks) / len(marks))


"""
Sample Input
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30

Sample Output
BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
"""
from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    item, space, quantity = input().rpartition(' ')
    d[item] = d.get(item, 0) + int(quantity)
for item, quantity in d.items():
    print(item, quantity)


"""
Sample Input
6
append 1
append 2
append 3
appendleft 4
pop
popleft

Sample Output
1 2
"""
from collections import deque
# d = deque()
# for _ in range(int(input())):
#     cmd, *num = input().split()
#     if num:
#         eval('d.'+ cmd + '(int(num[0]))')
#     else:
#         eval('d.' + cmd + '()')

# for _ in range(int(input())):
#     exec('queue.{0}({1})'.format(*input().split()+['']))

for _ in range(int(input())):
    method, *num = input().split()
    getattr(d, method)(*num)
# getattr(x, 'foobar') is equivalent to x.foobar
# setattr(x, 'foobar', 123) is equivalent to x.foobar = 123
# delattr(x, 'foobar') is equivalent to del x.foobar
print(*d)


import calendar
print(calendar.TextCalendar(firstweekday=6).formatyear(2018))
print(calendar.weekday(2015, 10, 9))
mm, dd, yy = map(int, input().split())
print(calendar.day_name[calendar.weekday(yy, mm, dd)].upper())


for i in range(int(input())):
    try:
        a, b = map(int,input().split())
        print(a // b)
    except Exception as e:
        print("Error Code:", e)


import re
for _ in range(int(input())):
    ans = True
    try:
        reg = re.compile(input())
    except re.error:
        ans = False
    print(ans)

"""
has to pass float() but cannot be '12.'
"""
for _ in range(int(input())):
    ans = False
    s = input()
    try:
        num = float(s)
        ans = True
        num = int(s)
        ans = False
    except:
        pass
    print(ans)


"""
5 3     # subject as the row, student as the column
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5
"""
_, subject = map(int, input().split())
score = []
for _ in range(subject):
    score.append(map(float, input().split()))
for i in zip(*score):
    print(sum(i) / subject)


"""
Sample Input
1 4
x**3 + x**2 + x + 1

Sample Output
True
"""
x, ans = map(int, input().split())
print(eval(input()) == ans)


"""
input
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1   # sorted by the 2nd column (zero-based index)

output
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
"""
n, m = map(int, input().split())
rows = [input() for _ in range(n)]
# rows = list(input() for _ in range(n))
k = int(input())

print(*sorted(rows, key=lambda row: int(row.split()[k])), sep='\n')


"""
Sample Input
5
12 9 61 5 14

Sample Output
True

Explanation
Condition 1: All the integers in the list are positive.
Condition 2: Any of the integers is a palindromic integer.
"""

n, l = input(), list(input().split())
print(all(int(i) > 0 for i in l) and any(i == i[::-1] for i in l))


"""
A list on a single line containing the cubes of the first fibonacci numbers.

Sample Input
5

Sample Output
[0, 1, 1, 8, 27]
"""
n = int(input())

def fib(x):
    if x < 2:
        return x
    else:
        return fib(x-1) + fib(x-2)

cube = lambda x: x ** 3

print(list(map(cube, map(fib, list(range(1, n+1))))))

# fib = lambda y: y if y < 2 else fib(y - 1) + fib(y - 2)
# print(list(map(lambda x: x**3, map(fib, range(int(input()))))))


