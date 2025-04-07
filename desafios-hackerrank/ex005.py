"""O esboço de código incluído lerá um inteiro,, de STDIN.Sem usar nenhum método de string, tente imprimir o seguinte: 123...n
Observe que "..." representa os valores consecutivos entre eles.
Exemplo n = 5 saída 12345
Restrições: 1 <= n <= 150

"""
n = int(input("Digite um número entre 1 e 150: "))
for i in range(1, n +1):
    print(i, end="")