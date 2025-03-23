class Employee:
    salary = 234
    increment = 20
    
    @property
    def salaryAfterIncrement(self):
        newsalary=(self.salary + self.salary * (self.increment/100))
        return newsalary
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,newsalary):
        self.increment = ((newsalary/self.salary)-1)*100

e = Employee()

# print(e.salaryAfterIncrement)
e.salaryAfterIncrement=280.8
print(e.increment)