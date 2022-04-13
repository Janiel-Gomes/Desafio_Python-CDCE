# TODO: Complete os espaços em branco com uma solução possível para o problema.
n = int(input()) #recebe os dados
for i in range(n): #percorre o numero N
    x, y = input().split() #recebe os dados de x e y na mesma linda
    teste = 0
    cont = 0
    if len(x) < len(y): #testa se X é menor que y, caso verdadeiro, ele diz que não encaixa
        print("nao encaixa")
    else: #se x não for menor que y ele entrar no else
        for j in range(len(y)): # j vai percorrer y
            teste -= 1 #teste = teste - 1
            if x[teste] == y[teste]: #compara se x[teste] é igual a y[teste]
                cont += 1 #caso seja cont = cont + 1
        if cont == len(y): # se cont for igual a o tamanho de y ele exibe encaixa se não for exibe não encaixa
            print("encaixa")
        else:
            print("nao encaixa")