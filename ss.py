from decorators import perf_timer


@perf_timer
def LCSmemo(s1, s2, i1, i2):
    """
    find the Longest Common Sequence between two strings
    :param s1: str
    :param s2: str
    :param i1: int, the position pointer
    :param i2: int, the position pointer
    :param memo: a list of lists of None to memory the results
    :return: the LCS str
    """
    memo = [[None] * len(s2) for _ in range(len(s1))]       # cool trick!

    return helper(s1, s2, i1, i2, memo)


def helper(s1, s2, i1, i2, memo):

    if i1 == len(s1) or i2 == len(s2):
        return ''

    if memo[i1][i2] is not None:
        return memo[i1][i2]

    if s1[i1] == s2[i2]:
        memo[i1][i2] = s1[i1] + helper(s1, s2, i1+1, i2+1, memo)
        return memo[i1][i2]
    else:
        memo[i1][i2] = max(helper(s1, s2, i1, i2+1, memo), helper(s1, s2, i1+1, i2, memo))
        return memo[i1][i2]


print(LCSmemo('Jeez, I am waiting for snow.', "Jeez, I've been waiting for snow.", 0, 0))
