n = tuple(map(str,input("Enter the strings: ").split()))
e = input("Enter the employee name:")
for i in range(len(n)):
    if n[i] == e:
        print(f"Index of {e}: {i}")
        break
else:
    print(-1)   

