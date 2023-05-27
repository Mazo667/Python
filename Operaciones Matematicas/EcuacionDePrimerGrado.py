#Ecuacion de Primer Grado: ax+b = 0  la solucion es x = -b/a , lo cual requiere
#que a sea distinto de cero

a = float(input("Ingrese el valor de a: "))
b= float(input("Ingrese el valor de b: "))

if(a != 0):
    x = float(-b/a)
    print("El resultado es :",x)
else:
    print("El valor de a debe ser distinto a de cero")