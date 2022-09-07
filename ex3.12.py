#Escreva um programa que calcule o tempo de uma viagem de carro.
#Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

lugar_de_destino = input("Local de Destino: ")
distancia = float(input("Distancia a Percorrer em Kilometros: "))
velocidade = float(input("Velocidade Média Esperada em KM/H: "))

velocidade_media = distancia/velocidade
print(velocidade_media)