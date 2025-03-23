cp = int(input("Enter CP: "))
s = int(input("Enter S: "))

if cp < s:
    a = (s/cp)*100 - 100
    print("Profit.")
    print(f"{a:.2f}%")
if cp > s:
    a = 100 - (s/cp)*100 
    print("Loss.")
    print(f"{round(a,2)}%")
if cp == s:
    print("No profit no loss.")
