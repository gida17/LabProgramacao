import sys

texto = open("E9.in","r")
saida = open("E9.out","w")
linhas  = texto.read()
texto.close()
linhas = linhas.split("\n")
valores = []
resultados = []

for linha in linhas:
    linha = linha.split(" ")
    linha = linha[::-1]
    for x in linha:
        if str(x).isdigit():
            valores.append(int(x))
        else:
            if str(x) == "+":                
                if len(valores) != 0:
                    resultados.append(valores[0] + valores [1])
                    del valores[0]
                    del valores[1]
                    
                elif len(valores) == 1:
                    resultados[-1] = resultados[-1] + valores [0]
                    del valores[0]
                    
                else:
                    resultados[-2] = resultados[-1] + resultados[-2]
                    del resultados [-1]
                    
            if str(x) == "-":                
                if len(valores) != 0:
                    resultados.append(valores[0] - valores [1])
                    del valores[0]
                    del valores[1]
                    
                elif len(valores) == 1:
                    resultados[-1] = resultados[-1] - valores [0]
                    del valores[0]
                    
                else:
                    resultados[-2] = resultados[-1] - resultados[-2]
                    del resultados [-1]
                    
            if str(x) == "*":                
                if len(valores) > 1:
                    resultados.append(valores[0] * valores [1])
                    del valores[0]
                    del valores[1]
                    
                elif len(valores) == 1:
                    resultados[-1] = resultados[-1] * valores [0]
                    del valores[0]
                
                else:
                    resultados[-2] = resultados[-1] * resultados[-2]
                    del resultados [-1]
                    
            if str(x) == "/":                
                if len(valores) != 0:
                    resultados.append(valores[0] / valores [1])
                    del valores[0]
                    del valores[1]
                    
                elif len(valores) == 1:
                    resultados[-1] = resultados[-1] / valores [0]
                    del valores[0]
                    
                else:
                    resultados[-2] = resultados[-1] / resultados[-2]
                    del resultados [-1]
                    
    saida.write("%d\n" %(resultados[0]))
