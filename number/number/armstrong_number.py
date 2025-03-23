n = input()
count = len(n)
temp = int(n)
rev = 0
while n != 0:
    a = int(n) % 10
    rev = a**count + rev
    n = int(n) // 10
print(rev)
if temp == rev:
    print("Armstrong.")
else:
    print("Not Armstrong.")