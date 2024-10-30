def sumar_numeros():
    suma = 0
    while True:
        numero = int(input("Introduce un número entero (0 para terminar): "))
        if numero == 0:
            break
        suma += numero
    return suma

def main():
    resultado = sumar_numeros()
    print(f"La sumatoria de todos los números ingresados es: {resultado}")

if __name__ == "__main__":
    main()
