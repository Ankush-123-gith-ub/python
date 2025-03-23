################## GUESS THE NUMBER ##################
from random import randint
a=randint(1,100)
nog=1
while(a!=0):
    n= int(input("Guess the number: "))
    if(n < a):
        print("Higher number plz.")
        nog+=1
       
    elif(n > a):
        print("Lower number plz.")
        nog+=1
    else:
        print(f"Yes the number is {a}.")
        break
      
print(f"You have guess the number in {nog} attempts.")   
