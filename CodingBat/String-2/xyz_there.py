def xyz_there(str):
    """
    Return True if the given string contains an appearance of "xyz" where
     the xyz is not directly preceeded by a period (.).
     So "xxyz" counts but "x.xyz" does not.

    xyz_there('abcxyz') → True
    xyz_there('abc.xyz') → False
    xyz_there('xyz.abc') → True

    :param str: str
    :return: boolean
    """
    if 'xyz' not in str:
        return False
    elif '.xyz' in str:
        return False
    elif 'xyz' in str:
        return True


print(xyz_there('abcxyz'))
print(xyz_there('abc.xyz'))
print(xyz_there('xyz.abc'))
print(xyz_there('abc.xyzxyz'))
