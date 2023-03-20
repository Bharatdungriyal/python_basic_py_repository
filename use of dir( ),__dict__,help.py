#..............dir().........................
""" The dir() function returns a list of all the attributes and methods (including dunder methods)
available for an object. It is a useful tool for discovering what you can do with an object. Example: """
x = [1, 2, 3]
print(dir(x))
print(x.__add__)
#..................... __dict__.......................
"""The __dict__ attribute returns a dictionary representation
of an object's attributes. It is a useful tool for introspection. Example: """
class Person:
   def __init__(self, name, age):
    self.name = name
    self.age = age

p = Person("John", 30)
print(p.__dict__)

#..............help()..................
"""The help() function is used to get help
 documentation for an object, including a description of its attributes and methods. Example: """
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1


p = Person("John", 30)
print(p.__dict__)

print(help(Person))
#print(help(str)) it will give you information about str what is it and so on .