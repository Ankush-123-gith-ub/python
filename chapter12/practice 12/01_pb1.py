try:
    with open("1.txt","r") as f:
        print(f.read())
except Exception as E:
    print(E)

try:
    with open("2.txt","r") as f:
        print(f.read())
except Exception as E:
    print(E)

try:
    with open("3.txt","r") as f:
        print(f.read())
except Exception as E:
    print(E)

print("Thank you..")
    
