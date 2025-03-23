ch = input("Enter chr: ")
vow = "AEIOUaeiou"
for i in ch:
    if i.isalpha():
        if ch in vow:
            print("Vowel.")
        else:
            print("Consonant.")
    else:
        print("not an alphabet")
            
