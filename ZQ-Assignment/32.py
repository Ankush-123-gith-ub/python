l = input("Enter the  numbers: ").split()
list = [int (x) if x.isdigit() else x for x in l]
n =  None 
for i in list:
    if(i % 3 == 0):
        if(n is None or i > n ):
           n = i
if n is not None:
    print(n)
    
