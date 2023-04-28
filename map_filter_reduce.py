"""+++++++++++++++++++++++++++++++Map, Filter and Reduce+++++++++++++++++++++++++++

In Python, the map, filter, and reduce functions are built-in functions that allow you to apply a function
to a sequence of elements and return a new sequence. These functions are known as
higher-order functions, as they take other functions as arguments."""

"""----------------------------------- map----------------------------------
The map function applies a function to each element in a sequence and returns a new sequence
 containing the transformed elements. The map function has the following syntax:

map(function, iterable)
"""

nums=[2,3,4,5,6,7,8,9]

double= list(map(lambda n: n*2,nums))
print(double)
"""_______________________________filter________________________________________
The filter function filters a sequence of elements based on a given predicate 
(a function that returns a boolean value) and returns a new sequence containing only the elements that meet 
the predicate. The filter function has the following syntax:

filter(predicate, iterable)"""



# List of numbers
numbers = [1, 2, 3, 4, 5]

# Get only the even numbers using the filter function
evens = filter(lambda x: x % 2 == 0, numbers)

# Print the even numbers
print(list(evens))

"""In the above example, the lambda function lambda x: x % 2 == 0 is used to filter the numbers
 list and return only the even numbers. The filter function applies the lambda function to each element
 in the list and returns a new list containing only the even numbers. 
 for example we have different companies mobiles like samsung ,vivo,lava,iphone,redmi,Oneplus,Jio etc now when
 we seperate the iphones from different companies phones so it will called the filter 
"""



#  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^reduce^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""The reduce function is a higher-order function that applies a function to a sequence 
and returns a single value. It is a part of the functools module in Python and has the following syntax:

               reduce(function, iterable)"""



from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate the sum of the numbers using the reduce function
sum = reduce(lambda x, y: x + y, numbers)

# Print the sum
print(sum)

"""In the above example, the reduce function applies the lambda function lambda x, y: x + y to the elements in 
the numbers list. The lambda function adds the two arguments x and y and returns the result. The reduce function
 applies the lambda function to the first two elements in the list (1 and 2), then applies the function to
 the result (3) and the next element (3), and so on. The final result is the sum of all the elements in
  the list, which is 15.
  
  It is important to note that the reduce function requires the functools module to be imported
   in order to use it."""