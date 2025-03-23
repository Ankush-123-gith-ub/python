n = int(input("Enter the number: "))
sq_n = n**2
revn = int(str(sq_n)[::-1])
a = int((revn)**(1/2))
# a = int(math.sqrt(revn))
new_n = int(str(a)[::-1])
if n == new_n:
    print("This is Adom number.")
else:
    print("Not an Adom number.")

