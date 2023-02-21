#------------join function------------------
list=["john cena","roman reings","khali"]
for item in list:
   # print(item , "and")
    print(item,"and",end=" ")
print("other WWE stars")
a= " and ".join(list)
print(a,  "other WWE Stars")


# lambda function or anonymous functions
def add(a,b):
    return a+b
print(add(5,6))
          # both gives same result but with the help of lambda we write less code as compare to other
add= lambda x,y:x+y
print(add(5,6))

double= lambda x:x*2
cube= lambda x:x**3
print(cube(5))
print(double(85))

avg= lambda x,y,z: (x+y+z)/3
print(avg(5,6,2))


#-----------------break and continue--------------------------------

for i in range(12):
   if(i == 10):
     print("Skip the iteration")
     continue
   print("5 X", i, "=", 5 * i)
   #  it just leave the iteration,it does not leave the loop just do not read the particular line of code.


i = 0
while True:
    print(i)              #  it break the loop
    i = i + 1
    if (i % 100 == 0):
        break