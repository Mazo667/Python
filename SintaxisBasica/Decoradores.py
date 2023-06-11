"""Son una forma de modificar o mejorar una funcion sin cambiar su implementacion interna."""
"""Los decoradores son funciones que toman otra funcion como argumento y devuelven una funcion modificada a(b)->c"""

def funcion_a(funcion_b):
    def funcion_c():
        print("Antes de la ejecucion a decorar")
        funcion_b()
        print("Despues de la ejecucion de la funcion a decorar")
    return funcion_c

@funcion_a
def saludar():
    print("Hola")

saludar()