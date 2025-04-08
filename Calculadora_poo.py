import math 
# Clase base que representa una calculadora simple (abstracción)
class Calculadora:
    def __init__(self, a, b):
        self.__resultado = 0  # atributo privado (encapsulamiento)
        self.operacion = ""

    def _mostrar_operacion(self): 
        return f"{self.operacion}: {self.a} y {self.b} = {self.__resultado}"
    
    def mostara_operacion(self):
        return f"\n{self._sumar()}n{self._restar()}\n{self._multiplicar()}\n{self._dividir()}"

    
    def sumar(self,a, b):
        self.operacion = "Suma "
        self.__resultado = a + b
        return self._mostrar_operacion(a,b)  
    
    def restar(self,a, b):
        self.operacion = "Resta "
        self.__resultado = a - b
        return self._mostrar_operacion(a,b)
    
    def multiplicar(self,a, b):
        self.operacion = "Multiplicacion "
        self.__resultado = a * b  
        return self._mostrar_operacion(a,b)
    
    def dividir(self,a, b):
        self.operacion = "Division "
        self.__resultado = a / b
        return self._mostrar_operacion(a,b)
    
    def mostrar_resultado(self,a, b):
        return f"El resultado de {self.operacion} entre {a} , {b} {self._resultado}"