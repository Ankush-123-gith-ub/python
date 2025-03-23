n = input()
countu,countl,countd,counts = 0,0,0,0
s = " " in n
if len(n) <= 8:
    for i in n:
        if i.isupper():
            countu += 1
        if i.islower():
            countl += 1
        if i.isdigit():
            countd += 1
        if i in "!#$%&'()*+,-./:;<=>?@^_`{|}~©®™§¶°±÷×√∑∞≈≠≤≥€£¥₩₹¢¤¬µªº¿":
            counts += 1
    if countu >=1 and countl >=1 and countd >=1 and counts >=1 and s == False:
        print("Valid")
    else:
        print("Invalid")
else:
    print("Invalid")
