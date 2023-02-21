# dictionary
dictionary= {"a":1 , "b":2}
print(dictionary["a"])

user= {"name":"bhuwan", "age":25, "can_swim": 'false'}
print(user)
print(user["name"])
print(user.items()) # a dictionary can be change in list

# tupple
my_tupple= (1,2,3,4,5,6,7,8,9)
#my_tupple[1]=0  it will show error because tupple is immutable, tupple is like a list but it is immutable
print(my_tupple[1:4])
print(my_tupple[1:8:2])  # [start : stop : stepover]
print(my_tupple.count(5))
print(my_tupple.index(5))
print(len(my_tupple))

# Set :-  unordered collection of a unique object
my_set={1,2,2,3,3,4,5,3,6,8,7,6,}
print(my_set)
my_set.add(100)
my_set.add(2)
my_set.add(50)
print(my_set) # it will not add two because it is already there in my_set


# print(my_set[0]) # it will show error because set object does not support objecting


# formatted string
username= "deepak joshi"
age= 29
user_id="*********"
print(f"hello friend your name is {username} and you are {age} years old , your ID is {user_id}")


# [start : stop: stepover]
x='123435656457'
print(x[1:9:2])

# replace
quote="to be or not to be"
print(quote.replace("be","me"))
# uppercase
print(quote.upper())
print(quote.capitalize())