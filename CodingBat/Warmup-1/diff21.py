def diff21(n):
    """
    Given an int n, return the absolute difference between n and 21,
    except return double the absolute difference if n is over 21.

    diff21(19) → 2
    diff21(10) → 11
    diff21(21) → 0
    """
    distance = abs(n - 21)
    
    if n > 21:
        distance *= 2

    return distance


print(diff21(19))
print(diff21(10))
print(diff21(21))
