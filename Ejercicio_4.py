# Premisa de ejercicio 4
# Leer dos números y mostrar todos los enteros comprendidos entre ellos.

if __name__ == "__main__":
    print("Bienvenido al programa de números")
    numero1 = int(input("Por favor ingrese el primero número: "))
    numero2 = int(input("Por favor ingrese el segundo número: "))

    if numero2 > numero1:
        for i in range(numero1, numero2 + 1):
            print(i)
    elif numero1 > numero2:
        for i in range(numero1, numero2 + 1, -1):
            print(i)
    else:
        print(numero1)

