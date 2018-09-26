def make_out_word(out, word):
    """
    Given an "out" string length 4, such as "<<>>", and a word,
    return a new string where the word is in the middle of the out string,
     e.g. "<<word>>".

    make_out_word('<<>>', 'Yay') → '<<Yay>>'
    make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
    make_out_word('[[]]', 'word') → '[[word]]'

    :param out: str
    :param word: str
    :return: str
    """
    return out[:2] + word + out[2:]


print(make_out_word('<<>>', 'Yay'))
print(make_out_word('<<>>', 'WooHoo'))
print(make_out_word('[[]]', 'Word'))
