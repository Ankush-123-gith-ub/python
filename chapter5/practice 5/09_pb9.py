### list can't be written in a set
s={1,2,3,4,"harry",[5,6]}
s.remove([5,6])
print(type(s))
print(s)