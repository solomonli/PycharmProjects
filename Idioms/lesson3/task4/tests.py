from test_helper import run_common_tests, failed, passed, get_answer_placeholders
#from test_helper_4automation import check_placeholder
import sys
from test_helper import run_common_tests, failed, passed, get_answer_placeholders

# https://docs.python.org/3/library/tokenize.html
from tokenize import tokenize, untokenize, NUMBER, STRING, NAME, OP, TokenError
from io import BytesIO
from collections import Counter
import random

def get_tokens(code, filter_spaces=True, group_by_parentheses_one_level=True):
    try:
        g = tokenize(BytesIO(code.encode('utf-8')).readline)  # tokenize the string
        tokens = [tokval for toknum, tokval, _, _, _ in g][1:]
        # failed( tokens)
    except TokenError as e:
        failed("ERR %r <br>  in get_tokens(%r, ...)" %(e, code))
   
    
    
    if group_by_parentheses_one_level:
        def group_by_parentheses_one_level():
            start = None
            tokens_some_grouped = []
            for nr, t in enumerate(tokens):
                # print(nr, repr(t))
                if not t:
                    continue

                if t in "[({":
                    if len(tokens) > nr+1 and tokens[nr+1]  in "])}":  # if not just empty parentheses
                        tokens[nr] += tokens[nr+1]
                        t = tokens[nr]
                        del tokens[nr+1]
                    else:
                        start = nr

                if start is None:
                    tokens_some_grouped .append ( t )

                if t in "])}" and start != None:
                    if 'for' in tokens:  # don't group for list comprehensions
                        tokens_some_grouped.extend( tokens[start:nr+1] )
                    else:
                        tokens_some_grouped.append( ''.join(tokens[start:nr+1]).replace(',', ', '))  # todo: maybe 1) use untokenize
                    start = None
            return tokens_some_grouped
        tokens = group_by_parentheses_one_level()

    if filter_spaces:
        tokens = [t for t in tokens if t.strip()]
    return tokens


def hints_by_token_comparison(input, expected , limit_hints=2, **tokens_kwargs):
    """

    :param input:
    :param expected:
    :param limit_hints: max number of hints per category (missing/unnecessary)
    :return:
    """
    msgs = []
    a_tokens = get_tokens(input, **tokens_kwargs)
    b_tokens = get_tokens(expected, **tokens_kwargs)
    if a_tokens == b_tokens:
        msgs = [  "seems OK, maybe spacing is mangled.." ]

    else:
        a = Counter( a_tokens )
        b = Counter( b_tokens )
        if a == b:
            msgs =[ "Ordering is incorrect" ]

    unnecessary= a - b
    missing  = b - a

    if limit_hints:
        missing = list( missing.keys() )
        unnecessary = list( unnecessary.keys() )

        random.shuffle( missing )
        random.shuffle( unnecessary )

        missing = missing[:limit_hints]
        unnecessary = unnecessary[:limit_hints]

    msgs_more = messages_by_fragments(input, required=missing, unnecessary=unnecessary )
    return msgs + msgs_more

def code_highlight(txt):
    return "<span style='color:blue; font-family: monospace;'>%s</span>" % txt

def messages_by_fragments(placeholder, result=None, unnecessary=[], required=[]):
    
    msgs = []

    if result and  result in placeholder    and  len(placeholder) > len(result):
        msg = "Too much code in placeholder.."
        if placeholder.startswith(result):
            msg += " at the end..."
        if placeholder.endswith(result):
            msg += " at the beginning.."
        msgs.append( msg )

    if not isinstance(unnecessary, (list, tuple)):
        unnecessary = [unnecessary]
    if not isinstance(required, (list, tuple)):
        required = [required]

    for item in unnecessary:
        if item in placeholder:
            msgs .append( "some " +code_highlight(item) + " is not needed" )
    msgs.append("")
    for item in required:
        if not item in placeholder:
            msgs .append(  code_highlight(item) + " is expected "  )

    return msgs


def placeholder_smart_compare(placeholder, expected, human_nr=None, **hints_kwargs ):
    """Compares placeholder code with expected by tokens -- so spacing in expressions is ignored.
    Can have extra lists of `required` and `unnecessary` lists of strings"""
    tokens_kwargs = {} # possible use -- best would be to filter them from  **kwargs
    a_tokens = get_tokens(placeholder, **tokens_kwargs)
    b_tokens = get_tokens(expected, **tokens_kwargs)
    
    # if placeholder == expected:
    if a_tokens  == b_tokens:
        # failed( "DBG: "+"<br>"+str(a_tokens)+"<br>"+str(b_tokens) )
        passed()

    else:
        msgs = hints_by_token_comparison(placeholder, expected, **hints_kwargs)
        if human_nr:
            msgs.insert(0, "Placeholder nr. %s:" %(human_nr))
        failed( '<br />'.join(msgs) )




#### task:  sum
def test_answer_placeholders():
    placeholders = get_answer_placeholders()

    # placeholder tests
    placeholder_smart_compare(placeholders[0], """sum( finances )""", human_nr=1     )


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()       # TODO: uncomment test call

