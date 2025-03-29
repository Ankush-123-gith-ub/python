m = input().split()
n = len(m)
sum = 0
for i in range(1,n+1):
    sum += (1/i)
print((round((sum/n),2)))