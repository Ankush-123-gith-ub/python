class demo:
    a=4
o=demo()
print(o.a) # print class attribute bcz an instance attribute is not present
o.a=0 # instance attribute
print(o.a) # it will print instance attribute bcz it is set
print(demo.a) # now it will print the class attribute 
              # bcz class atrribute doesn't change