import re
print(*filter(None, re.split(r'[.,]+', input())), sep='\n')

# 100,000,000.000
