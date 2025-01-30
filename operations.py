import math

class Operations:
    def addition(self, a, b):
        return sum(a,b)
    def substraction(self,a,b):
        return a-b
    def multiplication(self,a,b):
        return a*b
    def int_division(self,a,b):
        if b != 0:
            return a//b
        return "Error: Division by Zero wach 3mrk 9riti lmath"
    def dec_div(self,a,b):
        if b != 0:
            return a/b
        return "Error: Division by Zero wach 3mrk 9riti lmath"
    def remainder(self,a,b):
        return a%b
    def power(self,a,b):
        return pow(a,b)
    def squareroot(self,a):
        return math.sqrt(a)
    def logarithm(self,a):
        return math.log(a)
    def expo(self, a):
        return math.exp(a)
    
    
operations = Operations()
    