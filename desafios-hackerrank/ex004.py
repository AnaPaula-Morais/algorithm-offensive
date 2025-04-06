"""Um dia extra é adicionado ao calendário quase a cada quatro anos como 29 de fevereiro, e o dia é chamado de dia bissexto . Ele corrige o calendário para o fato de que nosso planeta leva aproximadamente 365,25 dias para orbitar o sol. Um ano bissexto contém um dia bissexto.No calendário gregoriano, três condições são usadas para identificar anos bissextos:
    *O ano pode ser dividido uniformemente por 4, é um ano bissexto, a menos que:
        **O ano pode ser dividido uniformemente por 100, NÃO é um ano bissexto, a menos que:
            ***O ano também é divisível por 400. Então é um ano bissexto.
Tarefa

Dado um ano, determine se é um ano bissexto. Se for um ano bissexto, retorne o Boolean True, caso contrário, retorne False.

Note que o stub de código fornecido lê de STDIN e passa argumentos para a is_leapfunção. É necessário apenas completar a is_leapfunção.
"""


def is_leap(year):
    leap = False
    
    if (year % 4 == 0 and year % 400 == 0 and year % 100 == 0 ):
        print(True)
    elif(year % 4 == 0 and year % 400 == 0 and year % 100 != 0):
        print(False)
    
    return leap

year = int(input("Digite um ano, para saber se é bissexto ou não: "))
print(is_leap(year))