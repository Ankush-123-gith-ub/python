a=int(input("Enter your age: "))

# if staement number 1
if(a>=18):
    print("Eligible for vote")
    print("Good for you")
# end ofstatemnt 1

# if staement number 2
if (a>0):
    print("Valid age")
elif a<0:
    print("Invalid age")

elif a==0:
    print("You are entering 0 which is not valid")

else:
    print("Not eligible for vote")
# end of statement 2

print("End of program")