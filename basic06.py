# function
def say_hello():
    print("My name is bharat sharma,I am the student of galgotias university")
say_hello()
say_hello()     # it is used to avoide the rewriting of same line of code or paragraph.
say_hello()

def say_wish(name,age):
    print(f"Hello {name} you are {age} years old now ")

say_wish("Deepak sir","28")
say_wish("bhavi","19")

def function1(a,b):
    print("hello you are in function1 in which the addition of a and b is ",a+b)
function1(4,5)


def function(a,b):
    average=(a+b)/2
    print(f"the average of the numbers a and b is {average}")
function(5,4)    # to find the average of two number



#    *args and **kwargs


def fun(a,b,c,d):
    print(a,b,c,d)
fun("larry","carry","jerry","merry")
""" if we add one more name here without increasing alphabets upper like a,b,c,d,e so it will show error,
  now let suppose we have thousands of name here and we can't take a,b,c,d etc much now and it will also 
  so boring and time taking so we will use the *args and **kwargs here to add the name easily or for
   making code suitable"""


def funargs(*args):
    for item in args:
        print(item)

usename= ["bhavi","deepika","deepak","bharti"]
funargs(*usename)


def funargs(normal,*args):
    print(normal)
    for item in args:
        print(item)
x= ["larry","carry","jerry","merry"]
normal= "I am a normal guy"
funargs(normal,*x)


def funargu(normal,*args,**Kwargs):
    print(normal)
    for item in args:
        print(item)
    print("\nnow i would like to introduce you with some of my friends")
    for Key,Value in Kwargs.items():
        print(f"{Key} is a {Value}.")

KW={"bhavi":"job seeker","deepika":"teacher","deepak":"software engineer","bharti":"airhostess" }
arg=["larry","carry","jerry","merry"]
funargu(normal,*arg,**KW)
"""(normal,*args,**kwargs)  we can write anyhting in the place of args and kwargs
 like (normal,*argxyz,**kwargslmn)"""