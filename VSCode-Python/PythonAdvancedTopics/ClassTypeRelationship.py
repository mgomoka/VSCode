""" Creates New Class 'Person' With Name Attribute
class Person:
    def __init__(self, name):
        self.name = name
"""

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

"""
# Create 'Pet' Class That 'Cat' And 'Cow' Inherit From
def pet_init(self, name, age):
    self.name = name
    self.age = age
    self.type
pet_class = type("pet_class", (), {"__init__": pet_init})
def cat_init(self, name, age):
    super().__init__(name, age)
    self.type = 'Cat'
def cat_speak(self):
    print("meow")
def cow_init(self):
    self.type = 'Cow'
def cow_speak(self):
    print("moo")
cat_class = type("cat_class", (pet_class, ), {"__init__": cat_init, "cat_speak": cat_speak})
new_cat = cat_class('Catone', 12)
new_cat.cat_speak()
"""
