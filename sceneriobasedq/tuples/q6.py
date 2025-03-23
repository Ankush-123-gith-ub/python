a = tuple(map(int,input("Enter the strings: ").split(",")))
b = tuple(map(int,input("Enter the strings: ").split(",")))
for i in a:
    for j in b:
        if i == j:
            print(f"({i})")