def q(n):   
    length = len(n)
    sum_o = 0
    sum_e = 0
    for i in range(length):
        if i % 2 == 0:
            sum_o += int(n[i])
        if i % 2 != 0:
            sum_e += int(n[i])
    if (sum_e - sum_o) % 2 != 0:
        return True
    else:
        return False
n = input("Enter digit: ")
print(q(n))

