class NumeroNegativoError(Exception):
    pass

def mostrar_impares_hasta_n(n):
    impares = [str(i) for i in range(1, n + 1) if i % 2 != 0]
    return ", ".join(impares)

def main():
    try:
        numero = int(input("Introduce un número entero positivo: "))
        
        if numero < 0:
            raise NumeroNegativoError("No se permiten números negativos.")
        elif numero == 0:
            raise ValueError("El número debe ser mayor que cero.")
        
        print(mostrar_impares_hasta_n(numero))
    
    except NumeroNegativoError as e:
        print(f"Error: {e} no se puden numeros negativo")
    except ValueError as e:
        print(f"Error: {e} introduce un numero no una letra")


if __name__ == "__main__":
    main()







