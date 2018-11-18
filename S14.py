#Strings
print(type(3))
print(type(3.14))

print(type("3"))
print(type('3'))

samp_string = "This is a very important string"

print(samp_string[0])
print(samp_string[-1])
print(samp_string[3+5])

print("Length = ", len(samp_string))
print(samp_string[0:4])
print(samp_string[8:])
print(samp_string[:10])

print("Green" + "Eggs")
print("Hello" * 5)

#convert an int into a string
num_string = str(4)

#cycle through each char
for char in samp_string:
    print(char)

#cycling in pairs
for i in range(0,len(samp_string) - 1, 2):
    print(samp_string[i] + samp_string[i+1])

#you can get Unicode with order
print("A=", ord("A"))

#You can convert from unicode with chr
print("65=", chr(65))