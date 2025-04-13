import math 
# Clase base que representa una calculadora simple (abstracción)
class Calculadora:
    def __init__(self):
        self.__resultado = 0  # atributo privado (encapsulamiento)
        self.operacion = ""

    def _mostrar_operacion(self, a, b): 
        return f"{self.operacion}: {a} y {b} = {self.__resultado}"
    
    def mostrar_operacion(self, a ,b):
        return f"\n{self._sumar()}n{self._restar()}\n{self._multiplicar()}\n{self._dividir()}"

    
    def sumar(self,a, b):
        self.operacion = "Suma "
        self.__resultado = a + b
        return self._mostrar_operacion(a,b)  
    
    def restar(self,a, b):
        self.operacion = "Resta "
        self.__resultado = a - b
        return self._mostrar_operacion(a,b)
    
    #def _multiplicar(self, a , b): #vr ing
        #return a * b 
    
    #def multiplicar(self,a, b): #vr ing
        #self.operacion = "multiplicar"
        #self.__resultado = self._multiplicar(a,b) 
        #return self._mostrar_operacion(a,b)
    
    def multiplicacion(self, a, b):
        self.operacion = "Multiplicar"
        self.__resultado = a * b
        return self._mostrar_operacion(a,b)
    
    def dividir(self,a, b):
        self.operacion = "Dividir"
        if b == 0:
            self.__resultado = a / b
            return self._mostrar_operacion(a,b)
        else:
            return "Error: Dividir entre cero no es posible"
    
    def mostrar_resultado(self,a, b):
        return f"El resultado de {self.operacion} entre {a} , {b} {self._resultado}"