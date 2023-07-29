class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

class Color:
    def __init__(self, color):
        self.color = color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        # super().__init__(lado)
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho
    
    
cuadrado1 = Cuadrado(5, 'rojo')
print(f'Cálculo área cuadrado: {cuadrado1.calcular_area()}')