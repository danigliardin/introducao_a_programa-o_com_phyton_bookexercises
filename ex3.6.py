#Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado.
#Para ser aprovado, todas as médias do aluno devem ser maiores que 7.
#Considere que o Aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variaveis:
#matéria, matéria2 e matéria3.

materia1 = int(input("Media Materia 1 = "))
materia2 = int(input("Media Materia 2 = "))
materia3 = int(input("Media Materia 3 = "))

if materia1 and materia2 and materia3 >= 7:
    print("Aprovado")
else:
    print("Reprovado")