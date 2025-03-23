#Decimal to Binary
decimal_number = int(input("Enter a decimal number: "))

if decimal_number == 0:
    print("0")
else:
    binary_representation = ""
    temp_number = abs(decimal_number)  # Handle negative numbers

    while temp_number > 0:
        remainder = temp_number % 2
        binary_representation = str(remainder) + binary_representation
        temp_number //= 2

    if decimal_number < 0:
      print("-" + binary_representation)
    else:
      print(binary_representation)