def contadorRegresivo(numero):
    """Contador Regresivo de un numero mayor a 0"""
    if(numero >= 0):
        print(numero)
        contadorRegresivo(numero-1)
    
contadorRegresivo(5)