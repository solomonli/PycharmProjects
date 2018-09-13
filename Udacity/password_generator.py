import random

word_file = "words.txt"
word_list = []

with open(word_file, 'r') as words:
    for line in words:

        word = line.strip().lower()

        if 3 < len(word) < 8:
            word_list.append(word)


# def generate_password():
#     return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)


def generate_password():
    return str().join(random.sample(word_list, 3))


# def generate_password():
#     return ''.join(random.sample(word_list, 3))

print(generate_password())
