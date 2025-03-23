class Number:
    def __init__(self,n):
        self.n=n
        # print(self.n)
    def __add__(a,b):
        return a.n + b.n

n=Number(1)
m=Number(2)
print(n+m)