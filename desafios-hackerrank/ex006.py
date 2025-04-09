import numpy as np
"""Você recebe uma matriz 2-D com dimensões N x M.Sua tarefa é executar a função min sobre o eixoe então encontre o máximo disso. Formato de entrada. A primeira linha de entrada contém os valores separados por espaços de N e M.
O próximo N linhas contém M inteiros separados por espaços.

Formato de saída

Calcular o mínimo ao longo do eixoe então imprima o máximo desse resultado."""

#N e M são linhas e colunas respectivamente
n = int(input("Digite o número de linhas da matriz: "))
m = int(input("Digite o número de colunas da matriz: "))

matriz = []

for i in range(n):
    linha = list(map(int,input(f"Digite os {m} números da linha {i + 1}, separados por espaço ").split()))
    while len(linha) != m:
        print("Quantidade de valores incorreta. Tente novamente")
        linha = list(map(int,input(f"Digite os {m} números da linha {i + 1}, separados por espaço ").split()))
    matriz.append(linha)

array = np.array(matriz)

minimos_linha = np.min(array, axis=1)
resultado_final = np.max(minimos_linha)
print("Os menores números de cada linha foram ", minimos_linha)
print("O maior entres esses menores valores é: ", resultado_final)


