t = int(input("Enter the testcase: "))
temp = []
for i in range(t):
    n = int(input("Enter the number: "))
    temp.append(n)
temp.sort()  #method 1
print(temp)  #method 1
# another method
# for j in range(len(temp)):
#     for j in range(len(temp)-1):
#         if temp[j] > temp[j+1]:
#             a = temp[j]
#             temp[j] = temp[j+1]
#             temp[j+1] = a
# print(temp)