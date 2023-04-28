"""An iterable is any Python object capable of returning its members one at a time"""

fruit_list = ("banana", "apple", "orange", "Lemon", "grapes")
new_list = iter(fruit_list)

print(next(new_list))
print(next(new_list))
print(next(new_list))
print(next(new_list))
print(next(new_list))

# iterate over string using iter and next function

fruit_list = "\nBanana"
new_list = iter(fruit_list)

print(next(new_list))
print(next(new_list))
print(next(new_list))
print(next(new_list))
print(next(new_list))
print(next(new_list))

# for loop to iterate through a tuple      #  iterate over string using for loop is same like this

fruit_list = ("banana", "apple", "orange", "Lemon", "grapes\n")
for i in fruit_list:
    print(i)


class Counting:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x

new_object = Counting()
newit = iter(new_object)

print(next(newit))
print(next(newit))
print(next(newit))
print(next(newit))
print(next(newit))
print(next(newit))
print(next(newit))
print(next(newit))
print(end="\n")


# raise StopIteration

class Counting:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <=29:
          z = self.a
          self.a += 1
          return z
        else:
           raise StopIteration


new_object = Counting()
new_it = iter(new_object)

for i in new_it:
    print(i)










