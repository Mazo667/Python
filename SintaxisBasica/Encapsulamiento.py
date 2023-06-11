class Ejemplo:
    __atributoPrivado = "Soy un atributo encapsulado"
    atributoPublico = "Soy un atributo publico"

    def __metodoPrivado(self):
        print("Soy un metodo inalcanzable desde afuera")

    def atributoPrivado(self):  #EL metodo publico retorna al atributo encapsulado
        return self.__atributoPrivado
    
    def metodoPublico(self):
        return self.__metodoPrivado()   #El metodo publico retorna el metodo Encapsulado
    

miClase = Ejemplo()
print(miClase.atributoPublico)
miClase.metodoPublico()
