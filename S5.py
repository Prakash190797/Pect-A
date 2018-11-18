#program on Grade check according to age
age = eval(input("enter Age:"))

if(age<5):
    print("To Young for school")
elif(age==5):
    print("Go to kindergarden")
elif(age>=6 and age<=17):
    grade = age - 5
    print("Go to grade : {}".format(grade))
elif( age>17):
    print("Go to college")