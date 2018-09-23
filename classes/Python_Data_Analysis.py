words = ['apple', 'adam', 'bat', 'beat', 'baton', 'cat']
by_letter = {}
for word in words:
	letter = word[0]
	by_letter.setdefault(letter, []).append(word)


from collections import defaultdict

by_letter = defaultdict(list)
for word in words:
	by_letter[word[0]].append(word)

print(by_letter)

counts = defaultdict(lambda: 4)
for i in counts:
	print(i)


import re


states = ['     Alabama', 'George!', 'george', 'FlOrIda',
          'south    carolina##', 'West virginia?']

def remove_punctuation(value):
	return re.sub('[!#?]', '', value)

clear_ops = [str.strip, remove_punctuation, str.title]

def clean_strings(strings, ops):
	result = []
	for value in strings:
		for function in ops:
			value = function(value)
		result.append(value)
	return result

print(clean_strings(states, clear_ops))
# print(map(remove_punctuation, states)) # won't work in Python3

x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = {**x, **y}
print(z)

print("Hello" "    World!")


def make_closure(a):
    def closure():
        print('I know the secret: {}'.format(a))
    return closure

closure = make_closure(5)
# <function make_closure.<locals>.closure at 0x10f7278c8>


def make_watcher():
    have_seen = {}
    def has_been_seen(x):
        if x in have_seen:
            return True
        else:
            have_seen[x] = True
            return False
    return has_been_seen


watcher = make_watcher()
vals = [5, 6, 1, 5, 1, 6, 3, 5]

print([watcher(x) for x in vals])
# [False, False, False, True, True, True, False, True]

def make_counter():
    count = [0]
    def counter():
    # increment and return the current count
        count[0] += 1
        return count[0]
    return counter

counter = make_counter()


def format_and_pad(template, space):
    def formatter(x):
        return (template % x).rjust(space)
    return formatter
fmt = format_and_pad('%.4f', 15)
print(fmt(1.756))
