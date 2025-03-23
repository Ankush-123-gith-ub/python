a,b,c = map(int,input("enter the marks: ").split())
Updated_Marks = {'Math': a, 'Science': b, 'English': c,'History': 88}
print(Updated_Marks.values())
print(Updated_Marks.keys())
print(Updated_Marks.items())
count = 0
sum = 0
for i in Updated_Marks.values():
    sum += i
    count += 1
avg =  (sum/count)
print(sum)
print(count)
print(avg)
