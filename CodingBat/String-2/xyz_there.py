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
        # remove '.xyz' then find if there's a 'xyz' left
        str2 = str.replace('.xyz', '')
        if 'xyz' in str2:
            return True
        else:
            return False
    else:
        return True


print(xyz_there('abcxyz'))
print(xyz_there('abc.xyz'))
print(xyz_there('xyz.abc'))
print(xyz_there('abc.xyzxyz'))
