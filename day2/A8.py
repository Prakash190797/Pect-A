#-------------------Read one line at a Time-------------
#open the file

with open("mydata6.txt", encoding = "utf-8") as myFile:

    lineNum = 1

    #we'll use a while loop that loops until the data
    #read is empty

    while True:
        line = myFile.readline()

        #line is empty so exit
        if not line:
            break

        print("Line", lineNum, ":", line,end="")
        lineNum += 1

#-----------------Problem: Analyze the file------------
# As you cycle through each line output the number of
# words and average word length
'''
Line 1
Number of Words : 3
Avg Word Length : 4.7
Line 2
Number of Words : 3
Avg Word Length : 4.7
'''
with open("mydata6.txt", encoding = "utf-8") as myFile:

    lineNum = 1

    while True:

        line = myFile.readline()

        if not line:
            break
        print("\n Line", lineNum)

        wordList = line.split()

        print("Number of Words:", len(wordList))

        charCount = 0

        for word in wordList:

            for char in word:

                charCount += 1
            avgNumChars = charCount/len(wordList)

        print("Avg Word Length: {:.2f}".format(avgNumChars))

        lineNum += 1

