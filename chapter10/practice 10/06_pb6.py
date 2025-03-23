from random import randint
class train:
    def __init__(slf,trainNo):
        slf.trainNo=trainNo
    def book(self,fro,to):
        print(f"The ticket is booked in train no {self.trainNo} from {fro} to {to}.")
    def getStatus(self):
        print(f"The  train no {self.trainNo}  is running on time. ")
    def getFare(self,fro,to):
        print(f"Ticket fair is for train no {self.trainNo} from {fro} to {to} is {randint(22,999)}.")

t=train(21343454)
t.book("Rampur","Delhi")
t.getStatus()
t.getFare("Rampur","Delhi")