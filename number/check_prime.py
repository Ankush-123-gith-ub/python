# using for loop
# n = int(input("Enter the number: "))
# if n < 2:
#     print("Not Prime.")
# else:
#     a = 1
#     for i in range(2,n):
#         if n % i == 0:
#             a = 0
#             break
#     if a:
#         print("Yes, This is prime.") 
#     else:
#         print("No, This is not prime.")
n = int(input("Enter the number: "))
if n < 2:
    print("Not Prime.")
else:
    a = 1
    i = 2
    while i < n:
        if n % i == 0:
            a = 0
            break
        i = i + 1
    if a:
        print("Yes, This is prime.")
    else:
        print("No, This is not prime.")



