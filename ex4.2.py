#Escreva um programa que pergunte a velocidade do carro de um usuário.
# Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o usuário foi multado.
# Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80km/h.

velocidade_carro = float(input("Qual a velocidade do carro em km/h?"))

if velocidade_carro > 80:
    print("Velocidade acima do limite de 80km/k, Multado!!!")
if velocidade_carro <= 80:
    print("Debtro do limite de 80km/h")