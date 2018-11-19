#Getters and Setters
#Getters and Setters are used to protect our objects
#from assigning bad fields or for providing improved
#output

class Square:

    def __init__(self, height = "0", width = "0"):

        self.height = height
        self.width = width

    @property
    def height(self):
        print("Retrieving the Height")

        return self.__height
    
    @height.setter
    def height(self, value):

        #we protect the height from receiving a bad value
        if value.isdigit():

            #Put a __ before this private field
            self.__height = value
        else:
            print("Please only enter numbers for height")

    #This is the getter
    @property
    def width(self):
        print("Retrieving the width")
        return self.__width 

    #This is the setter
    @width.setter
    def width(self,value):

        if value.isdigit():
            self.__width = value
        else:
            print("Please only enter numbers for width")
        
    def getArea(self):

        return int(self.__width)*int(self.__height)

def main():

    aSquare = Square()

    height = input("Enter height:")
    width = input("Enter width:")

    aSquare.height = height
    aSquare.width = width

    print("Height:", aSquare.height)
    print("Width:", aSquare.width)
    print("Area:", aSquare.getArea())

main()
