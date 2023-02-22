# scope =
a=1            # global scope
def confusion():
    a=5         #local scope
    return a
print(a)
print(confusion())

b=10
def solution(b):
    print(b)
solution(300)   # parameters are considered as local variables

l=10
def function1(n):
    m=12
    global l       # global keyword
    l = l + 34
    print(l,m)
    print(n,"i have printed")
function1("this is me")


def bhavi():
    x=20
    def rohan():
        global x
        x=80   # after adding global it jumped outside to check global value
    print("before calling rohan()",x)
    rohan()
    print("after calling rihan()",x)
bhavi()
print(x)
