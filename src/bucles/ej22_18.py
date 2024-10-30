def suma_digitos(numero):
    suma = 0  
    while numero > 0:
        digito = numero % 10 
        suma += digito  
        numero //= 10  
    return suma

def main():
    contador_pares = 0  
    while True:
        numero = int(input("Ingrese un número entero positivo (-1 para terminar): "))  
        if numero == -1: 
            break
        if numero < 0:
            print("Por favor, ingrese solo números enteros positivos.")
            continue
        suma = suma_digitos(numero)  
        print(f"La suma de los dígitos del número {numero} es: {suma}")
        
        if numero % 2 == 0:  
            contador_pares += 1 

    print(f"Se ingresaron {contador_pares} números pares.")

if __name__ == "__main__":
    main()
