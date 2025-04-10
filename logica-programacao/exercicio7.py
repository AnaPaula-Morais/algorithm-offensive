
print("Olá seja muito bem vindo(a) a loja da Ana Morais!" )

total = float(input("Digite o valor do produto: "))
quantProduto = int(input("Digite a quantidade do produto: "))
total = total * quantProduto

if(total < 2500):
    print(f"Valor SEM deconto: R${total}")
    print(f"Valor COM desconto: R${total }. Só temos descontos para produtos acima de R$2500")
elif(total >= 2500 and total < 6000):
    desconto = total * (4 / 100)
    valorFinal = total - desconto
    print(f"Valor SEM desconto: R${total}")
    print(f"Valor COM desconto: R${valorFinal}")
elif(total >= 6000 and total < 10000):
    desconto = total * (7 / 100)
    valorFinal = total - desconto
    print(f"Valor SEM desconto: R${total}")
    print(f"Valor COM desconto: R${valorFinal}")
else:
    desconto = total * (11 / 100)
    valorFinal = total - desconto
    print(f"Valor SEM desconto: R${total}")
    print(f"Valor COM desconto: R${valorFinal}")
