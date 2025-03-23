n = list(map(int,input("Enter the numbers: ").split()))
strt = n[0]
end = n[-1]
temp = []
for i in range(strt,end+1):
    temp.append(i)
for i in range(len(n)):
    if n[i] != temp[i]:
        print(f"The series {temp} is expected, but {temp[i]} is missing.")
        break