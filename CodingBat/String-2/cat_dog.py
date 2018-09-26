def cat_dog(str):
    """
    Return True if the string "cat" and "dog" appear
    the same number of times in the given string.

    cat_dog('catdog') → True
    cat_dog('catcat') → False
    cat_dog('1cat1cadodog') → True

    :param str: str
    :return: boolean
    """
    count_cat = 0
    count_dog = 0

    for i in range(len(str) - 2):
        if str[i:i+3] == 'cat':
            count_cat += 1
        if str[i:i+3] == 'dog':
            count_dog += 1

    return count_cat == count_dog

#     return count_cat(str) == count_dog(str)
#
#
# def count_cat(str):
#
#     count = 0
#     for i in range(len(str) - 2):
#         if str[i:i+3] == 'cat':
#             count += 1
#     return count
#
#
# def count_dog(str):
#
#     count = 0
#     for i in range(len(str) - 2):
#         if str[i:i+3] == 'dog':
#             count += 1
#     return count


print(cat_dog('catdog'))
print(cat_dog('catcat'))
print(cat_dog('1cat1cadodog'))
