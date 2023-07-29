import abc
from abc import ABC

# Declaramos nuestra clase
class Animal(ABC):
    
    # Primer método
    # Decorador para métodos absctractos
    @abc.abstractmethod 
    def setName(self, name):
        self.name = name
    
    # Segundo método
    # Decorador para métodos absctractos
    @abc.abstractmethod
    def getName(self):
        return self.name