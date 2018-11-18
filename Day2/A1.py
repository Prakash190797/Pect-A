#Logic behind lists
import random 
import math

randList = ["string", 1.234, 28]

oneToTen = list(range(10))

#combine lists
randList = randList +oneToTen

#Get first item with index
print(randList[0])

print("List length:", len(randList))

#Slice a list to get 1st 3 items
first3 = randList[0:3]

for i in first3:
    print("{} : {}".format(first3.index(i),i))

#item repeat
print(first3[0] * 3)

#check if list has that item 
print("string" in first3)

#get index of matching item
print("Index of string:", first3.index("string"))

#no. of times item is in list
print("How many string:", first3.count("string"))

#change a list item
first3[0] = "New string"

for i in first3:
    print("{} : {}".format(first3.index(i),i))

first3.append("Another")

#create a randomlist
#generate a random list of 5 values betwwen 1 and 9
numList = []
for i in range(5):
    numList.append(random.randrange(1,9))

print(numList)