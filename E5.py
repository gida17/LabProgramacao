try:
    texto = open("E5.in","r")
    saida = open("E5.out","w")
    numeros = texto.read()
    texto.close()
    lista =[]
    quant = 0
    a =[]
    b = []
    cont = 0
    
    numeros = numeros.split("\n")
    quant = int(numeros[0])
    for x in numeros[1::]:
        temp = x.split(" ")
        a.append(int(temp[0]))
        b.append(int(temp[1]))   
            
    def f(n):
        global cont
        if n == 1:
            1
            cont += 1
            return
        if n%2 == 0:
            cont += 1
            f(n/2)
        if n%2 != 0:
            cont += 1
            f(3*n+1)

    for x in range(0,quant):
        for y in range (a[x],(b[x]+1)):
            f(y)
            lista.append(cont)
            cont = 0
        saida.write("Caso %d: %d\n" % (x+1,max(lista)))
        lista = []
        
except:
    print("Erro")
