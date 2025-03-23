n = list(map(int,input("Enter the numbers: ").split()))
for i in n:
    if i >= 1 and i<= 26:
        print(chr(64+i),end="")
    elif i >= 27 and i <= 52:
        print(chr(70+i),end="")
