import sys

try:
    texto = open(sys.argv[1], "r")
    saida = open(sys.argv[2], "w")
    numeros = texto.read()
    texto.close()
    quant = numeros.count("\n")
    a = []
    b = []
    saldo = []
    sequencia = []
    inicio = 0
    diferenca = 0
    maximo = 0
    
    if quant % 2 != 0:
        quant += 1
        
    quant = int(quant / 2)
        
    numeros = numeros.split("\n")
        
    for x in numeros[::]:
        if " " in x:
            temp = x.split(" ")
            a.append(int(temp[0]))
            b.append(int(temp[1]))
        else:        
            saldo.append(x)
            
    temp = []
    
    for x in range(0, quant):
        diferenca = a[x] - b[x]
        for y in saldo[x]:
            temp.append(int(y))
        for y in range(0, diferenca):
            for w in temp:
                if w > maximo:
                    maximo = w
            sequencia.append(maximo)
            temp.remove(maximo)
            maximo = 0
        temp = []
           
    for x in range(0, quant):
        for y in saldo[x]:
            temp.append(int(y))
            
    for x in range(0, quant):
        diferenca = a[x] - b[x]
        for y in range(0, diferenca - 1):
            if len(sequencia) > 1:
                if temp.index(int(sequencia[y])) > temp.index(int(sequencia[y + 1])):
                    sequencia[y], sequencia[y + 1] = sequencia[y + 1], sequencia[y]
                    
            else:
                saida.write(str(sequencia[0]))
                
        for y in range(0, diferenca):
            saida.write(str(sequencia[0]))
            del sequencia[0]
        
        for y in range(0, a[x]):
            del temp[0]
        
        saida.write("\n")
        
except:
    print("Erro")
