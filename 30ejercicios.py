"""1. Escribir un programa que imprima por pantalla la frase “Hola, ya se
imprimir frases”."""

print(str("Hola, ya se imprimir frases"))

"""Escribir un programa que imprima por pantalla un número entero, por
ejemplo el 273, o el 597."""

print(int(273))

"""3. Escribir un programa que imprima por pantalla un número decimal, por
ejemplo el 3.5 o el 7.5"""

print(float(3.5))

"""4.Escribir un programa que imprima por pantalla la suma de 1234 y 532."""

print(int(1234) + int(532))

"""5. Escribir un programa que imprima por pantalla la resta de 1234 y 532."""

print(int(1234) - int(532))

"""6. Escribir un programa que imprima por pantalla la multiplicación de 1234
y 532."""

print(int(1234) * int(532))

"""7. Escribir un programa que imprima por pantalla la división de 1234 y
532."""

print(float(int(1234) / int(532)))

"""8. que imprima por pantalla los números del 1 al 3."""

for i in range(1, 4):
    print(i)

"""9. Escribir un programa que imprima por pantalla los números del 1 al 10 con while"""

i = 1
while i <= 10:
    print(i)
    i += 1

"""10. Escribir un programa que imprima por pantalla los números del 1 al 10.000  con do while"""

i = 1       
while True:
    print(i)
    i += 1
    if i > 10000:
        break

"""11. Escribir un programa que imprima por pantalla los números del 5 al 10"""

for i in range(5, 11):
    print(i)

"""12. Escribir un programa que imprima por pantalla los números del 5 al 15"""

for i in range(5, 16):
    print(i)

"""13. Escribir un programa que imprima por pantalla los números del 5 al 15000"""

for i in range(5, 15001):
    print(i)

"""14.Escribir un programa que imprima 200 veces la palabra “hola”. Nota: en el
código fuente que usted escriba debe figurar solamente una vez la palabra “hola”"""

for i in range(200):
    print("hola")

"""15.Escribir un programa que imprima por pantalla los cuadrados de los 30
primeros números naturales"""

for i in range(1, 31):
    print(i**2)

"""16.Escribir un programa que multiplique los 20 primeros número naturales
(1*2*3*4*5...)"""

multiplicacion = 1
for i in range(1, 21):
    multiplicacion *= i
print(multiplicacion)

"""17. Escribir un programa que sume los cuadrados de los cien primeros números
naturales, mostrando el resultado en pantalla"""

suma = 0
for i in range(1, 101):
    suma += i**2
print(suma)

"""18.Escribir un programa que lea un número entero desde teclado y realiza la
suma de los 100 número siguientes, mostrando el resultado en pantalla"""

numero = int(input("Ingrese un número entero: "))
suma = 0
for i in range(numero, numero + 100):
    suma += i
print(suma)

"""19.Escribir un programa que convierta de euros a dólares. Recibirá un número
decimal correspondiente a la cantidad en euros y contestará con la cantidad
correspondiente en dolares."""

euros = float(input("Ingrese la cantidad en euros: "))
dolares = euros * 1.11  # 1 euro = 1.11 dólares el dia de hoy :v
print(f"{euros} euros son {dolares} dólares")

""""20.Escribir un programa que calcule el área de un rectángulo del cual se le
proporcionará por el teclado su altura y anchura (números decimales)"""

altura = float(input("Ingrese la altura del rectángulo: "))
anchura = float(input("Ingrese la anchura del rectángulo: "))
area = altura * anchura
print(f"El área del rectángulo es: {area}")

"""21.Escribir un programa que lea dos números del teclado y diga cual es el
mayor y cual el menor"""

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
if numero1 > numero2:
    print(f"{numero1} es mayor que {numero2}")
elif numero1 < numero2:
    print(f"{numero2} es mayor que {numero1}")
else:
    print(f"{numero1} es igual a {numero2}")

"""22.Escribir un programa que lea un número entero por el teclado e imprima
todos los número impares menores que él"""

numero = int(input("Ingrese un número entero: "))
for i in range(1, numero, 2):
    print(i)

