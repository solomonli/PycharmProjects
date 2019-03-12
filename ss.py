def decode_count(string):
    """
    Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
    For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
    You can assume that the messages are decodable. For example, '001' is not allowed.
    :param string: a string of alpha letters
    :return: an integer
    """
    res = 0
    l = len(string)

    for i in range(l - 1):
        if string[i] > '2' or string[i] == '2' and string[i + 1] > '6':
            res -= 1

    res += l

    return res


print(decode_count('222222'))
# not recursive...

