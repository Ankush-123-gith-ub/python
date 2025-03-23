n = int(input("Enter the number: "))

table=[n*i for i in range(1,11)]

with open("tables.txt","a") as t:
    # t.write(str(table) + "\n")
    t.write(f"{str(table)}\n")