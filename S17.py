#Problem: Acronym Generator
# You will enter a string and then convert it to an acronym
# with uppercase letters like this
'''
Convert to Acronym : Random Access Memory
RAM
'''

#Ask for a string
orig_string = input("Convert to Acronym:")

orig_string = orig_string.upper()

list_of_words = orig_string.split()

for word in list_of_words:
    print(word[0], end="")

print()

#More String Methods
# For our next problem some additional string methods are going to be
# very useful

letter_z = "z"
num_3 = "3"
a_space = ""

# Returns True if characters are letters or numbers
# Whitespace is false
print("Is z a letter or number:", letter_z.isalnum())

print("Is z a letter:", letter_z.isalpha())

# Returns True if characters are numbers (Floats are False)
print("Is 3 a number:", num_3.isdigit())

print("Is z a lowercase:", letter_z.islower())

print("Is z a uppercase:", letter_z.isupper())

print("Is space a space:", a_space.isspace())

