def borda(texto): 
    tamanho = len(texto)  
    if tamanho: 
        print('+', '-' * tamanho, '+')
        print('|', texto, '|')
        print('+', '-' * tamanho, '+')



borda("Ana Paula")
borda("Lógica de programação")