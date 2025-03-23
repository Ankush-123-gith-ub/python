n = input("Enter the message: ")
count_v = 0
count_s = 0
count_d = 0
vowel = "AEIOUaeiou"
for i in n:
    if i.isalpha():
        if i in vowel:
            count_v += 1
        else:
            count_s += 1
    elif i.isdigit():

        count_d += 1
print(f"Number of Vowels: {count_v}\nNumber of Consonants: {count_s}\nNumber of Digits: {count_d}")