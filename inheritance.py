class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def show_details(self):
        print(f"name of employee: {self.id} is {self.name}")


class programmer(employee):
    def showlanguage(self):
        print("THE default language is python")


e1=employee("bhuwan",321)
e1.show_details()
e2=employee("ravi",987)
e2.show_details()
# e2.showlanguage  # it will show error because it is not defined in employee.
e3=programmer("deepu",123)
e3.showlanguage()

# employee is like a dad and programmer is like a son who have his dad qualities as well as self also.
