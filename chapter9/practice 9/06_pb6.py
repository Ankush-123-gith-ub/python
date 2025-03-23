word="python"
with open("log.txt") as l:
    a=l.read()
if word in a:
    print("true")
else:
    print("false")