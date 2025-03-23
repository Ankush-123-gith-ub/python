class Employee:
    language="Py" # class attribute
    salary=12000000

    def getInfo(self):
        self.name=input("name is:")
        print(f"the language is {self.language}")
        print(f"salary is {self.salary}")
        print(f"the name is {self.name}")
    @staticmethod
    def greet():
        print("Good Mornig")

harry=Employee()
harry.getInfo() #1st method
harshu=Employee()
Employee.getInfo(harshu) #second method
harshu.greet()