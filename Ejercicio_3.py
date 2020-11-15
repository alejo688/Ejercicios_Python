# Premisa de ejercicio 3
# Leer un número entero y mostrar todos los divisores exactos del número comprendidos entre 1 y el número leído.

def conteo(numero):
    for i in range(1, numero + 1):
        print(numero/i)

if __name__ == "__main__":
    print("Bienvenido al programa de divisores")
    numero = int(input("Ingrese un número mayor o igual a 1: "))

    if numero < 1:
        while numero < 1:
            print("Error, número no valido")
            numero = int(input("Ingrese un número mayor o igual a 1: "))
        conteo(numero)
    else:
        conteo(numero)