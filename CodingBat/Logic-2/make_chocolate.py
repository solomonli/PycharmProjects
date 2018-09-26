def make_chocolate(small, big, goal):
    """
    We want make a package of goal kilos of chocolate.
    We have small bars (1 kilo each) and big bars (5 kilos each).
    Return the number of small bars to use, assuming we always use big bars before small bars.
    Return -1 if it can't be done.

    make_chocolate(4, 1, 9) → 4
    make_chocolate(4, 1, 10) → -1
    make_chocolate(4, 1, 7) → 2

    :param small: int
    :param big: int
    :param goal: int
    :return: int
    """

    if small + big * 5 < goal:  # overall there are no adequate bar units
        return -1

    elif small < goal % 5:  # (6,2,7) after using 1 big bar, there should be enough small bars
        return -1

    else:
        x, y = divmod(goal, 5)
        return goal - min(x, big) * 5   # (6,1,10) you have limited big bars


print(make_chocolate(4, 1, 9))
print(make_chocolate(4, 1, 10))
print(make_chocolate(4, 1, 7))
