"""O esboço de código fornecido lê dois inteiros, a e b, de STDIN.Adicione lógica para imprimir duas linhas. A primeira linha deve conter o resultado da divisão inteira,//. A segunda linha deve conter o resultado da divisão de ponto flutuante,/.Não é necessário arredondamento ou formatação.
    ex: a = 3 e b = 5
    resultado: 0 e 0.6
"""

a = int(input("Digite um número inteiro: "))
b = int(input("Digite outro número inteiro: "))

divisao_inteira = a // b
divisao_flutuante = a / b

print(f"O resultado da divisão inteira de {a} e {b} é  = {divisao_inteira}")
print(f"O resultado da divisão de ponto flutuante de {a} e {b} é = {divisao_flutuante}")