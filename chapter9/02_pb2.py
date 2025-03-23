import random
def game():
    score=random.randint(1,96)
    print("You are playing the game")
    print(f"Your score is {score}")
    with open("hiscore.txt","r") as h:
        hiscore=h.read()
        if (hiscore != ""):
            hiscore=int(hiscore)
        else:
            hiscore=0
    if (score > hiscore):
        # write this hi score to the file
        with open("hiscore.txt","w") as h:
            h.write(str(score))
    return
    
game()
