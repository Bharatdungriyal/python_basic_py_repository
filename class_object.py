class person():
    name="deepak"
    occupation="software engineer"
    networth= 100000
    def info(self):
      print(f'{self.name} is a {self.occupation}')


a=person()
print(a.name,a.occupation,a.networth)
a.info()

b=person()
b.name="bhavi"
b.occupation="job seeker"
print(b.name)
b.info()

c=person()
c.name="larry"
c.occupation="doctor"
c.info()



class playerCharater :
   def __init__(self,name,age) :
        self.name= name
        self.age= age

   def run(self):
    print("run")
    return Done

player1= playerCharater("burry",23)
player2= playerCharater("furry",32)

print(player1.name)
print(player2.name)

