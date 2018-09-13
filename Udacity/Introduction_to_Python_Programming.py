print("{1} {0}".format(111, 222))
print("{} and {:08.2f}".format("a", 3))
print("{:.5f}".format(1 / 10))
print("{:.55f}".format(1 / 10))
print(sum({-10: 'x', -20: 'y', -30: 'z'}))
print(sum({-10: 10, -20: 20, -30: 30}))
print(sum({-10: 'x', -20: 'y', -30: 'z'}, 100))

lst = []
for letter in 'shark':
    lst.append(letter)
print(lst)

new_lst = [l for l in lst if l <= 'r']
print(new_lst)  # l for l in xxx

number_list = [x ** 2 for x in range(10) if x % 2 == 0]
print(number_list)

ll = [x for x in range(100) if x % 3 == 0 if x % 7 == 0]
print(ll)  # 'and' was not used

lll = [x * y for x in [2, 3, 4] for y in [12, 24, 36]]
print(lll)  # two 'for' was used

German = "Ä Ö Ü ä ö ü ß"
G1 = German.casefold(); G2 = German.lower()
print(G1); print(G2)

print('\n'.join(['I', 'am', 'bored']))  # a string joins a list


def starbox(width, height):
    """print a box made up of asterisks.

    width: width of box in characters, must be at least 2
    height: height of box in lines, must be at least 2
    """
    print("*" * width)  # print top edge of box

    # print sides of box
    for _ in range(height - 2):
        print("*" + " " * (width - 2) + "*")

    print("*" * width)  # print bottom edge of box


print("Test 1:")
starbox(5, 5)

print("Test 2:")
starbox(2, 3)

card_deck = [4, 11, 8, 5, 13, 2, 8, 10, 13, 7, 9]
hand = []
while sum(hand) <= 51:
    hand.append(card_deck.pop())
print(hand)  # pop removes the last element from a list and returns it

# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
rainfall *= .9

# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall

# increase reservoir_volume by 5% to account for stormwater that flows into the reservoir in the days following the storm
reservoir_volume *= 1.05

# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume *= 0.95

# subtract 2.5e5 cubic metres from reservoir_volume to account for water that's piped to arid regions.
reservoir_volume -= 2.5e5

# print the new value of the reservoir_volume variable
print(reservoir_volume)

prophecy = "And there shall in that time be rumours of things going astray, and there will be a great confusion as to where things really are, and nobody will really know where lieth those little things with the sort of raffia work base, that has an attachment…at this time, a friend shall lose his friends’s hammer and the young shall not know where lieth the things possessed by their fathers that their fathers put there only just the night before around eight o’clock…"

vowel_count = 0
lower_prophecy = prophecy.lower()
vowel_count += lower_prophecy.count('a')
vowel_count += lower_prophecy.count('e')
vowel_count += lower_prophecy.count('i')
vowel_count += lower_prophecy.count('o')
vowel_count += lower_prophecy.count('u')
print(vowel_count)

city = "Seoul"
high_temperature = 18
low_temperature = 9
temperature_unit = "degrees Celsius"
weather_conditions = "light rain"

alert = "Today's forecast for {}: The temperature will range from {} to {} {}. Conditions will be {}.".format(city,
                                                                                                              low_temperature,
                                                                                                              high_temperature,
                                                                                                              temperature_unit,
                                                                                                              weather_conditions)
print(alert)


