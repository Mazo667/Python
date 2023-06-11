"""Es una funcion que recibe multiples parametros y los transforma en iterable"""
def Suma(*numeros):
    Resultado = 0
    for numero in numeros:
        Resultado += numero
    print(Resultado)

Suma(2,5,7)
Suma(3,5)
Suma(2,8,56,32)