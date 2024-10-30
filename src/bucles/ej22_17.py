def suma_digitos(numero):
    suma = 0  
    while numero > 0:
        digito = numero % 10  
        suma += digito  
        numero //= 10  
    return suma

def main():
    numero = int(input("Ingrese un número entero positivo: ")) 
    if numero < 0:
        print("Por favor, ingrese un número entero positivo.")
        return
    resultado = suma_digitos(numero) 
    print(f"La suma de los dígitos del número {numero} es: {resultado}")

if __name__ == "__main__":
    main()
