sentence1=input("Enter the snetence: ")
sentence2=input("Enter the line to check: ")
if (sentence2 in sentence1):
    print("Spam detcted.")
else:
    print("Not a spam")