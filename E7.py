import sys

texto = open("E7.in","r")
saida = open("E7.in","w")
numeros = texto.read()
texto.close()
numeros = numeros.split("\n")

caso = 0
repeticoes = int(numeros[0])
filaRegular = []
filaPreferencial = []

while repeticoes >= caso:
    for x in numeros[1::]:
        if str(x).isdigit():
            filaRegular = []
            filaPreferencial = []
            caso += 1
            saida.write("Caso %d:\n" %(caso))
        
        if not str(x).isdigit():
