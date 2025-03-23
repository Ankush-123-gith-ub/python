a = int(input())
b = int(input())
c = int(input())
if a == b and a == c:
    print("Equilateral triangle.")
elif a == b and a != c or a != b and a == c:
    print("Isosceles triangle.")
elif a != b and a != c:
    print("Scalene triangle.")