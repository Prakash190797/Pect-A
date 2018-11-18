#Force user to enter a number
while True:
    try:
        nuber = int(input("Ënter a Number:"))
        break
    except ValueError:
        print("You didn't enter a number")
    except:
        print("An unknown error  occurred")
print("Thank you for entering a number")

#Implement a Do while Loop
#Guess a number

secret_number=7

while True:
    guess = int(input("Guess a number between 1 and 10:"))

    if guess == secret_number:
        print("You guessed it")
        break
