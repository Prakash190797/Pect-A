#program on birthday impotance according to age
age = eval(input("Enter age: "))
if(age>=1 and age<=18):
    print("Important")
elif(age==21 or age==50):
    print("Importantb birthday")
elif not(age<65):
    print("Important Birthday")
else:
    print("Not important")
    