def div5(n):
    if(n % 5==0):
        return True
    return False
l1=[1,23,43,80,90,5,1,10,56]
f=list(filter(div5,l1))
print(f)