def mayor_numero():
    mayor = None  
    while True:
        numero = int(input("Ingrese un número entero positivo (0 para terminar): "))  
        if numero == 0:  
            break
        if numero > 0:  
            if mayor is None or numero > mayor:  
                mayor = numero
            
    return mayor

def main():
    resultado = mayor_numero()  
    if resultado is not None:
        print(f"El mayor número ingresado es: {resultado}")
    else:
        print("No se ingresaron números positivos.")

if __name__ == "__main__":
    main()
