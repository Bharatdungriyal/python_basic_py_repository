    #   try and except
a= input("enter number whose table you want :")  # to write table
try:
     for i in range(1,11):
          print(f" {int(a)} X {i} = {int(a)*i}")
except:
     print("invalid input!")



try:
     x= int(input("what is the value ?"))
     print(f"x is {x}")
except ValueError :
     print("x is m=not an integer")

try:
     num=int(input("enter an integer: "))
     print(num)
except ValueError:
     print("Enter no. is not an integer")


#     import

import random
coin=random.choice(["heads","tails"])
print(coin)


import random
number= random.randint(1,10)  # it's like probability to get any one number from 1 to 10
print(number)



import random
cards=["jacks","queen","king"]  # to shuffle the cards
random.shuffle(cards)
for card in cards:
         print(card,end="\n")


#  statics
import statistics
print(statistics.mean([100,90]))


# recursion in python to find factorial

def factorial(n):
     if(n==0 or n==1):
          return 1
     else:
          return n*factorial(n-1)

print(factorial(5))





































