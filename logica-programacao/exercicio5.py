"""Fça um algoritmo que receba três valores, representando os lados de um triangulo fornecidos pelo usuário. Verifique se os valores formam um triângulo como:
    equiláreto(três lado iguais)
    isóceles(dois lados iguais)
    escaleno(três lados diferentes)
    lembre-se de que para formar um triangulo, nenhum dos lados pode ser igual a zero e um dos lados não pode ser maior que a soma dos outros dois
"""

lado1 = int(input("Digite o valor do primeiro lado do triangulo: "))
lado2 = int(input("Digite o valor do segundo lado do triangulo: "))
lado3 = int(input("Digite o valor do terceiro lado do triangulo: "))

if((lado1 > 0 and lado2 > 0 and lado3 > 0) and (lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1)):
    if(lado1 != lado2 and lado1 != lado3 and lado2 != lado3):
        print("O triangulo é escaleto")
    else:
        if(lado1 == lado2 and lado2 == lado3):
            print("O triangulo é equilátero")
        else:
            print("O triangulo é isóceles")
else:
    print("Pelo menos um dos valores não serve para formar um triângulo")