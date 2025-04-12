print("Bem vindo(a) a loja de Gelados da Ana Morais")
print("------------------Cardápio------------------")
print("--------------------------------------------")
print("---| Tamanho | Cupuaçu (CP) | Açaí (AC) |---")
print("---|    P    |    R$ 9.00   | R$ 11.00  |---")
print("---|    M    |    R$ 14.00  | R$ 16.00  |---")
print("---|    G    |    R$ 18.00  | R$ 20.00  |---")
print("--------------------------------------------")



#loop principal 
while True:
    #a função upper converte a string para maiúscula
    saborDesejado = input("Entre com o sabor desejado (CP/AC): ").upper()
    if(saborDesejado != "CP" and saborDesejado != "AC"):
        print("Sabor inválido. Tente novamente")
        continue

    
    tamanhoDesejado = input("Entre com o tamanho desejado (P/M/G): ").upper() 

    if(tamanhoDesejado != "P" and tamanhoDesejado != "M" and tamanhoDesejado != "G"):
        print("Tamanho inválido. Tente novamente")
        continue
    
    nomeSabor = ""
    preco = 0
    total = 0
    #condição para calcular o valor
    if(saborDesejado == "CP"):
        nomeSabor = "Cupuaçu"
        if(tamanhoDesejado == "P"):
            preco = 9.00
        elif(tamanhoDesejado == "M"):
            preco = 14.00
        elif(tamanhoDesejado == "G"):
            preco = 18.00
    elif(saborDesejado == "AC"):
        nomeSabor = "Açai"
        if(tamanhoDesejado == "P"):
            preco = 11.00
        elif(tamanhoDesejado == "M"):
            preco = 16.00
        elif(tamanhoDesejado == "G"):
            preco = 20.00
    print(f"Você pediu um {nomeSabor} no tamanho {tamanhoDesejado}: R${preco: .2f} ")
    total += preco
    #loop para perguntar se deseja continuar o pedido
    while True:
        DesejaContinuar = input("Deseja mais alguma coisa? (S/N) ").upper()
        if(DesejaContinuar == "S"):
            break
        elif(DesejaContinuar == "N"):
            print(f"O valor total a ser pago é: R${total: .2f}")
            exit()
        else:
            print("Opção inválida digite S ou N")

