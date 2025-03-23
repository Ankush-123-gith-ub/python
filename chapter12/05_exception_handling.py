try:
    a=int(input("Hey,Enter a number: "))

except ValueError as v:
    print("Heyy")
    print(v)

except Exception as E:
    print(E)

print("Thank You.")