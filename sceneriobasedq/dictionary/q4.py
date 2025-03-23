n = int(input("Enter the turns: "))
dict = {}
dict_b ={}
for i in range(n):
    a = int(input("Enter the number: "))
    b = input("Enter the name: ")
    dict[a] = b
    dict_b[a] = len(b)
print(dict)
print(dict_b)