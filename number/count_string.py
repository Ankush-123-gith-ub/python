n = input("")
vowels = "aeiouAEIOU"
digits = "0123456789"
c_vowels = 0
c_digits = 0
c_consonANTS = 0
for i in n:
    if i in vowels:
        c_vowels = c_vowels + 1
    elif i in digits:
        c_digits = c_digits + 1
    elif i.isalpha():
        c_consonANTS = c_consonANTS + 1
print("vowels: ",c_vowels)
print("c_consonants: ",c_consonANTS)
print("c_digits: ",c_digits)