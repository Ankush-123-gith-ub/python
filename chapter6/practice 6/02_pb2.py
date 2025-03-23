s1=int(input("enter the s1number 1: "))
s2=int(input("enter the s2number 2: "))
s3=int(input("enter the s3number 3: "))
#check for percentage
total_percentage=(s1+s2+s3)/3

#check condition
if(total_percentage>=40):
    if(s1>=33 and s2>=33 and s3>=33 ):
        print("Student is passed.",total_percentage)
    else:
        print("Student is failed.",total_percentage)
else:
    print("Student is failed.",total_percentage)
