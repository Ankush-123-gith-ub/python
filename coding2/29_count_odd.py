strt = int(input("Enter first range: ")) 
end = int(input("Enter last range: "))
count = 0 
for i in range(strt,end + 1):
    if i % 2 != 0:
        count += 1
print(count)

