"""Deseamos calcular el interes simple y compuesto que ganara un capital a una tasa de 
interes dada en un periodo de n meses, su formula es
Interes Simple = capital * n * tasa de interes
Interes Compuesto = captial * (1 + tasa de interes)                         """

capital = float(input("Ingrese el capital: "))
tasa = float(input("Ingrese la tasa: "))
n = float(input("Ingrese el numero de meses: "))
#Interes Simple
int_simple = capital*n*tasa
#Interes Compuesto
int_com = capital*pow(1+tasa, n)
print("Interes Simple: %0.2f" %int_simple)
print("Interes Compuesto: %0.2f"%int_com)