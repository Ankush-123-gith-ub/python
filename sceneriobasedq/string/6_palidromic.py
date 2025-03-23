n  = input("Enter the string: ")
count = 0
for i in n:
    if n.count(i) == 1:
        count += 1
if count > 1:
    print("False.")
else:
    print("True.")

