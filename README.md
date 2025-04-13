# Practica 1
## Descripción del proyecto 

El proyecto consiste en el desarrollo de una calculadora que combina operaciones matemáticas básicas y avanzadas, implementada utilizando principios de programación orientada a objetos. Incluye funcionalidades como suma, resta, multiplicación, división y cálculo de factoriales, distribuidas en diferentes módulos que trabajan de manera conjunta. Es una práctica diseñada para aplicar conceptos como herencia, encapsulamiento y polimorfismo en Python.

## Preparacion del entorno y ejecución
 1. Clonar el repositorio:
```bash 
git clone https://github.com/yefeza/pg2-practica1.git
cd pg2-practica1
```
2. Crear un entorno virtual:
```bash
python -m venv env
```
3. Activar el entorno virtual:
    En Windows:
```bash
.\env\Scripts\activate
```
4. Ejecutar el script:
```bash
python main.py
```
5. Desactivar el entorno virtual:
```bash
deactivate
```
## Inplementación de la calculadora estandar 

Permite realizar operaciones aritmeticas basicas como la SUMA, RESTA, MULTIPLICACION Y DIVISION.
Esta Calculadora tiene estas partes de procedimiento: 

```Python

import math 
class Calculadora:
    def __init__(self, a, b):

    def _mostrar_operacion(self): 
    
    def mostara_operacion(self):
    
    def sumar(self,a, b):
    
    def restar(self,a, b):
    
    def multiplicar(self,a, b):
    
    def dividir(self,a, b):
    
    def mostrar_resultado(self,a, b):

```
## Implementacion de la calculadora factorial 

Esta Calculadora extiende la funcionmalidad de la calculadora estandar añadiendo la capacidad de calcular el factorial de un número. Utiliza programación orientada a objetos para implementar esta funcionalidad, probablemente mediante una clase que hereda de la calculadora base.

Esta Calculadora Factorial tiene las siguiengtes partes de procedimiento:

```Python

from Calculadora_poo import Calculadora

class CalculadoraCientifica (Calculadora):

    def __init__(self, numero):

    def calcular(self):

    def mostrar_resultado(self):

```

# Principios de la PROGRAMACION ORIENTADA A OBJETOS y como se aplica

Este documento explica los conceptos fundamentales de la **Programación Orientada a Objetos (POO)** y cómo se aplican en el desarrollo de software.

## Principios Fundamentales

### 1. Abstracción
- Representa las características esenciales de un objeto, ocultando detalles innecesarios.
- **Ejemplo**: Una clase `Vehículo` que contiene atributos como `marca` y `modelo`.

### 2. Encapsulación
- Agrupa datos y métodos dentro de una clase, restringiendo el acceso directo a los atributos.
- **Ejemplo**: El atributo `saldo` de una clase `CuentaBancaria` es accesible solo mediante métodos como `depositar()` o `retirar()`.

### 3. Herencia
- Permite crear nuevas clases basadas en clases existentes, reutilizando y ampliando su funcionalidad.
- **Ejemplo**: Una clase `Coche` hereda de `Vehículo` y añade atributos específicos como `número de puertas`.

### 4. Polimorfismo
- Facilita que un método se comporte de distintas formas según el tipo de objeto.
- **Ejemplo**: El método `calcularArea()` puede implementarse de forma diferente en clases como `Cuadrado` y `Círculo`.

## Aplicación de la POO
- **Diseño modular**: Representa entidades como objetos para facilitar la organización del código.
- **Reutilización del código**: La herencia evita duplicar funcionalidades comunes.
- **Facilidad de mantenimiento**: La encapsulación permite modificar clases sin afectar otras partes del programa.
- **Escalabilidad**: Los sistemas basados en objetos se adaptan fácilmente a nuevos requerimientos.


# Diferencia entre la implementacion procedimental y orientada a objetos:

## Implementación Procedimental
Se basa en la ejecución de funciones o procedimientos que realizan tareas específicas de forma directa.

### Características
- **Estructura lineal**: El código está organizado en funciones independientes.
- **Separación de datos y funciones**: Los datos son procesados externamente por las funciones.
- **Ideal para problemas simples**: Recomendado para scripts o cálculos básicos.

## Implementación Orientada a objetos
Organiza el código en torno a objetos, los cuales combinan datos(atributos) y comportamientos (métodos) en una única unidad.

### Características
- **Modularidad**: El código se divide en clases y objetos.
- **Emcapsulamiento**: Los datos y métodos están protegidos dentro de los objetos.
- **Ideal para sitemas complejos**: Adecuado para aplicaciones escalables y estructuradas.

# LICENCIA DE PUBLICACION 

