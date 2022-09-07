quantidade_dia = float(input("Quantidade de cigarros fumados por dia: "))
anos = float(input("Quantos anos de fumante: "))

quantidade_dia_minutos = quantidade_dia * 1440
morte = (quantidade_dia_minutos - 10)

print(morte)

