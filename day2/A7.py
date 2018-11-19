#--------------Files Operations-----------------
#We are able to store data for later use in files
#you can create or use an already created file with open

#if you use w(write) for mode the the file is overwritten.
#if you use a(append) you add to the end of the file

#text is stored using unicode where numbers represent all
#possible characters

#we start the code with 'with' which guarantees the file
#will be closed if the program crashes

import os
with open("mydata5.txt", mode = 'w', encoding= 'utf-8') as myFile:

    #you can write to the file with 'write'
    #it doesn't add a newline
    myFile.write("Some random text\n More random text\n and some more")

with open("mydata5.txt", encoding= "utf-8") as myFile:

    # We can read data in a few ways
    # 1. read() reads everything into 1 string
    # 2. readline() reads everything including the first newline
    # 3. readlines() returns a list of every line which includes
    # each newline

    print(myFile.read())

# Find out if the file is closed
print(myFile.closed)

#gives the name of the file
print(myFile.name)

#gives the mode of the file
print(myFile.mode)

os.rename("mydata5.txt", "mydata6.txt")

#delete a file
#os.remove("mydata3.dat")

#create directory
os.mkdir("mydir2")

#change directories
os.chdir("mydir2")

#display current directory
print("current Directory:", os.getcwd())

#remove a direcotry but 1st move back 1 directory
os.chdir("..")
os.rmdir("mydir2")

#Note: every time you have to change the file name

