f = open("file.txt")
data = f.read()
print(data)
f.close()

# Same data can we written using with statement like this :
with open("file.txt") as f:
    print(f.read())
# you don't have to close the file.