try :
    a = int(input("Enter the 1number: "))
    b = int(input("Enter the 2number: "))
    print(a/b)

except ZeroDivisionError as E:
    print("infinite")