def readable_timedelta(days):
    '''
    turn days into weeks and days
    '''
    return "{} week(s) and {} day(s)".format(days // 7, days % 7)


weight_in_kg = 75;
height_in_m = 1.78
if 18.5 <= weight_in_kg / height_in_m ** 2 < 25:  # test if it's in a range
    print("BMI is considered 'normal'.")


def cylinder_surface_area(radius, height, has_top_and_bottom):
    side_area = height * 6.28 * radius
    top_area = 3.14 * radius ** 2

    if has_top_and_bottom:
        return side_area + top_area * 2
    else:
        return side_area


def which_prize2(points):
    prize = None
    if points <= 50:
        prize = "a wooden rabbit"
    elif 150 <= points <= 180:
        prize = "a wafer-thin mint"
    elif points >= 181:
        prize = "a penguin"
    if prize:
        return "Congratulations! You have won " + prize + "!"
    else:
        return "Oh dear, no prize this time."


def top_three(input_list):
    return sorted(input_list, reverse=True)[:3]
    # the list's length won't fail the [:3] slicing


# for the iterable in a loop, you can use 'element', 'token', or 'item'


names = ['charlotte hippopotamus turner', 'oliver st. john-mollusc', 'nigel incubator-jones',
         'philip diplodocus mallory']
# create a new list of capitalized names without modifying the original list
capitalized_names = []  # create a new, empty list
for name in names:
    capitalized_names.append(name.title())  # add elements to the new list

# modify the names list in place
for index in range(len(names)):  # iterate over the index numbers of the names list
    names[index] = names[index].title()  # modify each element of names


def html_list(list_items):
    ul = "<ul>\n"
    for item in list_items:
        ul += "<li>{}</li>\n".format(item)
    ul += "</ul>"
    return ul


print(html_list(['first string', 'second string']))


def nearest_square1(limit):
    answer = 0
    while (answer + 1) ** 2 < limit:
        answer += 1
    return answer ** 2


import math


def nearest_square2(num):
    return round(math.sqrt(num)) ** 2


def nearest_square3(num):
    return math.floor(math.sqrt(num)) ** 2


print(nearest_square1(48))
print(nearest_square2(48))  # here 48 doesn't mean the limit
print(nearest_square3(48))

manifest = [["bananas", 15], ["mattresses", 34], ["dog kennels", 42], ["machine that goes ping!", 120],
            ["tea chests", 10], ["cheeses", 0]]
cargo_hold = []
cargo_weight = 0

for cargo in manifest:
    if cargo_weight + cargo[1] >= 100:
        break
    else:
        cargo_hold.append(cargo[0])
        cargo_weight += cargo[1]
print(cargo_hold)

headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]
news_ticker = ''
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break  # this code is so beautiful!!!
print(news_ticker)


def check_answer(my_answer, answer):
    return bool(my_answer == answer)


def check_answers(my_answers, answers):
    # Checks the five answers provided to a multiple choice quiz and returns the results.
    results = []
    for i in range(len(my_answers)):
        results.append(check_answer(my_answers[i], answers[i]))
    count_correct = 0

    for result in results:
        if result:
            count_correct += 1

    if count_correct / len(results) > 0.7:
        return "Congratulations, you passed the test!"
    elif (len(results) - count_correct) / len(results) >= 0.3:
        return "Unfortunately, you did not pass."


def remove_duplicates1(items):
    set_items = set(items)
    return list(set_items)


def remove_duplicates2(source):
    target = []

    for element in source:
        if element not in target:
            target.append(element)
    return target


squares = set()
n = 1
while n ** 2 < 2000:
    squares.add(n ** 2)
    n += 1
print(squares)

population = {'Shanghai': 17.8, 'Istanbul': 13.3,
            'Karachi': 13.0, 'Mumbai': 12.5}
# Dictionary keys must be immutable, but keys can be added naturally
population['Beijing'] = 20.1

Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963,
                       "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
                       "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
                       "Sgt. Pepper's Lonely Hearts Club Band": 1967,
                       "Magical Mystery Tour": 1967, "The Beatles": 1968,
                       "Yellow Submarine": 1969, 'Abbey Road': 1969,
                       "Let It Be": 1970}

for album_title in Beatles_Discography:
    print("title: {}, year: {}".format(album_title, Beatles_Discography[album_title]))

import collections


def most_prolific(dct):
    c = collections.Counter(dct.values())
    # return c
    return max(sorted(c.keys()), key=lambda y: c[y])
    # I don't understand this lambda function...


