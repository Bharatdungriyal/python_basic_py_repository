#.................................public...................................
class Student:
    # constructor is defined
    def __init__(self, age, name):
        self.age = age               # public variable
        self.name = name             # public variable

obj = Student(21,"Harry")
print(obj.age)
print(obj.name)
'''All the variables and methods (member functions) in python are by default public.
 Any instance variable in a class followed by the ‘self’ keyword ie. self.var_name are public accessed.'''

#____________________________________________private___________________________________________
class employee:
    def __init__(self):
        self.__name = "bhavi"

a = employee()
#print(a.__name)  cannot be accessed directly
print(a._employee__name)  # but can be accessed indirectly due to Name mangling
print(a.__dir__())
'''Name mangling in Python is a technique used to protect class-private and superclass-private attributes
 from being accidentally overwritten by subclasses. Names of class-private and superclass-private attributes
  are transformed by the addition of a single leading underscore and a double leading underscore respectively.'''

class MyClass:
    def __init__(self):
        self._nonmangled_attribute = "I am a nonmangled attribute"
        self.__mangled_attribute = "I am a mangled attribute"

my_object = MyClass()

print(my_object._nonmangled_attribute) # Output: I am a nonmangled attribute
#print(my_object.__mangled_attribute) # Throws an AttributeError
print(my_object._MyClass__mangled_attribute) # Output: I am a mangled attribute


#..............................................protected...........................................
class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()
print(dir(obj))

# calling by object of Student class
print(obj._name)
print(obj._funName())
# calling by object of Subject class
print(obj1._name)
print(obj1._funName())
'''In object-oriented programming (OOP), the term "protected" is used to describe a 
member (i.e., a method or attribute) of a class that is intended to be accessed only by 
the class itself and its subclasses. In Python, the convention for indicating that a member is protected 

is to prefix its name with a single underscore (_)'''