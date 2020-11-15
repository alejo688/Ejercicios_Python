# Premisa de ejercicio 1
# Leer un número entero y mostrar todos los enteros comprendidos entre 1 y el número leído

def conteo(numero):
    numero += 1
    for i in range(1, numero):
        print(i)

if __name__ == "__main__":
    print("Bienvenido al programa de números enteros")

    numero = int(input("Ingrese un número igual o mayor a uno por favor: "))

    if numero < 1:
        while numero < 1:
            print("Error número no válido")
            numero = int(input("Ingrese un número igual o mayor a uno por favor: "))
            
        conteo(numero)
    else:
        conteo(numero)