#Unknown number of arguments
# We can receive an unknown number of arguments using
# the splat (*) operator

def sumAll(*args):

    sum = 0

    for i in args:
        sum += i
    return sum

print("Sum:", sumAll(1,2,3,4))

#Our functions
import math
def get_area(shape):

    shape = shape.lower()

    if shape == "rectangle" :
        rectangle_area()
    elif shape == "circle":
        circle_area()
    else:
        print("Please enter rectangle or circle:")

def rectangle_area():

    length = float(input("enter the length:"))
    width = float(input("enter the breadth:"))

    area = length * width

    print("the area of the rectangle is:", area)

def circle_area():

    radius = float(input("enter the radius:"))

    area = math.pi * (math.pow(radius,2))

    print("Th area of circle is: {:.2f}".format(area))

def main():

    shape_type = input("get area for what shape:")

    get_area(shape_type)

main()