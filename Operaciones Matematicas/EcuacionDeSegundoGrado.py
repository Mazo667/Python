import math

a = float(input("Ingrese valor de a: "))
b = float(input("Ingrese valor de b: "))
c = float(input("Ingrese valor de c: "))
#Calculo la raiz cuadrada del discriminante
r2= b**2 - 4*a*c
if(r2 > 0):
    print("Raices reales y diferentes: ")
    x1 = (-b + math.sqrt(r2))/2/a
    x2 = (-b - math.sqrt(r2))/2/a
    print (x1 +" "+x2)
if(r2 == 0):
    print("Raices Reales e iguales: ")
    x1 = -b /2/a
    x2 = x1
    print(x1 + " " + x2)
if(r2 < 0):
    print("Raices Complejas y conjugadas: ")
    x1_parteReal = -b/2/a
    x1_parteIma = math.sqrt(-r2)/2/a
    x2_parteReal = -b/2/a
    x2_parteIma = -math.sqrt(-r2)/2/a
    print("x1 y x2 Reales: ({},{})".format(x1_parteReal,x2_parteReal))
    print("x1 y x2 Imaginarios: ({},{})".format(x1_parteIma,x2_parteIma))
