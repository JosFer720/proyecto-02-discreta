#PROYECTO 02
#MATEMATICA DISCRETA 1 - 10
#FERNANDO RUIZ - 23065
#FABIAN MORALES -23---
#ERICK GUERRA - 23---

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

def main():
    while True:
        print("\nElige una opción:")
        print("1. Generar un número primo al azar dentro de un rango")
        print("2. Calcular el MCD de dos números")
        print("3. Calcular el inverso modular de dos números")
        print("4. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            try:
                inferior = int(input("Ingresa el límite inferior del rango: "))
                superior = int(input("Ingresa el límite superior del rango: "))
                primo = generar_primo_azar(inferior, superior)
                print(f"Número primo generado: {primo}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            try:
                a = int(input("Ingresa el primer número: "))
                b = int(input("Ingresa el segundo número: "))
                resultado_mcd = mcd(a, b)
                print(f"El MCD de {a} y {b} es: {resultado_mcd}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "3":
            try:
                a = int(input("Ingresa el número a: "))
                m = int(input("Ingresa el módulo m: "))
                inverso = inverso_modular(a, m)
                if inverso is not None:
                    print(f"El inverso modular de {a} mod {m} es: {inverso}")
                else:
                    print(f"No existe inverso modular para {a} mod {m}.")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "4":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida, intenta de nuevo.")

main()