from test_helper import failed, passed, get_answer_placeholders, \
    test_is_not_empty, test_answer_placeholders_text_deleted


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if "^$" in placeholder:
        passed()
    else:
        failed("Use '^$' to match empty string")


def test_answer_placeholders1():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if "views.post_list" in placeholder:
        passed()
    else:
        failed("Map url to the views.post_list")


if __name__ == '__main__':
    test_is_not_empty()
    test_answer_placeholders_text_deleted()
    test_answer_placeholders()
    test_answer_placeholders1()


