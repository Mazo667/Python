class MiClase:
    #Variable de Clase
    miVar = "Este valor es de la clase"

    def __init__(self,var):
        self.var = var

    #Metodo Estatico
    @staticmethod
    def metodoEstatico():
        print(MiClase.miVar)

    @property
    def metodoPublico(self):
        return self.var

clase1 = MiClase("Variable de Instancia")
clase1.metodoEstatico()
print(clase1.metodoPublico)