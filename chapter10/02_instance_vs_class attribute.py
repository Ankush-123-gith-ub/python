class Employee:
    language="Py" # class attribute
    salary=12000000

harry = Employee()
harry.name="Harry Yadav" # instance attribute
print(harry.language,harry.salary,harry.name)

harshu = Employee()
harshu.name="Harshit Yadav"
harshu.language="java"
harshu.salary=120000000
print(harshu.language,harshu.salary,harshu.name)