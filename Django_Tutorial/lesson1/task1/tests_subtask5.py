from test_helper import failed, passed, get_answer_placeholders, \
    test_is_not_empty, test_answer_placeholders_text_deleted


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if "order_by" in placeholder:
        passed()
    else:
        failed("Use order_by method")


def test_answer_placeholders1():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if "published_date" in placeholder:
        passed()
    else:
        failed("Order posts by published_date")


def test_answer_placeholders2():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    if "posts" in placeholder:
        passed()
    else:
        failed("Define posts variable")


def test_answer_placeholders3():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[1]
    if "posts" in placeholder:
        passed()
    else:
        failed("Pass posts variable to the template")


if __name__ == '__main__':
    test_is_not_empty()
    test_answer_placeholders_text_deleted()
    test_answer_placeholders()
    test_answer_placeholders1()
    test_answer_placeholders2()
    test_answer_placeholders3()


