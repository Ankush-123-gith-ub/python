def code_name(n):
    a = n.split()
    a[0] = a[0][0]
    print(".".join(a))
    return 0 
n = input()
code_name(n)
