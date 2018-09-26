def hell_name(name):
    """
    Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

    hello_name('Bob') → 'Hello Bob!'
    hello_name('Alice') → 'Hello Alice!'
    hello_name('X') → 'Hello X!'

    :param name: str
    :return: str
    """
    return 'Hello ' + name + '!'


print(hell_name('Bob'))
print(hell_name('Alice'))
print(hell_name('X'))
