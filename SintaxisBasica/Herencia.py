class Persona:   #Clase Padre
    def __init__(self,nombre,id):
        self.nombre = nombre
        self.id = id

    def datosPersonales(self):
        print(f'Persona: {self.nombre} ID {self.id}')

miPersona = Persona('Raul',4497) #Instanciamos un empleado
miPersona.datosPersonales()

#AHORA CREAMOS OTRA CLASE HIJO LLAMADA EMPLEADO

class Empleado(Persona):    #De esta forma decimos que herede los atributos de la clase Persona
    def datosEmpleado(self,empresa):
        print(f'Empresa donde trabaja: {empresa}')

miEmpleado = Empleado('Pablo',1122)
miEmpleado.datosPersonales()
miEmpleado.datosEmpleado('Google')
