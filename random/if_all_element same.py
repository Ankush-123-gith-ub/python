def same(s):
    a = s[0] 
    if s.count(a) == len(s):
        return "Identity"
    else:
        return "Not Identity."
n = "bbbdd"
print(same(n))