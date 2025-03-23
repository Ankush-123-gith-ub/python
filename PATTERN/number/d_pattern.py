n = 7

# Upper part
for i in range(n):
    print(" " * (n - i - 1), end="")
    for j in range(1, 2*i+2):
        print(j, end=" ")
    print()

# Lower part
for i in range(n-2, -1, -1):
    print(" " * (n - i - 1), end="")
    for j in range(1, 2*i+2):
        print(j, end=" ")
    print()
