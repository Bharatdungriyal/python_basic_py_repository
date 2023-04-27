"""Generators in Python are special type of functions that allow you to create an iterable sequence
of values. A generator function returns a generator object, which can be used to generate the values
 one-by-one as you iterate over it. Generators are a powerful tool for working with large or complex data sets,
  as they allow you to generate the values on-the-fly, rather than having to create and store the entire
sequence in memory."""


"""In Python, you can create a generator by using the yield statement in a function. 
The yield statement returns a value from the generator 
and suspends the execution of the function until the next value is requested. Here's an example:"""
def my_generator():
    for i in range(500):
      # Complex computations
      yield i

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))

#for j in  gen:
#  print(j)


"""Generators offer several benefits over other types of sequences, such as lists, tuples, and sets. 
One of the main benefits of generators is that they allow you to generate the values on-the-fly, rather than
 having to create and store the entire sequence in memory. This makes generators a powerful tool for working 
 with large or complex data sets, as you can generate the values as you need them, rather than having to store
  them all in memory at once."""

""" Another benefit of generators is that they are lazy, which means that the values are generated 
only when they are requested. This allows you to generate the values in a more efficient and memory-friendly 
manner, as you don't have to generate all the values up front."""


def topten():
    n=1

    while n<=10:
        sq=n*n
        yield sq
        n=n+1

value = topten()

for i in value:
    print(i)
