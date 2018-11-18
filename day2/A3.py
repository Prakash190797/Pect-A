#List Comprehensions 
#create a list of even values

import math
evenList = [i*2 for i in range(10)]

for k in evenList:
    print(k,end =" ")
print()

numList = [1,2,3,4,5]

listOfValues = [[math.pow(m,2), math.pow(m,3), math.pow(m,4)] for m in numList]

for k in listOfValues:
    print(k)
print()

#Intro to Multidimensional list
multiDList = [[0] * 10 for i in range(10)]

multiDList[0][1] = 10

#get the 2nd item in the 1st list
print(multiDList[0][1])

#get the 2nd item in 2nd list
print(multiDList[1][1])

#Multidimensional List

listTable = [[0] * 10 for i in range(10)]

for i in range(10):

    for j in range(10):

        listTable[i][j] = "{} : {}". format(i,j)

for i in range(10):

    for j in range(10):

        print(listTable[i][j], end = "||")
    print()

#Create a multiplication table

multTable = [[0] * 10 for i in range(10)]

for i in range(1,10):

    for j in range(1,10):

        multTable[i][j] = i * j

for i in range(1,10):

    for j in range(1,10):

        print(multTable[i][j], end = " ")

    print()