#Make A isfloat Function
def isfloat(str_val):
    try:
        float(str_val)
        return True
    except ValueError:
        return False
    
pi = 3.14

print("Is pi a float:", isfloat(pi))

#Problem on Caesar's cipher
# Receive a message and then encrypt it by shifting the
# characters by a requested amount to the right
# A becomes D, B becomes E for example
# Also decrypt the message back again

message = input("Enter your message:")
key = int(input("How many characters to shift(1-26):"))

#Prepare your secret message
secret_message = ""

for char in message:
    if char.isalpha():
        char_code = ord(char)
        char_code += key
        if char.isupper():
            if char_code > ord('Z'):
                char_code -= 26
            elif char_code < ord('A'):
                char_code += 26
        else:
            if char_code > ord('z'):
                char_code -= 26
            elif char_code < ord('a'):
                char_code += 26
        
        secret_message += chr(char_code)
    
    else:

        secret_message +=  char

print("Encrypted:", secret_message)

key = -key
orig_message = ""

for char in secret_message:

    if char.isalpha():
        char_code = ord(char)
        char_code += key
        if char.isupper():
            if char_code > ord('Z'):
                char_code -= 26
            elif char_code < ord('A'):
                char_code += 26
        else:
            if char_code > ord('z'):
                char_code -= 26
            elif char_code < ord('a'):
                char_code += 26
        orig_message += chr(char_code)

    else:
        orig_message += char

print("Decrpyted message:", orig_message)
        