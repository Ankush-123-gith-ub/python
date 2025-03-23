n = input("Enter the string to be checked: ")
temp = "qwertyuiopasdfghjklzxcvbnm"
for i in temp:
    if i not in n.lower():
        print("False")
        break
else:
    print("True")

