#Escreva um programa para calcular a redução do tempo de vida de um fumante.
#Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
#Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá.
#Exiba o total em dias.

quantidade_dia = float(input("Quantidade de cigarros fumados por dia: "))
anos = float(input("Quantos anos de fumante: "))

quantidade_dia_minutos = quantidade_dia * 1440
morte = (quantidade_dia_minutos - 10)

print(morte)

