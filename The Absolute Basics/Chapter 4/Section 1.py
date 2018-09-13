__author__ = 'phil'

# Create a variable with input()
guess = input("Guess my favourite number: ")
# Now some basic logic
if guess == "7":
    print("You got it!")

# Variable names changed slightly to allow them to all be in the same file
guess2 = input("Guess my favourite number: ")
# Same as before
if guess2 == "7":
    print("You got it!")
# Now add an else statement
else:
    print("Nope, that's not it!")

# Guessing one of two numbers now
guess3 = input("Guess one of my two favourite numbers: ")
# Making use of the 'or' keyword
if guess3 == "7" or guess3 == "3":
    print("You got it!")

# Guessing both now
guess41 = input("Guess my first favourite number: ")
guess42 = input("Guess my second favourite number: ")
# Making use of the 'and' keyword
if guess41 == "7" and guess42 == "3":
    print("You got it!")

# Telling the user if they are close
guess5 = input("Guess my favourite number: ")
if guess5 == "7":
    print("You got it!")
# Elif - a combination of else and if
elif guess5 == "6" or guess5 == "8":
    print("You're pretty close!")
else:
    print("Nope, that's not it!")

# Introducing while loops
guessed = 0
# Start of the while loop
while guessed == 0:
    guess6 = input("Guess my favourite number: ")
    if guess6 == "7":
        print("You got it!")
        # Breaking out of the while loop (stopping the cycle)
        guessed = 1
    else:
        print("Nope, that's not it!")

# Introducing for loops
print("You have 10 guesses - make them count!")
# Start of the for loop, and use of range()
for i in range(10):
    guess7 = input("Guess my favourite number: ")
    if guess7 == "7":
        print("You got it!")
    else:
        print("Nope, that's not it!")