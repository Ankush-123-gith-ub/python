n = input("Enter word: ")
vowel = "AEIOUaeiou"
new = []
for i in n:
    if i.lower() in vowel:
        if i.lower() not in new:
            new.append(i.lower())
print(new)
print(f"Count of unique vowels: {len(new)}")