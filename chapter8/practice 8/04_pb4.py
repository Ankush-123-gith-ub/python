def sum_of_n(n):
    if n==1:
        return 1
    return n+sum_of_n(n-1)

n=int(input("Enter the number: "))
print(f"Sum of n is {sum_of_n(n)}")
