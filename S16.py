#String methods
rand_string = "this is an important string"

#delete  whitespace on left
rand_string = rand_string.lstrip()

#delete whitespace on right
rand_string = rand_string.rstrip()

#capitalize 1st letter
print(rand_string.capitalize())

#Capitalize every letter
print(rand_string.upper())

#lowercase all letters
print(rand_string.lower())

#turn a list into a string
a_list = ["Bunch", "of","random","words"]

print("".join(a_list))

#convert a string a list
a_list_2 = rand_string.split()

for i in a_list_2:
    print(i)

#count how many times a string occurs in a string
print("How many is: ", rand_string.count("is"))

#get the index of matching string
print("where is string:", rand_string.find("string"))

#replace a substring
print(rand_string.replace("an", "an kind of"))
