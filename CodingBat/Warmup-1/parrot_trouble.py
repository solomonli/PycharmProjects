def parrot_trouble(talking, hour):
    """
    We have a loud talking parrot.
    We are in trouble if the parrot is talking and
    the hour is before 7 or after 20.
    Return True if we are in trouble.

    parrot_trouble(True, 6) → True
    parrot_trouble(True, 7) → False
    parrot_trouble(False, 6) → False

    :param talking: boolean
    :param hour: int, range 0..23
    :return: boolean
    """
    return talking and (hour < 7 or hour > 20)


print(parrot_trouble(True, 6))
print(parrot_trouble(True, 7))
print(parrot_trouble(False, 6))
