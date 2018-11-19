#...................Problem: Create a Customer List..............
# Create an array of customer dictionaries
# Output should look like this
'''
Enter Customer (Yes/No) : y
Enter Customer Name : Derek Banas
Enter Customer (Yes/No) : y
Enter Customer Name : Sally Smith
Enter Customer (Yes/No) : n
Derek Banas
Sally Smith
'''

customers = []

while True:

    createEntry = input("Enter Customer(Yes/No) :")
    createEntry = createEntry[0].lower()

    if createEntry == 'n':

        break

    else:

        fName,lName = input("Enter Customer Name: ").split()

        customers.append({"fName": fName, "lName": lName})

for cust in customers:
    print(cust['fName'], cust['lName'])

