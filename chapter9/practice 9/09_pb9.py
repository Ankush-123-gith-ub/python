with open ("file1.txt") as f1:
    a=f1.read()
with open ("file2.txt") as f2:
    b=f2.read()
if(a==b):
    print("yes both file content is same(identical).")
else:
    print("no both file content is not same(non-identical).")