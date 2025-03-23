def decode_message(code):
    message = ""
    for num in code:
        if 1 <= num <= 26:
            message += chr(ord('A') + num - 1)
        elif 27 <= num <= 52:
            message += chr(ord('a') + num - 27)
        else:
            message += "?"  # Placeholder for invalid numbers
    return message

# Example usage
code_input = list(map(int, input("Enter numbers separated by spaces: ").split()))
message = decode_message(code_input)
print("Decoded Message:", message)