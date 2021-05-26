# Premisa de ejercicio 6
# Leer un número entero de tres dígitos y mostrar todos los enteros comprendidos entre 1 y cada uno de los dígitos.

def getDigits(numero):
    numeroTexto = str(numero)
    count = len(numeroTexto)

    return count

def validDigits(numero):

    while numero < 0:
        numero = int(input("El número debe ser mayor o igual a 1: "))

    while getDigits(numero) != 3:
        numero = int(input("La cantidad de digitos extacta es 3, por favor intente nuevamente: "))

    return numero

def rangoNumeros(numero):
    for i in range(1, numero + 1):
        print(i)

if __name__ == "__main__":
    print("Bienvenido al programa de rango de números de tres digitos")
    numero = int(input("Por favor ingrese el número: "))
    numero = validDigits(numero)
    
    rangoNumeros(numero)
