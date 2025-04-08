from Calculadora_poo import Calculadora

class CalculadoraCientifica (Calculadora):

    def __init__(self, numero):
        self.numero = numero
        super().__init__()
    def calcular(self):
        self._resultado = 1
        cont = 1
        while cont <= int(self.numero):
            self._resultado = self._resultado * cont
            cont += 1
        return self.mostrar_resultado()
    def mostrar_resultado(self):
        return f"El factorial de {self.numero} es {self._resultado}"