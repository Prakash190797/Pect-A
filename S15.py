#program on secret string
norm_string = input("Enter a string to hide in uppercase:")

secret_string = ""

#cycle through each char in string
for char in norm_string:
    secret_string += str(ord(char))

print("Secret Message:", secret_string)

norm_string = ""

#cycle through each char in string

for i in range(0, len(secret_string)- 1, 2):
    char_code = secret_string[i] + secret_string[i+1]
    norm_string += chr(int(char_code))

print("Original Message:", norm_string)    

#Important
# Make the above work with upper and lowercase with 1 addition and
# 1 subtraction
# Add these 2 changes
# secret_string += str(ord(char) - 23)
# norm_string += chr(int(char_code) + 23)
