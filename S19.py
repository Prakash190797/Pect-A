#Intro to functions
def add_numbers(num1, num2):
    return num1 + num2

print("5 + 4 =", add_numbers(5,4))

#function local variables
# Variables created in a function can't be accessed outside
# of it
def assign_name():
    name = "Doug"
assign_name()

# You can't change a global variable even if it is passed
# into a function
def change_name(name):
    name = "Mark"

name = "Tom"

change_name(name)
print(name)

# If you want to change the value pass it back
def change_name_2():
    return "Mark"
name = change_name_2()
print(name)

# You can also use the global statement to change it
gbl_name = "Sally"

def change_name_3():
    global gbl_name
    gbl_name = "Sammy"
change_name_3()
print(gbl_name)

#Returning None 
def get_sum(num1, num2):
    sum = num1 + num2

print(get_sum(5,4))

#problem: Solve for X
# Make a function that receives an algebraic equation like
# x + 4 = 9 and solve for x

def solve_eq(equation):
    x,add,num1,equal,num2 = equation.split()
    num1, num2 = int(num1), int(num2)

    return "x=" + str(num2 - num1)

print(solve_eq("X + 4 = 9"))

#Return multiple values

def mult_divide(num1, num2):

    return (num1 * num2),(num1 / num2)

mult,divide = mult_divide(5,4)

print("5 * 4 = ", mult)
print("5 / 4 = ", divide)

#Return a list of primes

def isprime(num):
    for i in range(2, num):
        if(num%i == 0 ):
            return False
    return True

def getPrimes(max_number):

    list_of_primes = []

    for num1 in range(2, max_number):

        if isprime(num1):
            list_of_primes.append(num1)
    return list_of_primes

max_num_to_check = int(input("Search for Primes Up to:"))

list_of_primes = getPrimes(max_num_to_check)

for prime in list_of_primes:
    print(prime)
    