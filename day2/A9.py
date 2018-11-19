#-------------Tuples----------------
# A Tuple is like a list, but their values can't be changed
# Tuples are surrounded with parentheses instead of
# square brackets

myTuple = (1,2,3,4,5)

#Get a value with an index
print("1st value", myTuple[0])

#get a slice from the 1st index up to but not including
#the third

print(myTuple[0:3])

#Get the number of items in a Tuple
print("Tuple Length:", len(myTuple))

#Join or concatenate tuples
morefibs = myTuple + (13,21,34)
print(morefibs)

#check if a value is in a Tuple
print("Is 34 in Tuple:", 34 in morefibs)

#Iterate through a tuple
for i in morefibs:
    print(i)

#convert a list into a tuple
aList = [55,89,144]
aTuple = tuple(aList)

#convert a tuple into a list
aList = list(aTuple)

#get max and min value
print("Min:", min(aTuple))
print("Max:", max(aTuple))

