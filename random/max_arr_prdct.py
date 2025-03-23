# n = input("Enter the numbers: ").split()
n = list(map(int,input("Enter the numbers: ").split()))
length = len(n)
if length < 2:
    print("Bhad me jao")
else:
    max_prdct = n[0]*n[1]
for i in range(length-1):
    if n[i]*n[i+1] > max_prdct:
        max_prdct = n[i]*n[i+1]
        a = n[i]
        b = n[i+1]
print(f"Max product of {a} * {b} = {max_prdct}.")



