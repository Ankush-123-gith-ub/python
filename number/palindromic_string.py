# n = input()
# # Count Character Frequencies
# odd_count = 0 
# for char in n:
#     a = n.count(char)
#     if a % 2 != 0:
#         odd_count += 1
# if odd_count <= 1:
#     print("True")
# else:
#     print("False")

n = input()
# Count Character Frequencies
odd_count = 0 
frequency = {}
for char in n:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
for i in frequency.values():
    if i % 2 != 0:
        odd_count += 1
if odd_count <= 1:
    print("True")
else:
    print("False")
    


