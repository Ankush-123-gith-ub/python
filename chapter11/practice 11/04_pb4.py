class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(a, b):
        return Complex(a.r + b.r, a.i + b.i)
    
    def __mul__(a, b):
        real_part = a.r * b.r - a.i * b.i
        imag_part = a.r * b.i + a.i * b.r
        return Complex(real_part, imag_part)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"
        
    

c1 = Complex(1, 2)
c2 = Complex(3, 4)
print(c1 + c2)
print(c1*c2)