"""23.Implemente el algoritmo de Euclides para encontrar el gcd de dos número leídos
desde teclado"""
# gcd (máximo común divisor)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
print(f"El gcd de {a} y {b} es: {gcd(a, b)}")

"""24.Escriba un programa que lea los coeficientes a, b y c de una ecuación de segundo, y
estudie si tiene o no solución. En caso positivo, las soluciones se calcularán e
imprimirán en pantalla"""

import math
a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

if a == 0:
    print("No es una ecuación de segundo grado")
else:
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        print("No tiene solución real")
    elif discriminante == 0:
        x = -b / (2*a)
        print(f"La solución es: {x}")
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        print(f"Las soluciones son: {x1} y {x2}")

"""25.Pruebe la recursividad Escriba programas que calculen recursivamente las
funciones f actorial(n) y Ackermann(x, y)"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def ackermann(x, y):
    if x == 0:
        return y + 1
    elif x == 1:
        return y + 2
    elif x == 2:
        return 2 * y + 3
    elif x == 3:
        return 2**y - 3
    else:
        return ackermann(x - 1, ackermann(x, y - 1))
    
x = int(input("Ingrese un número para calcular su factorial: "))
print(f"El factorial de {x} es: {factorial(x)}")
x = int(input("Ingrese un número para calcular la función de Ackermann: "))
y = int(input("Ingrese otro número: "))
print(f"Ackermann({x}, {y}) = {ackermann(x, y)}")

"""26.Escriba un programa que lea tres números enteros positivos, y que calcule e imprima
en pantalla el menor y el mayor de todos ellos"""

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))
if numero1 < numero2 and numero1 < numero3:
    menor = numero1
elif numero2 < numero1 and numero2 < numero3:
    menor = numero2
else:
    menor = numero3
if numero1 > numero2 and numero1 > numero3:
    mayor = numero1
elif numero2 > numero1 and numero2 > numero3:
    mayor = numero2
else:
    mayor = numero3
print(f"El menor es: {menor}")
print(f"El mayor es: {mayor}")

"""27.Escriba un programa que lea temperaturas expresadas en grados Fahrenheit y las
convierta a grados Celsius mostrándola. El programa finalizará cuando lea un valor
de temperatura igual a 999. La conversión de grados Farenheit (F) a Celsius (C) está
dada por C = 5/9(F − 32)"""

def fahrenheit_a_celsius(f):
    return 5/9 * (f - 32)
temperatura = float(input("Ingrese la temperatura en grados Fahrenheit (999 para salir): "))
while temperatura != 999:
    celsius = fahrenheit_a_celsius(temperatura)
    print(f"{temperatura} grados Fahrenheit son {celsius} grados Celsius")
    temperatura = float(input("Ingrese la temperatura en grados Fahrenheit (999 para salir): "))

"""28.Implemente una sentencia switch que escriba un mensaje en cada caso. Inclúyala en
bucle de prueba for. Utilice también un break tras cada caso y pruébelo. Elimine el
break y vea qué ocurre"""

def switch_case(opcion):
    switcher = {
        1: "Opción 1",

        2: "Opción 2",
        
        3: "Opción 3",
    }
    return switcher.get(opcion, "Opción no válida")
for i in range(1, 5):
    print(switch_case(i))

"""29. Cuando se lee una entrada estándar, por lo general se alcanza el fin de archivo
cuando el usuario teclea CRTL-D, CRTL-Z, o algún otro carácter dependiente del
sistema. Descubra cuál es el adecuado en su sistema. Escriba un programa que lea
datos controlando el fin de la secuencia con la combinación adecuada"""

try:
    while True:
        dato = input("Ingrese un dato (CTRL+Z para salir): ")
        print(f"Usted ingresó: {dato}")
except EOFError:
    print("Fin de la secuencia de entrada")
    
"""30.Escriba un programa que use dos bucles for anidados y el operador de módulo (%)
para detectar e imprimir números primos"""

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
for i in range(2, 101):
    if es_primo(i):
        print(f"{i} es un número primo")

