#...................................constructors..............................................

class Employee:
  def __init__(self,n,o):
    print("hey i am an employee")   # default constructor
    self.name=n                         # parameterised constructor
    self.occ= o                   # parameterised constructor

  def info(self):
    print(f"{self.name} is a {self.occ}")

d = Employee("deepak", "developer")
e = Employee("munish", "teacher")
d.info()
e.info()

#..............................decorators..........................................
def greet(fx):
    def mfx():
        print("good morning")
        fx()
        print("thanks for using this function")
    return mfx

@greet
def hello():
    print("hello world")

hello()

def greet(fx):
    def mfx(*args,**kwargs):
        print("good morning")
        fx(*args,**kwargs)
        print("thanks for using this function")
    return mfx
  # *args and **kwargs is a method of taking an argument in the form of tupple and dictionary.
@greet
def add(a,b):
  print(a+b)

add(1,4)

