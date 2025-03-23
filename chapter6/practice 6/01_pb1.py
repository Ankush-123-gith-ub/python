a=int(input("enter the number 1: "))
b=int(input("enter the number 2: "))
c=int(input("enter the number 3: "))
d=int(input("enter the number 4: "))
if(a>b and a>c and a>d):
    print("a is the greatest:",a)
elif(b>c and b>d):
    print("b is the greatest:",b)
elif(c>d):
    print("c is the greatest:",c)
else:
    print("d is the greatest:",d)