__author__ = 'phil'

# Basic prompt
input("Prompt")

# Feeding the entered data from the prompt into a String variable
inputString = input("Enter something: ")
# Now output the String
print("You entered:", inputString)

# Assigning to a variable, and performing a calculation
mathsInt = (input("Enter an integer: ") / 2)

# Basic assigning
string = "I hate Python"
# Output the original
print(string)
# Replacing the contents of the string variable
string.replace("hate", "love")
# Output the new version
print(string)


# Basic assigning
phrase = "These are the strings you are looking for"
# Output the original
print(phrase)
# Replacing the contents
phrase.replace("the strings", "not the droids")
# Print the new version
print(phrase)

# Basic assigning
messyString = "tHis sTRinG is A MEss"
# Print the original
print(messyString)
# Change the case of messyString to Title Case, and assign it to titleString
titleString = messyString.title() # Remember that title() and other case changers often do not affect the original string
# Print out both messyString and titleString
print(messyString, titleString)
