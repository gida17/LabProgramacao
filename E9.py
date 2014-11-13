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
            if len(valores) != 0:
                operacao = valores[0]
