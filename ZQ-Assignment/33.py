l = input("Enter the  numbers: ").split(",")
list = [int (x) if x.isdigit() else x for x in l]
n =  None 
for i in list:
    if(n is None or len(i) < n ):
           n = len(i)
for k in list:
      if(len(k) == n):
            print(k)
            
