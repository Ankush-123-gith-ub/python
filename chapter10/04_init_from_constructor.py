class Employee:
    language="Py" # class attribute
    salary=12000000

    def __init__(self,name,salary,language):# dunder method which is autimatically called
        self.name=name
        self.salary=salary
        self.language=language
        print("I am creating an object")

    @staticmethod
    def greet():
        print("Good Mornig")

harry=Employee("Harry",1200000,"Java")
print(harry.name,harry.salary,harry.language)
