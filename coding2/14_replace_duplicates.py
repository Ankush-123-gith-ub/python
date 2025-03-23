n = input()
c_vowel = 0
c_cons = 0
temp = "AEIOUaeiou"
for i in n:
    if i in temp:
        c_vowel += 1
    else:
        c_cons += 1
if c_vowel - c_cons == 0:
    print("Perfect Word Bheem.")
if c_vowel - c_cons > 0:
    print("Positive Word Kalia.")
if c_vowel - c_cons < 0:
    print("Negative Word Jerry.")