class Employee:
    company="ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}.")

# class Programmer:
#      company="INFO"
#      def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}.")
#      def showlanguage(self):
#          print(f"The name is {self.name} and he is good with {self.language}.")

class Programmer(Employee):
    company="INFO"
    def showlanguage(self):
        print(f"The name is {self.name} and he is good with {self.language}.")
a=Employee()
b=Programmer()
print(a.company,b.company)


