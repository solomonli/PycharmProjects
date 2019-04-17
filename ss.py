# from decorators import timer, debug, job_schedule

def query_string(string, target):
    """
    Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
    return all strings in the set that have s as a prefix.
    For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
    Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
    :param string: str (e.g. 'de')
    :param target: list of strings (e.g. [dog, deer, deal])
    :return: list of strings
    """
    return list(filter(lambda x: x.startswith(string), target))


print(query_string('de', ['dog', 'deer', 'deal']))
