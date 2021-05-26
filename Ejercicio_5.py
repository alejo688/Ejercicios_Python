#Premisa del ejercicio 5
#Leer dos números y mostrar todos los números terminados en 4 comprendidos entre ellos.

def esTerminado4(numero):
    numeroTexto = str(numero)
    if numeroTexto.endswith("4"):
        print(numero)

def numeros(numero1, numero2):
    if numero2 > numero1:
        for i in range(numero1, numero2 + 1):
            esTerminado4(i)
    elif numero1 > numero2:
        for i in range(numero1, numero2 + 1, -1):
            esTerminado4(i)
    else:
        print(numero1)

if __name__ == "__main__":
    print("Bienvenidos al programa de números terminados en 4.")
    numero1 = int(input("Por favor ingrese el primer número: "))
    numero2 = int(input("Por favor ingrese el segundo número: "))

    numeros(numero1, numero2)