#-----------OOP'S------------
#Real world objects have attributes and capabilities
#A dog for example has the attribute of height, weight
#favourite food etc.

#it has capability to run, bark, scratch etc.

class Dog:

    def __init__(self, name = "", height= 0, weight= 0):

        #self allows you to refer to itself
        #it is like how you refer to yourself with my

        self.name = name
        self.height = height
        self.weight = weight
    def run(self):
        print("{} the dog runs".format(self.name))

    def eat(self):
        print("{} the dog eats".format(self.name))

    def bark(self):
        print("{} the dog barks".format(self.name))

def main():

    spot = Dog("Spot", 66, 26)
    spot.bark()
    
    bowser = Dog("bowser")
    bowser.eat()

main()

