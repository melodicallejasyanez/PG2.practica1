import math
# Clase base que representa una calculadora simple (abstracción)
class Calculadora:
    def __init__(self, a, b):
        self.__resultado = 0  # atributo privado (encapsulamiento)
        self.a = a
        self.b = b
        self.operacion = ""
    
    def sumar(self):
        self.operacion = "Suma "
        self.__resultado = self.a + self.b
        return self._mostrar_operacion()  
    
    def restar(self):
        self.operacion = "Resta "
        self.__resultado = self.a - self.b
        return self._mostrar_operacion()  
    
    def multiplicar(self):
        self.operacion = "Multiplicación "
        self.__resultado = self.a * self.b  
        return self._mostrar_operacion() 
    
    def dividir(self):
        if self.b != 0:
            self.operacion = "División "
            self.__resultado = self.a / self.b
            return self._mostrar_operacion() 
        else:
            return "Error: División por cero"
        
    def _mostrar_operacion(self): 
        return f"{self.operacion}: {self.a} y {self.b} = {self.__resultado}"

calculadora_1 = Calculadora(15, 5)
calculadora_2 = Calculadora(15, 5)
calculadora_3 = Calculadora(15, 5)
calculadora_4 = Calculadora(15, 5)

# Probar la función de suma
print(calculadora_1.sumar())
print(calculadora_2.restar())
print(calculadora_3.multiplicar())
print(calculadora_4.dividir())
