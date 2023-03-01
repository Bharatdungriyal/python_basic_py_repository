class math:
    def __init__(self,num):
        self.num=num

    def add_to_num(self,n):
        self.num=self.num + n


    @staticmethod
    def add(a,b):
        return a+b


a= math(5)
print(a.num)
a.add_to_num(6)
print(a.num)

print(math.add(7,2))

"""  it is necessary to use self argument while making method in a class? no
because  can make @staticmethod here """