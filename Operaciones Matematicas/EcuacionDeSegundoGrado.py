import math

a = float(input("Ingrese valor de a: "))
b = float(input("Ingrese valor de b: "))
c = float(input("Ingrese valor de c: "))
#Calculo la raiz cuadrada del discriminante
raiz_discriminante = math.sqrt(b*b-4*a*c)
#Se calcula x1 y x2
x1 = (-b + raiz_discriminante)/(2*a)
x2 = (-b - raiz_discriminante)/(2*a)
#Se muestran los resultados
print("Los valores de x1 y x2 son: ({},{})".format(x1,x2))