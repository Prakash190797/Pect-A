#Dictionaries
# Dictionaries instead use key / value pairs.

#create a dictionary abou me
derekDict = {"fName":"Derek", "lName":"Banas", "address":"123 Main St."}

#Get a value with a key
print("My Name:", derekDict["fName"])

#Change a value with the key
derekDict["address"] = "215 North Sr"

#Dictionaries may not print out in the order created
#since they are not ordered
print(derekDict)

#Add a new key value
derekDict['city'] = 'Pitsburgh'

#check if a key exists
print("Is there a city:","city" in derekDict)

#get the list of values
print(derekDict.values())

#get the list of keys 
print(derekDict.keys)

#get the key and value with items()
for k,v in derekDict.items():
    print(k,v)

#get gets a value associated with a key or the default
print(derekDict.get("mName", "Not here"))

#delete a key value
del derekDict["fName"]

#Loop through the dictionary keys
for i in derekDict:
    print(i)

#Delete all entries
derekDict.clear()

#List for holding Dictionaries
employees = []

#input employee data
fName,lName = input("Enter employee Name:").split()

employees.append({"fName": fName, "lName": lName})

print(employees)

