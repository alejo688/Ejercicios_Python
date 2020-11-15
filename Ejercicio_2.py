# Premisa de ejercicio 2
# Leer un número entero y mostrar todos los pares comprendidos entre 1 y el número leído.

def conteo(numero):
    for i in range(1, numero + 1):
        if i % 2 == 0:
            print(i)

if __name__ == "__main__":
    print("Bienvenido al programa de los números impares")
    numero = int(input("Por favor ingrese un número mayor o igual a 1: "))

    if numero < 1:
        while numero < 1:
            print("Error número no valido")
            numero = int(input("Por favor ingrese un número mayor o igual a 1: "))

        conteo(numero)
    else:
        conteo(numero)