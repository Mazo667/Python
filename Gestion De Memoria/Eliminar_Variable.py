num1 = [1,2,3]
num2=num1 #num2 tiene la misma refenecia que num1
b = [True,False,num1] #b contiene una refencia a num1
del num1 #Eliminacion de la variable
print(num2)
#print(num1) lo tomara como error por que ya no existe