print(most_prolific(Beatles_Discography))

elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True

print(elements['hydrogen']['is_noble_gas'])
print(elements['helium']['is_noble_gas'])

monthly_takings = {'January': [54, 63], 'February': [64, 60], 'March': [63, 49],
                   'April': [57, 42], 'May': [55, 37], 'June': [34, 32],
                   'July': [69, 41, 32], 'August': [40, 61, 40], 'September': [51, 62],
                   'October': [34, 58, 45], 'November': [67, 44], 'December': [41, 58]}


def total_takings1(yearly_record):
    lst = []
    for month in yearly_record.keys():
        for item in yearly_record[month]:
            lst.append(item)
    return sum(lst)


def total_takings2(yearly_record):
    total = 0
    for month in yearly_record.keys():
        total += sum(yearly_record[month])
    return total


print(total_takings1(monthly_takings))
print(total_takings2(monthly_takings))


def hours2days(hr):
    return hr // 24, hr % 24

print(hours2days(10000))

dimensions = 52, 40, 100  # tuple unpacking!
print(type(dimensions))


def print_list(l, numbered=False, bullet_character='-'):
    for index, element in enumerate(l):
        if numbered:
            print("{}: {}".format(index + 1, element))
        else:
            print("{} {}".format(bullet_character, element))


print_list(["cats", "in", "space"])
print_list(["cats", "in", "space"], True)

import math

print(math.exp(3))

import datetime
import os.path
import csv
import zipfile
import timeit

# In Python, the break statement provides you with the opportunity to exit out of a loop
# when an external condition is triggered.
# (usually after an if)

# The continue statement gives you the option to skip over the part of a loop
# where an external condition is triggered,
# but to go on to complete the rest of the loop.
# That is, the current iteration of the loop will be disrupted,
# but the program will return to the top of the loop.
# (usually after an if)

# When an external condition is triggered, the pass statement allows you to handle the condition
# without the loop being impacted in any way; all of the code will continue to be read
# unless a break or other statement occurs.
# (usually after an if)

# In Python, '__main__' is the name of the scope where top-level code will execute.
# When a program is run from standard input, a script, or from an interactive prompt,
# its __name__ is set equal to '__main__'.


def multiply(*args):
    z = 1
    for num in args:
        z *= num
    print(z)

multiply(4, 5)
multiply(10, 9)
multiply(2, 3, 4)


def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(kwargs_1="Shark", kwargs_2=4.5, kwargs_3=True)


def print_values(**kwargs):
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))

print_values(
            name_1="Alex",
            name_2="Gray",
            name_3="Harper",
            name_4="Phoenix",
            name_5="Remy",
            name_6="Val"
        )

# When ordering arguments within a function or function call, arguments need to occur in a particular order:

# 1. Formal positional arguments
# 2. *args
# 3. Keyword arguments
# 4. **kwargs

def example1(arg_1, arg_2, *args, **kwargs):
def example2(arg_1, arg_2, *args, kw_1="shark", kw_2="blobfish", **kwargs):

def some_args(arg_1, arg_2, arg_3):
    print("arg_1:", arg_1)
    print("arg_2:", arg_2)
    print("arg_3:", arg_3)

args = ("Sammy", "Casey", "Alex")
some_args(*args)


def some_args(arg_1, arg_2, arg_3):
    print("arg_1:", arg_1)
    print("arg_2:", arg_2)
    print("arg_3:", arg_3)

my_list = [2, 3]
some_args(1, *my_list)


def some_kwargs(kwarg_1, kwarg_2, kwarg_3):
    print("kwarg_1:", kwarg_1)
    print("kwarg_2:", kwarg_2)
    print("kwarg_3:", kwarg_3)

kwargs = {"kwarg_1": "Val", "kwarg_2": "Harper", "kwarg_3": "Remy"}
some_kwargs(**kwargs)
