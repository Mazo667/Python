class Persona:  #CLASE PERSONA
    def __init__(self,nombre,apellido): #CONSTRUCTOR
        #ATRIBUTOS
        self.nombre = nombre    
        self.apellido = apellido

    def myfunc(self):   #METODO DE LA CLASE
        print("Hola yo soy "+self.nombre+" "+self.apellido)

usuario1 = Persona("Mario","Luis")
usuario1.myfunc()

#METODOS ESPECIALES
print(str(usuario1)) #Retorna una representacion en cadena leible
print(repr(usuario1)) #Retorna una representacion informativa para programadores
del(usuario1) #Elimina un objeto