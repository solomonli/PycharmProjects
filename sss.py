"""def run_length_encode(string):
    res = ''

    for i in range(len(string)):
        if string[i] != string[i+1]:
            res += count_same(string[:i+1])
            string = string[i+1:]
            res += run_length_encode(string)
            break

    return res

def count_same(text):
    return str(len(text)) + text[0]

print(run_length_encode('AABBCCCDD'))
"""

def problem_1(lst):

    res = []

    for a, b in zip([*range(0, len(lst), 2)], [*range(-1, -len(lst), -2)]):
        res.append(lst[a])
        res.append(lst[b])

    return res

print(problem_1([1,2,3,4,5,6]))
