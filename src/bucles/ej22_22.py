def contar_digitos(num):
    pares = 0
    impares = 0
    while num > 0:
        digito = num % 10  
        if digito % 2 == 0:
            pares += 1  
        else:
            impares += 1 
        num //= 10  
    return pares, impares

def main():
    total_pares = 0
    total_impares = 0

    while True:
        numero = int(input("Ingrese un número entero positivo (0 para terminar): ")) 
        
        if numero == 0: 
            break
        elif numero < 0:  
            print("Por favor, ingrese solo números enteros positivos.")
            continue  

        pares, impares = contar_digitos(numero) 
        print(f"Número: {numero} - Dígitos pares: {pares}, Dígitos impares: {impares}")
        
        total_pares += pares  
        total_impares += impares 

    print(f"\nTotal de dígitos pares leídos: {total_pares}")
    print(f"Total de dígitos impares leídos: {total_impares}")

if __name__ == "__main__":
    main()
