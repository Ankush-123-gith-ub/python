words=["Donkey","Kutta","Kamina","Ullu"]
with open("words_censored.txt","r") as d:
    a=d.read()
for word in words:
    a=a.replace(word.lower(),"#"*len(word))
with open("words_censored.txt","w") as d:
    d.write(a)
