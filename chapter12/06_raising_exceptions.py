a=int(input("Enter  the first number: "))
b=int(input("Enter  the seond number: "))
if(b==0):
    raise ZeroDivisionError("Hey our program is not meant to divide by zero.")
print(f"The division is {a/b}.")
