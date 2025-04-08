from Calculadora_poo import Calculadora
from factorial import CalculadoraCientifica

print("Calculadora estandar")

calc = Calculadora()

print(calc.sumar(15, 5))
print(calc.restar(15, 5))
print(calc.multiplicar(15, 5))
print(calc.dividir(15, 5))  

print("Calculadora factorial")
calcF = CalculadoraCientifica(5)
print(calcF.calcular()) 