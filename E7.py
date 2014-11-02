import sys

texto = open(sys.argv[1], "r")
saida = open(sys.argv[2], "w")
numeros = texto.read()
texto.close()
numeros = numeros.split("\n")

caso = 0
repeticoes = int(numeros[0])
filaRegular = []
filaPreferencial = []

for x in numeros[1::]:
        if str(x).isdigit():
            filaRegular = []
            filaPreferencial = []
            caso += 1
            saida.write("Caso %d:\n" %(caso))
            repeticoes += 1
            
        
        if not str(x).isdigit():
            if x[0] is "f":
                filaRegular.append(x)
            if x[0] is "p":
                filaPreferencial.append(x)
                
            if x[0] is "A":
                if len(filaRegular) == 0:
                    if len(filaPreferencial) == 0:
                        None
                    else:
                        del filaPreferencial[0]
                else:
                    del filaRegular[0]
                    
            if x[0] is "B":
                if len(filaPreferencial) == 0:
                    if len(filaRegular) == 0:
                        None
                    else:
                        del filaRegular[0]
                else:
                    del filaPreferencial[0]
                    
            if x[0] is "I":
                if len(filaRegular) == 0:
                    saida.write("0 ")
                else:
                    saida.write("%s " %(filaRegular[0][2::]))
                    
                if len(filaPreferencial) == 0:
                    saida.write("0\n")
                else:
                    saida.write("%s\n" %(filaPreferencial[0][2::]))
