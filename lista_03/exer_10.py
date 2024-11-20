
class Temperatura:
    def celsius_para_fahrenheit(self, celsius):

        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit

temperatura = Temperatura()

celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit = temperatura.celsius_para_fahrenheit(celsius)

print("Temperatura em Fahrenheit: " + str(fahrenheit))
