# 1. Method Overloading using Default Arguments

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()

print(calc.add(5))        # one argument
print(calc.add(5, 10))    # two arguments
print(calc.add(5, 10, 15))# three arguments