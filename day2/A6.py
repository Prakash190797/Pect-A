#------------Recursive Functions-------------
#A function that refers to itself is a recursive function

#function 3! = 3*2*1

def factorial(num):

    if num <= 1:
        return 1
    else:
        result = num * factorial(num - 1)
        return result
    
a = int(input("Enter a positive integer to find its factorial:"))
print(factorial(a))

#----------------Problem: Calculate Fibonacci Numbers------------
#To calculate Fibonacci numbers we sum the 2 previous 
#values to calculate the next item in the list like this 
#1,1,2,3,5,8 ...

def fib(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fib(n - 1) + fib(n - 2)
        return result

a = int(input("Enter a whole number:"))
print(fib(a))