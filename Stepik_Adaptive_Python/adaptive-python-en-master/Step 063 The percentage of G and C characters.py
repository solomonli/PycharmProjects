import re

string = input()

f = re.findall(r'c|g', string, re.IGNORECASE)
# letter c or g, case ignored

print(100 * len(f) / len(string))
