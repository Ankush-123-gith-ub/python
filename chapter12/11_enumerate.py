l=[1,2,54,54,4]

# index=0
# for item in l:
#     print(f"The item number at {index} is {item}.")
#     index+=1
        
#        ^
#        |
#        | 
#    This can be simplified using enumerate func

for index,item in enumerate(l):
    print(f"The item number at {index} is {item}.")

                       