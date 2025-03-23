class Employee:
    company="ITC"
    name="hary"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.company}.")

class Coder:
     language="python"
     def printlanguage(self):
         print(f"Out of all language here is your language = {self.language}.")

class Programmer(Employee,Coder):
    company="INFO"
    def showlanguage(self):
        print(f"The name is {self.company} and he is good with {self.language}.")
a=Employee()
b=Programmer()
b.show()
b.printlanguage()
b.showlanguage()


