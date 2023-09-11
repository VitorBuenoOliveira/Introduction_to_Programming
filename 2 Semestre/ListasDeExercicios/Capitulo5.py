# Função para converter Celsius em Fahrenheit
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Receba a lista de temperaturas em Celsius separadas por espaços
celsius_lista = input("Digite as temperaturas em Celsius separadas por espaços: ").split()

# Converta e exiba as temperaturas em Fahrenheit
print("\nTemperaturas em Fahrenheit:")
for celsius in celsius_lista:
    celsius = float(celsius)
    fahrenheit = celsius_para_fahrenheit(celsius)
    print(f"{celsius}°C = {fahrenheit:.2f}°F")
