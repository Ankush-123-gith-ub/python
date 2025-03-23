n = list(map(int,input("Enter Numbers: ").split()))
k = int(input())
k = k % len(n)
n = n[-k:] + n[:-k]
print(n)
