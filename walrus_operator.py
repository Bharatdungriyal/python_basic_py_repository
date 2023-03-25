"""The Walrus Operator is a new addition to Python 3.8 and allows you to assign a value to
a variable within an expression. This can be useful when you need to use a value multiple times in a loop,
 but don't want to repeat the calculation.
The Walrus Operator is represented by the := syntax and can be used in a variety of contexts including
 while loops and if statements.
"""



happy = False
print(happy)
print(happy := True)
""" 
foods = list()
while True:             without walrus operator
  food = input("What food do you like?: ")
  if food == "quit":
      break
  foods.append(food) """
foods = list()                      # with walrus operator
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)



