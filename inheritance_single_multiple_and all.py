"""Single inheritance is a type of inheritance where a class inherits
properties and behaviors from a single parent class.
This is the simplest and most common form of inheritance.
Single inheritance is a powerful tool in Python that allows you to create new classes
 based on existing classes. It allows you to reuse code, extend it to fit your needs,
  and make it easier to manage complex systems. Understanding single inheritance is an important step
  in becoming proficient in object-oriented programming in Python."""
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal")


class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed

    def make_sound(self):
        print("Bark!")


d = Dog("Dog", "Doggerman")
d.make_sound()

a = Animal("Dog", "Dog")
a.make_sound()

# *********************     {multiple inheritance}       ******************************

class Employee:
  def __init__(self, name):
    self.name = name
  def show(self):
    print(f"The name is {self.name}")

class Dancer:
  def __init__(self, dance):
    self.dance = dance

  def show(self):
    print(f"The dance is {self.dance}")

class DancerEmployee(Employee, Dancer):
  def __init__(self, dance, name):
    self.dance = dance
    self.name = name

o  = DancerEmployee("Kathak", "Shivani")
print(o.name)
print(o.dance)
o.show()
print(DancerEmployee.mro())   # method resolution order

""" Multiple inheritance is a powerful feature in object-oriented programming that allows a class to inherit 
attributes and methods from multiple parent classes. This can be useful in situations
where a class needs to inherit functionality from multiple sources. """

#  ________________________  multilevel inheritance  ______________________

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")


class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed

    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")


class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color

    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")


o = Dog("tommy", "Black")
o.show_details()
print(GoldenRetriever.mro())
"""In this example, we have three classes: Animal, Dog, and GoldenRetriever.
The Dog class inherits from the Animal class, and the GoldenRetriever class inherits from the Dog class.
Now, when we create an object of the GoldenRetriever class, it has access to all 
the attributes and methods of the Animal class and the Dog class. 
We can also see that the GoldenRetriever class has its 
own attributes and methods that are specific to the class."""

# +++++++++++++++++++++++++   hybrid inheritance  ++++++++++++++++++++++

"""Hybrid inheritance is a combination of multiple inheritance and single inheritance 
in object-oriented programming. It is a type of inheritance in which multiple inheritance is 
used to inherit the properties of multiple base classes into a single derived class, 
and single inheritance is used to inherit the properties of the derived class into a sub-derived class."""


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Person(Human):
    def __init__(self, name, age, address):
        Human.__init__(self, name, age)
        self.address = address

    def show_details(self):
        Human.show_details(self)
        print("Address:", self.address)


class Program:
    def __init__(self, program_name, duration):
        self.program_name = program_name
        self.duration = duration

    def show_details(self):
        print("Program Name:", self.program_name)
        print("Duration:", self.duration)


class Student(Person):
    def __init__(self, name, age, address, program):
        Person.__init__(self, name, age, address)
        self.program = program

    def show_details(self):
        Person.show_details(self)
        self.program.show_details()
program = Program("Computer Science", 4)
student = Student("John Doe", 25, "123 Main St.", program)
"""In this example, the Student class inherits from the Person class,which in turn inherits from the
 Human class. The Student class also has an association with the Program class. This is an example 
 of Hybrid Inheritance in action, as it uses both Single Inheritance and Association 
to achieve the desired inheritance structure."""

# ----------------------   Hierarchical inheritance  ----------------------------------
"""Hierarchical Inheritance is a type of inheritance in Object-Oriented Programming where multiple 
subclasses inherit from a single base class. In other words, a single base class acts as a parent class 
for multiple subclasses. This is a way of establishing relationships between classes in a hierarchical manner."""

class Animal:
    def __init__(self, name):
        self.name = name

    def show_details(self):
        print("Name:", self.name)

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name)
        self.breed = breed

    def show_details(self):
        Animal.show_details(self)
        print("Species: Dog")
        print("Breed:", self.breed)

class Cat(Animal):
    def __init__(self, name, color):
        Animal.__init__(self, name)
        self.color = color

    def show_details(self):
        Animal.show_details(self)
        print("Species: Cat")
        print("Color:", self.color)
dog = Dog("phlophy", "Lahasa")
dog.show_details()
cat = Cat("billu", "Black")
cat.show_details()

""" In the above code, the Animal class acts as the base class for two subclasses, Dog and Cat.
The Dog class and the Cat class inherit the attributes and methods of the Animal class.
However, they can also add their own unique attributes and methods."""