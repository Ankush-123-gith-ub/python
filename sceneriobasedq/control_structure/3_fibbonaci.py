n= int(input("Enter the number: "))
a = 0
print(a,end=" ")
b = 1
print(b,end=" ")
sum = 0
for i in range(n-2):
    sum = a + b
    print(sum,end=" ")
    a = b
    b = sum


    