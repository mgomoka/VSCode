""" Creates New Class 'Person' With Name Attribute
class Person:
    def __init__(self, name):
        self.name = name
"""

# from tkinter.constants import S



def person_init(self, name, age):
    self.name = name
    self.age = age

def say_name(self):
    print(self.name)
def say_age(self):
    print(str(self.age))

new_class = type("Person", (), {"__init__": person_init, "say_name": say_name, "say_age": say_age})
print("\n" + str(new_class.__name__) + "\n" + "\n" + "\n")

x = new_class("Tim", 28)
print(x.name)
x.say_name()
x.say_age()

# Create New Type Class To Modify And Use To Create All Other New Classes
class CreateClass(type):
    def __init__(self):
        pass



# Create 'Dog' Class With Name & Age Varaibles And Return Name And Return Age Functions
def dog_init(self, name, age):
    self.name = name
    self.age = age
def get_dogname(self):
    return self.name
def get_dogage(self):
    return self.age
dog_class = type("Dog", (), {"__init__": dog_init, "get_dogname": get_dogname, "get_dogage": get_dogage})
# Create 2 New Variables Of 'Dog' Class, Pass Init Values, And Print Those Stored Values
zeb = dog_class("Zeb", 6)
ember = dog_class("Ember", 10)
print("\n", "\n", "\n" + str(zeb.get_dogname()))
print(zeb.get_dogage())
print(ember.get_dogname())
print(ember.get_dogage())



# Create 'Pet' Class That 'Cat' And 'Cow' Inherit From
def pet_init(self, name, age):
    self.name = name
    self.age = age
    self.type = ""
def print_name(self):
    print(self.name)
def print_age(self):
    print(self.age)
def print_type(self):
    print(self.type)
pet_class = type("pet_class", (), {"__init__": pet_init, "print_name": print_name, "print_age": print_age,"print_type": print_type})

new_pet = pet_class("Petone", 18)

def cat_init(self, name, age):
    pet_class.__init__(self, name, age)
    self.type = "Cat"
def cat_speak(self):
    print("meow")
cat_class = type("cat_class", (pet_class, ), {"__init__": cat_init, "cat_speak": cat_speak})

new_cat = cat_class("Catone", 18)
print("\n", "\n")
new_cat.print_name()
new_cat.print_age()
new_cat.print_type()
new_cat.cat_speak()

def cow_init(self, name, age):
    pet_class.__init__(self, name, age)
    self.type = "Cow"
def cow_speak(self):
    print("moo")
cow_class = type("cow_class", (pet_class, ), {"__init__": cow_init, "cow_speak": cow_speak})

new_cow = cow_class("Cowone", 20)
print()
new_cow.print_name()
new_cow.print_age()
new_cow.print_type()
new_cow.cow_speak()



# TEST AREA
import math
def quadrilateral_init(self, sideOne, sideTwo, sideThree, sideFour, angleOne, angleTwo, angleThree, angleFour):
    self.type = ''
    self.numberofsides = 4
    self.sumofangles = 360.0
    self.sidelengthOne = float(sideOne)
    self.sidelengthTwo = float(sideTwo)
    self.sidelengthThree = float(sideThree)
    self.sidelengthFour = float(sideFour)
    self.angleOne = float(angleOne)
    self.angleTwo = float(angleTwo)
    self.angleThree = float(angleThree)
    self.angleFour = float(angleFour)
def get_type(self):
    return self.type
def get_numberofsides(self):
    return self.numberofsides
def get_sumofangles(self):
    return self.sumofangles
def get_firstside(self):
    return self.sidelengthOne
def get_secondside(self):
    return self.sidelengthTwo
def get_thirdside(self):
    return self.sidelengthThree
def get_fourthside(self):
    return self.sidelengthFour
def get_firstangle(self):
    return self.angleOne
def get_secondangle(self):
    return self.angleTwo
def get_thirdangle(self):
    return self.angleThree
def get_fourthangle(self):
    return self.angleFour
def find_perimeter(self):
    return self.sidelengthOne + self.sidelengthTwo + self.sidelengthThree + self.sidelengthFour
def find_area(self):
    return ((1/2)*(self.sidelengthOne)*(self.sidelengthTwo)*math.sin(math.radians(self.angleTwo)))+((1/2)*(self.sidelengthThree)*(self.sidelengthFour)*math.sin(math.radians(self.angleThree)))
quadrilateral_class = type("quadrilateral_class", (), {"__init__": quadrilateral_init, 
                           "get_type": get_type, "get_numberofsides": get_numberofsides, "get_sumofangles": get_sumofangles, 
                           "get_firstside": get_firstside, "get_secondside": get_secondside, 
                           "get_thirdside": get_thirdside, "get_fourthside": get_fourthside, 
                           "get_firstangle": get_firstangle, "get_secondangle": get_secondangle, 
                           "get_thirdangle": get_thirdangle, "get_fourthangle": get_fourthangle, 
                           "find_perimeter": find_perimeter, "find_area": find_area})
def trapezoid_init(self, toplength, leftsidelength, bottomlength, rightsidelength, toprightangle, topleftangle, bottomleftangle, bottomrightangle):
    quadrilateral_class.__init__(self, toplength, leftsidelength, bottomlength, rightsidelength, toprightangle, topleftangle, bottomleftangle, bottomrightangle)
    self.type = 'trapezoid'
def isoscelestrapezoid_init(self, toplength, bottomlength, sideslength, topangles, bottomangles):
    quadrilateral_class.__init__(self, toplength, sideslength, bottomlength, sideslength, topangles, topangles, bottomangles, bottomangles)
    self.type = 'isosceles trapezoid'
def parallelogram_init(self, TBlength, LRlength, TRBLangles, TLBRangles):
    quadrilateral_class.__init__(self, TBlength, LRlength, TBlength, LRlength, TRBLangles, TLBRangles, TRBLangles, TLBRangles)
    self.type = 'parallelogram'
def rectangle_init(self, TBlength, LRlength):
    quadrilateral_class.__init__(self, TBlength, LRlength, TBlength, LRlength, 90, 90, 90, 90)
    self.type = 'rectangle'
def rhombus_init(self, sidelength, TBangles, LRangles):
    quadrilateral_class.__init__(self, sidelength, sidelength, sidelength, sidelength, TBangles, LRangles, TBangles, LRangles)
    self.type = 'rhombus'
def square_init(self, sidelength):
    quadrilateral_class.__init__(self, sidelength, sidelength, sidelength, sidelength, 90, 90, 90 ,90)
    self.type = 'square'
trapezoid_class = type("trapezoid_class", (quadrilateral_class, ), {"__init__": trapezoid_init})
isoscelestrapezoid_class = type("isoscelestrapezoid_class", (quadrilateral_class, ), {"__init__": isoscelestrapezoid_init})
parallelogram_class = type("parallelogram_class", (quadrilateral_class, ), {"__init__": parallelogram_init})
rectangle_class = type("rectangle_class", (quadrilateral_class, ), {"__init__": rectangle_init})
rhombus_class = type("rhombus_class", (quadrilateral_class, ), {"__init__": rhombus_init})
square_class = type("square_class", (quadrilateral_class, ), {"__init__": square_init})

new_square = square_class(5)
print("\n", "\n")
print(new_square.get_firstside())
print(new_square.find_perimeter())
print(new_square.find_area())
new_rectangle = rectangle_class(3.5, 8)
print("\n", "\n")
print(new_rectangle.get_firstside())
print(new_rectangle.find_perimeter())
print(new_rectangle.find_area())
