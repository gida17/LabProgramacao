import sys

texto = open("E6.in","r")
saida = open("E6.out","w")
numeros = texto.read()
texto.close()
quant = numeros.count("\n")
a = []
b = []
saldo = []
inicio = 0

if quant%2 != 0:
    quant += 1
    
quant = int(quant/2)
    
numeros = numeros.split("\n")
    
for x in numeros[::]:
    if " " in x:
        temp = x.split(" ")
        a.append(int(temp[0]))
        b.append(int(temp[1]))
    else:        
        saldo.append(int(x))
temp = []
