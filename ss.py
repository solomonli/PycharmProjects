def word_break(text, dictionary):
    """
    Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list.
    If there is more than one possible reconstruction, return any of them.
    If there is no possible reconstruction, then return null.

    For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox",
    you should return ['the', 'quick', 'brown', 'fox'].

    Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond",
    return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
    :param text: a string of letters, without space
    :param dictionary: a list of strings
    :return: a list of strings
    """
    # for element in lst:
    #     if element not in text:
    #         lst.remove(element)
    #
    # return lst
    res = []

    for i in range(1, len(text)):
        if text[:i] in dictionary:
           # res.append(text[:i])
           print(text[:i])
           sub_text = text[i+1:]

    return word_break(sub_text, dictionary)



print(word_break("bedbathandbeyond", ['bed', 'bath', 'bedbath', 'and', 'beyond']))




"""
table = {}

def wordBreak(s, dict):

    if len(s) == 0:

        return True

    if len(s) == 1:

        return s in dict

    if s in table:

        return list[s]

    isBreakable = False

    for i in range(len(s)):

        word = s[: i+1]

        if word in dict:

            subFlag = wordBreak(s[i + 1: ], dict)

        if s[i + 1: ] not in table:

            table[s[i + 1: ]] = subFlag

            isBreakable |= subFlag

    return isBreakable
"""