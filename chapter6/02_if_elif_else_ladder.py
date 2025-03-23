a=int(input("Enter your age: "))

if(a>=18):
    print("Eligible for vote")
    print("Good for you")

elif a<0:
    print("Invalid age")

elif a==0:
    print("You are entering 0 which is not valid")

else:
    print("Not eligible for vote")


print("End of program")