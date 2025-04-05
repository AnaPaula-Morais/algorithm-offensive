"""O esboço de código fornecido lê dois inteiros de STDIN, a e b. Adicione código para imprimir três linhas onde:
    * A primeira linha contém a soma dos dois números.
    * A segunda linha contém a diferença dos dois números (primeiro - segundo).
    * A terceira linha contém o produto dos dois números.
     ex: a = 3 e b = 5
     resultado 8, -2, 15
    """

a = int(input("Digite um número inteiro: "))
b = int(input("Digite outro número inteiro: "))

soma = a + b
diferenca = a - b
produto = a * b

print(f"A soma dos números é {soma}")
print(f"A diferença dos número é {diferenca}")
print(f"O produto dos números é {produto}")