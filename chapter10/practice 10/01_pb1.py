class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary = salary
        self.pin = pin
p=Programmer("Harry",12000000,234389)
p=Programmer("rohan",12000000,334389)
print(p.name,p.salary,p.pin,p.company)