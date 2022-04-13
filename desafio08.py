x = int(input())
n= list()

#TODO: Complete os espaços em branco com uma solução possível para o problema.
for i in range (10):
    n.append( x )
    x = x * 2
    print("N[{}] = ".format(i), n[i])