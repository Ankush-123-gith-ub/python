word="python"
lineno=1
with open("log.txt") as l:
    lines=l.readlines()
for line in lines:
    if word in line:
        print(f"python present in {lineno} line")
        break
    lineno+=1
else:
    print("it is not present")