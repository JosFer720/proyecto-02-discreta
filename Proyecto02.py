"""

                                                     Documentación Interna - PROYECTO 02

    Nombre del Programa: Proyecto02.py

    Fin En Mente: Implementar el sistema criptográfico RSA a través de un programa de computadora escrito en Python.

    Programador: Diego Fabián Morales Dávila    | 23267
                 Erick Antonio Guerra Illescas  | 23208
                 José Fernando Ruiz Estrada     | 23065

    Lenguaje: Python 3.7

    Recursos: Ninguno

"""
import random

def criba(n):
    not_prime = set()
    primes = []
    for i in range(2, n):
        if i in not_prime:
            continue
        for j in range(i * 2, n, i):
            not_prime.add(j)
        primes.append(i)
    return primes

def generar_primo_azar(inferior, superior):
    if inferior < 2:
        inferior = 2
    primos = [p for p in criba(superior + 1) if p >= inferior]
    if not primos:
        raise ValueError("No hay números primos en el rango especificado.")
    return random.choice(primos)

def euclides_extendido(a, b):
    if b == 0:
        return a, 1, 0
    else:
        mcd, x1, y1 = euclides_extendido(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return mcd, x, y

def inverso_modular(a, m):
    mcd, x, y = euclides_extendido(a, m)
    if mcd != 1:
        return None
    else:
        return x % m

def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#Función para Generar llaves, pública y privada. Obtiene el rango superior e inferior para la generación de dos números primos (p y q). Devuelve la llave pública y privada, ambas como arreglos.
def generar_llaves(rango_inferior, rango_superior):

            #Generación de números primos con la función "generar_primos_azar".
            primo1 = generar_primo_azar(rango_inferior,rango_superior)
            primo2 = generar_primo_azar(rango_inferior,rango_superior)

            
            print(primo1, primo2)

            #Obtención de (n) para el módulo de la llave pública y privada.
            n = primo1 * primo2

            if (n < 65537):
                e = 17
            else:
                e = 65537

            #Calcular el totiente para calcular la clave (d) para la llave privada.
            phin = (primo1-1) * (primo2-1)

            #Obtener clave (d): e y phin deben ser coprimos. En caso de no serlo devuelve none.
            d = inverso_modular(e,phin)

            #Si no es posible obtener una clave (d) devuelve none.
            if (d == None):
                return None
            else:
                #De lo contrario, devuelve 2 arreglos con cada llave, pública y privada respectivamente.
                return [e, n], [d, n]


#Función Encriptar: Obtiene la llave pública y el valor que se desea encriptar (m). Devuelve la cifra ingresada original (c).
def encriptar(caracter, llave_publica):
    #print(llave_publica)
    c = ((caracter)**llave_publica[0]) % llave_publica[1]

    return c


#Función Desencriptar: Obtiene la llave privada y el valor que se desea desencriptar (c). Devuelve la cifra ingresada original (m).
def desencriptar(cifrado, llave_privada):
    #print(llave_privada)
    m = ((cifrado)**llave_privada[0]) % llave_privada[1]

    return m

def main():

    rango_inferior = int(input("Ingrese el rango inferior: "))
    rango_superior = int(input("Ingrese el rango superior: "))

    llave_publica, llave_privada = generar_llaves(rango_inferior,rango_superior)
    print (llave_publica, llave_privada)
    
    caracter = int(input("Ingrese un numero para encriptar: "))
    cifrado = encriptar(caracter, llave_publica)
    print("El número " + str(caracter) + " encriptado es: " + str(cifrado))


    mensaje_descifrado = desencriptar(cifrado, llave_privada)
    print("El número cifrado " + str(cifrado) + " desencriptado es: " + str(mensaje_descifrado))
    



main()