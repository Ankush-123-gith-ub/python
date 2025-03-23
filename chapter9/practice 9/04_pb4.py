word="donkey"
with open("donkey.txt","r") as d:
    a=d.read()
newa=a.replace(word,"####")
with open("donkey.txt","w") as d:
    d.write(newa)
