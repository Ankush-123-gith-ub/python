# f = open("poem.txt")
with open("poem.txt") as f:
    poem=f.read()
a="twinkle"
if a in poem:
    print("Yes it contains the word twinkle")
else:
    print("NO it not contains the word twinkle")