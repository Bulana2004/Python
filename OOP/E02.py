class Temperature (object):
    def __init__(self, celsius, fahrenheit):
        self.celsius = celsius
        self.fahrenheit = fahrenheit

    def calculateFahrenheit(self):
        fahrenheit = (9/5 * self.celsius) + 32
        return fahrenheit

    def calculateCelsius(self):
        celsius = (self.fahrenheit - 32) * 5/9
        return celsius


celsius = int(input("Enter the celsius : "))
fahrenheit = int(input("Enter fahrenheight : "))
temperature = Temperature(celsius, fahrenheit)

print(f"Celsius to Fahrenheit = {temperature.calculateFahrenheit()}")
print(f"Fahrenheit to Celsius = {temperature.calculateCelsius()}")
