def end_other(a, b):
    """
    Given two strings, return True if either of the strings appears
    at the very end of the other string, ignoring upper/lower case differences
    (in other words, the computation should not be "case sensitive").
    Note: s.lower() returns the lowercase version of a string.

    end_other('Hiabc', 'abc') → True
    end_other('AbC', 'HiaBc') → True
    end_other('abc', 'abXabc') → True

    :param a: str
    :param b: str
    :return: boolean
    """
    al = a.lower()
    bl = b.lower()

    return bl.endswith(al) or al.endswith(bl)
    # return al[-(len(b)):] == bl or al == bl[-(len(a)):]


print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))
