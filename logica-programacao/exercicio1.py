"""Desenvolva u  algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto a ser aplicado a ele. Calcule e exiba o valor do desconto e o preço final do produto"""

preco_produto = float(input("Digite o valor do produto:"))
percentual = float(input("Digite o desconto em porcentagem:"))
desconto = preco_produto * (percentual/100)
valor_com_desconto = preco_produto - desconto
print(f"O preço do produto é {preco_produto}. Desconto de {percentual}%")
print(f"Valor calculado de desconto: {desconto}. Valor final do produto:{valor_com_desconto}")
