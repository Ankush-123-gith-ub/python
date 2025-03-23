from functools import reduce
l1=[1,243,43,805,900,5,1,1088,56]

def greater(a,b):
    if(a>b):
        return a
    return b
print(reduce(greater,l1))