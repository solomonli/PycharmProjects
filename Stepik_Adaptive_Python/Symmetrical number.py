def make_four_digit(x):
    return "{:04d}".format(x)   # a string returned

print("Please enter an integer less than 100000: ", end='')
N = int(input())

print("Symmetrical? {}!".format(make_four_digit(N) == make_four_digit(N)[::-1]))
