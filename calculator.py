import math

class Fraction:
    def __init__(self, num1, den1, num2, den2):
        self.num1 = num1
        self.den1 = den1
        self.num2 = num2
        self.den2 = den2

    def simplify(self, num, den):
        gcd = math.gcd(num, den)
        return f"{num // gcd}/{den // gcd}"

    def __add__(self):
        num = self.num1 * self.den2 + self.num2 * self.den1
        den = self.den1 * self.den2
        return self.simplify(num, den)

    def __sub__(self):
        num = self.num1 * self.den2 - self.num2 * self.den1
        den = self.den1 * self.den2
        return self.simplify(num, den)

    def __mul__(self):
        num = self.num1 * self.num2
        den = self.den1 * self.den2
        return self.simplify(num, den)

    def __truediv__(self):
        num = self.num1 * self.den2
        den = self.den1 * self.num2
        return self.simplify(num, den)

    def get_values(self):
        val1 = self.num1 / self.den1
        val2 = self.num2 / self.den2
        return val1, val2
    def __eq__(self, other=None):
        val1, val2 = self.get_values()
        return val1 == val2

    def __lt__(self, other=None):
        val1, val2 = self.get_values()
        return val1 < val2

    def __le__(self, other=None):
        val1, val2 = self.get_values()
        return val1 <= val2

    def __gt__(self, other=None):
        val1, val2 = self.get_values()
        return val1 > val2

    def __ge__(self, other=None):
        val1, val2 = self.get_values()
        return val1 >= val2

# Testing
f = Fraction(1, 2, 1, 3)
print("Add:       ", f.__add__())
print("Subtract:  ", f.__sub__())
print("Multiply:  ", f.__mul__())
print("Divide:    ", f.__truediv__())
print("Equal:     ", f.__eq__())
print("Less than: ", f.__lt__())
print("Greater:   ", f.__gt__())
