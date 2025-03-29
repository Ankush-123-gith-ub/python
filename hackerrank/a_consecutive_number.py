n = int(input())
sum = 0
for i in range(1,n+1,3):
        for j in range(i,i+3):
            if j <= n:
                sum += i
print(sum)


