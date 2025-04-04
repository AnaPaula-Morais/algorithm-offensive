"""Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa 60 reais por dia e 0,15 centavos porkm rodado. """

km_percorrido = int(input("Digite a distância percorrida em Km:"))
qnt_dias = int(input("Digite a quantide de dias que o carro ficou alugado:"))
valo_pagar = (km_percorrido * 0.15) + (60 * qnt_dias)
print(f"O valor a pagar é {valo_pagar}")