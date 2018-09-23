def monkey_trouble(a_smile, b_smile):
    """
    We have two monkeys, a and b, and the parameters a_smile and b_smile
    indicate if each is smiling.
    We are in trouble if they are both smiling or if neither of them is smiling.
    Return True if we are in trouble.

    monkey_trouble(True, True) → True
    monkey_trouble(False, False) → True
    monkey_trouble(True, False) → False

    :param a_smile: boolean
    :param b_smile: boolean
    :return: boolean
    """
    return a_smile == b_smile


print(monkey_trouble(True, True))
print(monkey_trouble(False, False))
print(monkey_trouble(True, False))
print(monkey_trouble(False, True))
