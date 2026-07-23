class Calculator:
    def __init__(self, value):
        self.value = value

    # Help to print value insted of address
    def __repr__(self):
        return f"{self.value}"

    # Aerithmetic Operations
    def __add__(self, other):
        return Calculator(self.value + other.value)

    def __sub__(self, other):
        return Calculator(self.value - other.value)

    def __mul__(self, other):
        return Calculator(self.value * other.value)

    def __truediv__(self, other):
        return Calculator(self.value / other.value)

    def __pow__(self, other):
        return Calculator(self.value ** other.value)

    def __mod__(self, other):
        return Calculator(self.value % other.value)

    # Bitwise Operations
    def __lshift__(self, other):
        return Calculator(self.value << other.value)

    def __rshift__(self, other):
        return Calculator(self.value >> other.value)

    def __and__(self, other):
        return Calculator(self.value & other.value)

    def __or__(self, other):
        return Calculator(self.value | other.value)

    def __xor__(self, other):
        return Calculator(self.value ^ other.value)

    def __invert__(self):
        return Calculator(~self.value)

    # Comparation Operations
    def __lt__(self, other):
        return Calculator(self.value < other.value)

    def __le__(self, other):
        return Calculator(self.value <= other.value)

    def __eq__(self, other):
        return Calculator(self.value == other.value)

    def __ne__(self, other):
        return Calculator(self.value != other.value)

    def __gt__(self, other):
        return Calculator(self.value > other.value)

    def __ge__(self, other):
        return Calculator(self.value >= other.value)

while True:

    a = int(input("Enter 1st number : "))
    if a == 00:
        break
    b = int(input("Enter 2nd number : "))
    c = input("Enter operation you want to perform: ")

    x = Calculator(a)
    y = Calculator(b)

    # Aerithmetic
    if c == "+":
        print(x + y)

    elif c == "-":
        print(x - y)

    elif c == "*":
        print(x * y)

    elif c == "/":
        print(x / y)

    elif c == "**":
        print(x ** y)

    elif c == "%":
        print(x % y)

    # Bitwise

    elif c == "<<":
        print(x << y)

    elif c == ">>":
        print(x >> y)

    elif c == "&":
        print(x & y)

    elif c == "|":
        print(x | y)

    elif c == "^":
        print(x ^ y)

    elif c == "~":
        print(~x)
        print(~y)

    # Comparation 
    elif c == "<":
        print(x < y)

    elif c == "<=":
        print(x <= y)

    elif c == "==":
        print(x == y)

    elif c == "!=":
        print(x != y)

    elif c == ">":
        print(x > y)

    elif c == ">=":
        print(x >= y)