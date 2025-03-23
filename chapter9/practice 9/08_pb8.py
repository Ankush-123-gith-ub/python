with open("this.txt") as o:
    a=o.read()
with open("new_this.txt","w") as n:
    n.write(a)