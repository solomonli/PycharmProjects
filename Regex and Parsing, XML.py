import re
print(*filter(None, re.split(r'[.,]+', input())), sep='\n')

# 100,000,000.000

"""
filter(function, iterable) is equivalent to the generator expression
 (item for item in iterable if function(item)) if function is not None and
  (item for item in iterable if item) if function is None.
"""