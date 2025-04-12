print("LANCHONETE")
print("1- Coxinha R$5.00")
print("2- Pastel  R$7.00")
print("3- Café    R$4.00")
print("4- Suco    R$6.00")
print("5- SAIR "         )

total = 0

while True:
    item = int(input("Qual item gostaria de comprar? "))
    

    if(item == 1):
        qnt = int(input("Quantas unidades quer comprar? "))
        total = total + qnt * 5.00
    elif(item == 2):
        qnt = int(input("Quantas unidades quer comprar? "))
        total = total + qnt * 7.00
    elif(item == 3):
        qnt = int(input("Quantas unidades quer comprar? "))
        total = total + qnt * 4.00
    elif(item == 4):
        qnt = int(input("Quantas unidades quer comprar? "))
        total = total + qnt * 6.00
    elif(item == 5):
        break
    else:
        print("Produto inválido. Selecione outro")
print(f"\nO total a ser pago neste pedido é R${total} ")