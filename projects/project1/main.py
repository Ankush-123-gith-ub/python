"""
1:for water
-1:for snake
0:gun
"""
import random 
computer = random.choice([1,-1,0]) 
yours_choice =input("Enter Yours Choice: ")
youDict={"w":1,"s":-1,"g":0}
reversedict={1:"water",-1:"snake",0:"gun"}
you=youDict[yours_choice]
print(f"you have choosen: {reversedict[you]}\ncomputer choosed: {reversedict[computer]}")

if(computer == you):
    print("It's draw.")
else:
    if(computer == 1 and you == -1): # 1-(-1)=2
          print("You Win")
    elif(computer == -1 and you == 1): # -1-1=-2
          print("You Loose")
    elif(computer == 0 and you == 1): # 0-1=-1
          print("You Win")
    elif(computer == 1 and you == 0): # 1-0=1
          print("You Loose")
    elif(computer == -1 and you == 0): # -1-0=-1 
          print("You Win")
    elif(computer == 0 and you == -1): # 0-(-1)=1
          print("You Loose")
    else:
         print("Something Went Wrong.")
        

        



