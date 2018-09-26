def date_fashion(you, date):
    """
    You and your date are trying to get a table at a restaurant.
    The parameter "you" is the stylishness of your clothes,
    in the range 0..10, and "date" is the stylishness of your date's clothes.
    The result getting the table is encoded as an int value with
    0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more,
    then the result is 2 (yes). With the exception that if
    either of you has style of 2 or less, then the result is 0 (no).
    Otherwise the result is 1 (maybe).

    date_fashion(5, 10) → 2
    date_fashion(5, 2) → 0
    date_fashion(5, 5) → 1

    :param you: int in range 0..10
    :param date: int
    :return: int 0, 1, 2
    """
    scale = list(range(11))
    high = scale[-2:]
    low = scale[:3]

    if you in low or date in low:
        return 0
    elif you in high or date in high:
        return 2
    else:
        return 1
