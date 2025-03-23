a = int(input())
b = int(input())
c = int(input())
if( a == b == c):
    print("Triangle ia an equilateral triangle.")
elif( a == b or a == c or b == c):
    print("Triangle ia an isosceles triangle.")
else:
    print("Triangle ia an scalene triangle.")