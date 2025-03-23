# 5/9 * (f-32)
strt = int(input("Enter temperature in fahrenheit: "))
end = int(input("Enter temperature in fahrenheit: "))
step_value = int(input("Enter temperature in fahrenheit: "))
while strt <= end:
    c = (5/9)*((strt) - 32)
    print(strt,int(c))
    strt  = strt + step_value
