#Escreva um programa que converta uma temperatura digitada em Celsius em Fahrenheit.

temp_celsius = float(input("Escreva a Temperatura em Celsius: "))

temp_far = ((9 * temp_celsius)/(5)) + 32
print(temp_far, "Fahrenheit")