n = list(map(int,input("Enter the numbers: ").split()))
r = int(input("Enter the rotating number: "))
print(n[-r:] + n[:-r])
