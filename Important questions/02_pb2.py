# import random
# def game():
#     score=random.randint(1,56)
#     print("You are playing the game")
#     print(f"Your score is {score}")
#     with open("hiscore.txt","r") as h:
#         content=h.read()
#         if content.isdigit():
#             hiscore=int(content)
#         else:
#             hiscore=score
#     if (score > hiscore or hiscore == ""):
#         # write this hi score to the file
#         with open("hiscore.txt","w") as h:
#             h.write(str(score))
#     return hiscore
# game()
import random

def game():
    # Ensure the file exists
    open("hiscore.txt", "a").close()  # Create the file if it doesn't exist

    score = random.randint(1, 56)  # Generate a random score
    print("You are playing the game")
    print(f"Your score is {score}")

    # Read the high score from the file
    with open("hiscore.txt", "r") as h:
        content = h.read().strip()  # Remove extra spaces or newlines
        if content.isdigit():  # Check if content is a valid integer
            hiscore = int(content)
        else:
            hiscore = score  # Default to current score if file is empty or invalid

    # Update the high score if the new score is higher
    if score > hiscore:
        with open("hiscore.txt", "w") as h:  # Overwrite with the new high score
            h.write(str(score))
        print("New high score achieved!")
    else:
        print("Try again to beat the high score!")

    return hiscore

# Run the game
game()