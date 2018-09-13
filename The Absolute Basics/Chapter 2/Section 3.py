__author__ = 'phil'

added = 40 + 2
subtracted = 100 - 50.5
multiplied = 3.142 * 4.5
divided = 4 / 2

print(added, subtracted, multiplied, divided)

# Keep final value as an integer
divided_int = 4 // 2
print(divided_int)

# Modulo
divided_mod = 7 % 3
print(divided_mod)

# Building statements
print(4 * 86)
print(divided_int * added)
multiply_all = added * subtracted * multiplied * divided * divided_int * divided_mod
print(multiply_all)

# Chaining
chain_string = "chaining different types, even numbers like"
print("This is an example of", chain_string, added)