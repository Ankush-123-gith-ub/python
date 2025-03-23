def price_tax(p,q):
    total_a = p*q
    if total_a <= 999:
        tax_a = (10/100)*total_a
    elif total_a > 999 and total_a < 10000:
        tax_a = (15/100)*total_a
    if total_a > 9999  :
        tax_a = (22/100)*total_a
    bill_a = total_a + tax_a
    print(total_a,tax_a,bill_a)
    return 0
price = int(input())
quantity = int(input())
print(price_tax(price,quantity))
