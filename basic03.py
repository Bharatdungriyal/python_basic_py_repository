# if,else,elif  statement
is_old = True
is_licenced=True
if is_old :
    print("you are old enough to drive")
elif is_licenced:
    print("you can drive easily")
else :
    print("you can't drive")


# can vote or not
age =int(input("whats your age now ?\n"))

if age<18:
    print("you cannot vote due you less age")
elif age==18:
    print(" you can vote after verifying your documents")
else :
    print("you are old enough,you can vote easily by showing your voter id ")




# truthy falsy
is_magician= False
is_expert= True

if is_expert and is_magician :
    print("you are a master magician")
elif is_magician and not is_expert:
    print("atleast you are doing something it's impressive")
elif not is_magician:
    print("you need megician power")

print(4==5)
print(4>5)
print(4<5)
print(5== 5)
print(4!=4)
print(4!=5)    # != means not equals to
print(True==1) # true because == option check the equality
print(" "==1 ) #false
print([]==1) #false
print("1"==1) # it is false because there is a string and a integer
print([]==[]) # true



# loops
for items in ("hello world\n"):
    print(items,end=" ")  # end=" " to write something in a line


for item in (1,2,3,4,5,6):
    for x in ["a","b","c","d","e"]:
        print(item,x)


user= {"name":"bhuwan", "age":25, "can_swim": 'false'}

for item in user.items():
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)


list=[int, float,"bhavi",5,3,6,7,1,3,2,23]

for item in list:
    if str(item).isnumeric()and item<6:
        print(item,end=" ")


# counter
my_list=[1,2,3,4,5,6,7,8,9,10]
counter=0
for item in my_list:
    counter= counter + item
    print(counter)

# range()

for number in range(0,100):
    print(number)

for number in range(10):
    print("hello sir , good morning")

# enumerate
for i,char in enumerate("hello world",start=1):
    print(i,char)


"""for i,char in enumerate (list(range(100))):
    print(i,char)
    if char==50:
     print(f'index of 50 is : {i}')"""



# while loop
i=0
while i<50:
    print(i)
    i +=1

while True:
    response= input("say something")
    if (response== "bye"):
        break
