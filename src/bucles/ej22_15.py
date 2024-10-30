def suma_positivos():
    suma = 0  
    while True:
        numero = int(input("Ingrese un número entero (0 para terminar): "))  
        if numero == 0:  
            break
        if numero > 0:  
            suma += numero
            
    return suma

def main():
    resultado = suma_positivos()  
    print(f"La sumatoria de los números positivos ingresados es: {resultado}")

if __name__ == "__main__":
    main()
