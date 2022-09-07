dias = float(input("Quantidade de Dias: "))
horas = float(input("Quantidade de Horas: "))
minutos = float(input("Quantidade de Minutos: "))
segundos = float(input("Quantidade em Segundos: "))

dia_segundo = dias * 86400
hora_segundo = horas * 3600
minuto_segundo = minutos * 60

total = dia_segundo + hora_segundo + minuto_segundo + segundos
print(total)

