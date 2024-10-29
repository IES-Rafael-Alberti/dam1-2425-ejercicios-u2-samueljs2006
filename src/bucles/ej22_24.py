def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    cantidad_primos = 0  
    
    while True:
        numero = int(input("Ingrese un número mayor que 1 (0 para terminar): "))  
        
        if numero == 0:  
            break
        elif numero <= 1:  
            print("Por favor, ingrese un número mayor que 1.")
            continue 
        
        if es_primo(numero):
            cantidad_primos += 1 
    
    print(f"Se ingresaron {cantidad_primos} números primos.")

if __name__ == "__main__":
    main()
