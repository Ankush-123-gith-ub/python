###################### HCF ######################
a,b = map(int,input().split())
for i in range(1,min(a,b)):
    if a % i == 0 and b % i == 0:
        hcf = i
print(hcf)