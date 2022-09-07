#Faça um programa que calcule o aumento de um salário.
#Ele deve solicitar o valor do salário e a porcentagem do aumento.
# Exiba o valor do aumento e do novo salário.

salario = float(input("Salario: "))
porcentagem = float(input("Porcentagem do Aumento: "))

aumento = porcentagem * 10
aumento_real = salario + aumento
print(aumento)
print(aumento_real)