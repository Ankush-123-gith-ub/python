def minion_game(string):
    vowel = "AEIOUaeiou"
    Kevin = 0
    Stuart = 0
    for i in range(len(string)):
        if string[i] in vowel:
            Kevin += (len(string)-i)
        else:
            Stuart += (len(string)-i)
    if Kevin > Stuart:
        print(f"Kevin {Kevin}")
    elif Stuart > Kevin:
        print(f"Stuart {Stuart}")
    else:
        print("Draw")
    
            