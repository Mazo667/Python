def es_primo(numero):
    """Determina si un numero entero positivo es primo o no"""
    if(numero <= 1):
        return False
    else:
        cont = 0
        for i in range(2, numero+1):
            if(numero % i == 0):
                cont += 1
        if (cont == 1):
            return True
        else:
            return False

print(es_primo(5))