print("---WHILE (se repite un bloque mientras la condición sea verdadera)")
contador = 0
while contador < 5:
    print(contador)
    contador +=1 #Output: 0 1 2 3 4



print("---ELSE (se ejecuta un bloque de código cuando la condición ya no devuelve true)")
contador = 0
while contador < 5:
    print(contador)
    contador +=1
else:
    print("dejo de contar") #Output: 0 1 2 3 4 dejo de contar



print("---BREAK (rompe la ejecución del while en cualquier momento)")
contador = 0
while contador < 5:
    contador +=1
    print(contador)
    if (contador == 4):
        print("Se ejecuto Break y el bucle termina")
        break
#Output: 1 2 3 4 Se ejecuto Break y el bucle termina



print("---CONTINUE")
contador = 0
while contador < 5:
    contador +=1
    print(contador)
    if(contador==3):
        continue #Output: 1 2 3 4 5