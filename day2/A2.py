#Sort a List: Bubble Sort
# Create the value that will decrement for the outer loop
# Its value is the last index in the list

import random

numList = []
for i in range(5):
    
    numList.append(random.randrange(1, 9))

i = len(numList) - 1

while i > 1 :
    j=0
    while j < i :

        print("\nIs {} > {}".format(numList[j],numList[j + 1]))
        print()

        if numList[j] > numList[j+1] :
            print("Switch")

            temp = numList[j]
            numList[j] = numList[j + 1]
            numList[j + 1] =temp

        else:
            print("Don't Switch")
        j += 1

        for k in numList:
            print(k, end=",")
        print()
    print("End of round")

    i -= 1
for k in numList:
    print(k,end = " ")
print()

#More list Functions

numList = []
for i in range(5):
    
    numList.append(random.randrange(1, 9))

#Sort a list
numList.sort()

#reverse a list
numList.reverse()

for k in numList:
    print(k, end = " ")
print()

#insert value at index insert(index,value)
numList.insert(5,10)

#delete first occurrence of value
numList.remove(10)

for k in numList:
    print(k, end = " ")
print()

#remove item at index
numList.pop(2)

for k in numList:
    print(k, end=" ")
print()

