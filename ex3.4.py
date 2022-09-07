#Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto.
#Considere que pagam imposto pessoas cujo salario é maior que R$ 1200,00.

salario = float(input("Seu salario: "))
if salario <= 1200.00:
    print("livre de imposto")
else:
    print("deve pagar")

