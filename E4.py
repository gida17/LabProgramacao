# coding:utf-8

import time #coloca antes de depois para medir o tempo

try:
    t0 = time.clock()
    texto = open("E4.in","r")
    matriz = texto.read()
    texto.close()
    numeros = []
    somatoriaDasLinhas = []
    somatoriaDasColunas = []
    somatoriaDasDiagonais = []
    quantidade = 0
    cont = 0
    soma = 0

    matriz = matriz.split("\n")    

    quantidade = int(matriz[0])
    
    for x in matriz[1::]:
        x = x.split(" ")
        for y in x:
            numeros.append(int(y))
            
    for x in range(cont,(cont+quantidade),):
        for x in numeros[cont:(cont+quantidade):]:
            soma += x
        somatoriaDasLinhas.append(soma)
        soma = 0
        cont += quantidade
        
    cont = 0
        
    for x in range(0,quantidade,):
        for y in numeros[cont::quantidade]:
            soma += y
        somatoriaDasColunas.append(soma) 
        soma = 0
        cont += 1
        
    cont = 0
        
    for x in numeros[cont::quantidade+1]: 
        soma += x
        cont += quantidade
    somatoriaDasDiagonais.append(soma)
    
    soma = 0
    cont = 0
    
    numeros.reverse()
    
    for x in numeros[cont::quantidade+1]: 
        soma += x
        cont += quantidade
    somatoriaDasDiagonais.append(soma)
    
    if (somatoriaDasLinhas.count(somatoriaDasLinhas[0]) == quantidade) and (somatoriaDasColunas.count(somatoriaDasColunas[0]) == quantidade) and (somatoriaDasDiagonais.count(somatoriaDasDiagonais[0]) == 2):
        saida = open("E4.out","w")
        saida.write("%d\n" % (somatoriaDasLinhas[0]))
    else:
        saida = open("E4.out","w")
        saida.write("-1\n")
        
    t1 = time.clock()
    
    print(t1-t0)
        
except:
    print("Erro")
