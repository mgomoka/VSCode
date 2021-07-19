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

