n = input().split()
sum = 0
count = 0
for i in n:
    a = 1/int(i)
    sum += a
    count += 1
harmonic_c = count/sum
print(round(harmonic_c,2))
print(f"Harmonic mean: {harmonic_c:.2f}")
