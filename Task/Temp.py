class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        fahrenheit = (self.celsius * 9 / 5) + 32
        return fahrenheit


temp = Temperature(36)
print("Fahrenheit:", temp.to_fahrenheit())
