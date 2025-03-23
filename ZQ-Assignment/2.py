t = 2 # years
p = int(input())
r = int(input())
ti = p*(1+r/100)**t
ci = ti - p
print(ci)