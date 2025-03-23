class Employee:
    a=1
    @classmethod
    def show(self):
        print(f"The Class value of  is {self.a}")
    
e=Employee()
e.a=45
e.show()