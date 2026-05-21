<div align="center">

# 🐍 Introducción al Desarrollo de Software con Python

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Status](https://img.shields.io/badge/Estado-Activo-brightgreen?style=for-the-badge) ![License](https://img.shields.io/badge/Licencia-MIT-blue?style=for-the-badge) ![Universidad](https://img.shields.io/badge/Proyecto-Acad%C3%A9mico-orange?style=for-the-badge)

<br/> <img src="https://media.giphy.com/media/coxQHKASG60HrHtvkt/giphy.gif" width="480" alt="Python coding"/> <br/>

> _"El código es como la poesía; debe ser claro, elegante y con propósito."_

<br/>

Un repositorio de introducción al desarrollo de software usando **Python** como lenguaje principal. Aquí encontrarás scripts sobre **condicionales**, **bucles** y **manejo de strings** con sus métodos más útiles.

</div>

----------

## 📋 Tabla de Contenido

-   [👥 Equipo](https://claude.ai/chat/5583c575-b195-49a5-8948-7ba65c977878#-equipo)
-   [✨ Características](https://claude.ai/chat/5583c575-b195-49a5-8948-7ba65c977878#-caracter%C3%ADsticas)
-   [📂 Estructura del Repositorio](https://claude.ai/chat/5583c575-b195-49a5-8948-7ba65c977878#-estructura-del-repositorio)
-   [🔍 Temas Cubiertos](https://claude.ai/chat/5583c575-b195-49a5-8948-7ba65c977878#-temas-cubiertos)
-   [🚀 ¿Cómo empezar?](https://claude.ai/chat/5583c575-b195-49a5-8948-7ba65c977878#-c%C3%B3mo-empezar)
-   [💡 Ejemplos de Código](https://claude.ai/chat/5583c575-b195-49a5-8948-7ba65c977878#-ejemplos-de-c%C3%B3digo)
-   [📌 Notas Finales](https://claude.ai/chat/5583c575-b195-49a5-8948-7ba65c977878#-notas-finales)

----------

## 👥 Equipo

Desarrollado con 💛 por estudiantes apasionados por la tecnología:

👤 Integrante

🌟 **Stefany Tangarife**

🌟 **Yoneibi Neira**

🌟 **Juan Esteban Palacios**

🌟 **Favio Naranjo**

🌟 **Leonardo Oyola**

</div>

----------

## ✨ Características

-   ✅ Scripts claros y bien comentados en español
-   ✅ Ejemplos prácticos de condicionales (`if`, `elif`, `else`)
-   ✅ Ejercicios con bucles (`for`, `while`)
-   ✅ Métodos de strings: `join()`, `split()`, `strip()`, `replace()`, `upper()`, `lower()`, y más
-   ✅ Código pensado para principiantes
-   ✅ Proyecto académico colaborativo
----------

## 🔍 Temas Cubiertos

### 🔀 Condicionales

<div align="center"> <img src="https://media.giphy.com/media/iIqmM5tTjmpOB9mpbn/giphy.gif" width="340" alt="Decision making gif"/> </div>

Concepto

Descripción

`if / elif / else`

Toma de decisiones básica

Operadores relacionales

`==`, `!=`, `>`, `<`, `>=`, `<=`

Operadores lógicos

`and`, `or`, `not`

Condicionales anidados

Evaluaciones dentro de evaluaciones

Expresión ternaria

`valor_si_verdadero if condición else valor_si_falso`

----------

### 🔁 Bucles

<div align="center"> <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExeDhxMHEweDdwYjUyMzRxbWhtenR0YnM4aDRhY2lqMXkxOHRvZHIzZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Rbst7XSD9K2dsazQTE/giphy.gif" width="340" alt="Loop gif"/> </div>

Concepto

Descripción

`for`

Iterar sobre secuencias

`while`

Repetir mientras se cumpla una condición

`break`

Salir del bucle

`continue`

Saltar a la siguiente iteración

`range()`

Generar rangos numéricos

`enumerate()`

Obtener índice y valor al mismo tiempo

----------

### 🔤 Manejo de Strings

<div align="center"> <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZG10MmZ6ZDhxZWx6eXI0MnMzYjQ1dmZyc3g2b2ozdDV3aXZxYnczdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/DbXSzkKLzy96e3uukf/giphy.gif" width="340" alt="Typing strings gif"/> </div>

Método

¿Qué hace?

`split()`

Divide un string en una lista

`join()`

Une elementos de una lista en un string

`strip()`

Elimina espacios al inicio y al final

`replace()`

Reemplaza una subcadena por otra

`upper()` / `lower()`

Convierte a mayúsculas o minúsculas

`find()` / `count()`

Busca y cuenta ocurrencias

`startswith()` / `endswith()`

Verifica cómo empieza o termina un string

`format()` / f-strings

Interpolación y formato de cadenas

----------

## 🚀 ¿Cómo empezar?

### Requisitos previos

-   Python 3.10 o superior → [Descargar Python](https://www.python.org/downloads/)
-   Un editor de código (recomendamos [VS Code](https://code.visualstudio.com/))

### Instalación

```bash
# 1. Clona el repositorio
git clone https://github.com/tu-usuario/intro-python.git

# 2. Entra a la carpeta
cd intro-python

# 3. ¡Ejecuta cualquier script!
python condicionales/basicos.py
python bucles/for_loop.py
python strings/split_join.py

```

> No se requieren librerías externas. Todo usa la librería estándar de Python. 🎉

----------

## 💡 Ejemplos de Código

### 🔀 Condicionales

```python
# Verificar si un número es positivo, negativo o cero
numero = int(input("Ingresa un número: "))

if numero > 0:
    print("✅ El número es positivo")
elif numero < 0:
    print("❌ El número es negativo")
else:
    print("⚪ El número es cero")

```

### 🔁 Bucles

```python
# Tabla de multiplicar con for y range
numero = 7
print(f"📊 Tabla del {numero}:")

for i in range(1, 11):
    resultado = numero * i
    print(f"  {numero} x {i:2} = {resultado}")

```

### 🔤 Manejo de Strings — `split()` y `join()`

```python
# split(): divide un string en partes
frase = "Python es poderoso, flexible y elegante"
palabras = frase.split(", ")
print(palabras)
# ['Python es poderoso', 'flexible', 'elegante']

# join(): une una lista en un string
lenguajes = ["Python", "JavaScript", "Kotlin", "Rust"]
resultado = " | ".join(lenguajes)
print(resultado)
# Python | JavaScript | Kotlin | Rust

```

### 🔤 Métodos adicionales de Strings

```python
texto = "   Hola, Mundo Python!   "

print(texto.strip())           # "Hola, Mundo Python!"
print(texto.strip().upper())   # "HOLA, MUNDO PYTHON!"
print(texto.strip().lower())   # "hola, mundo python!"
print(texto.strip().replace("Python", "Colombia"))  # "Hola, Mundo Colombia!"
print(texto.strip().count("o"))  # 3
print(texto.strip().startswith("Hola"))  # True

```

----------

## 📌 Notas Finales

> Este repositorio es un proyecto académico de introducción al desarrollo de software con Python. Está diseñado para quienes dan sus primeros pasos en programación y quieren aprender con ejemplos prácticos, claros.

<div align="center"> <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGludzdseDkxYTZlenM1eG5iOHk2YTczYXN1ZjV2Zzg4bXc3bjY4ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/m4jqqr0kXABqw5a4nb/giphy.gif" width="280" alt="Done gif"/>

----------

Hecho con ❤️ y mucho ☕

![Python](https://img.shields.io/badge/Made%20with-Python-3776AB?style=flat-square&logo=python&logoColor=white)

</div>
