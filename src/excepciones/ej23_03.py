class NumeroInvalidoError(Exception):
    pass

def cuenta_atras(n):
    return ", ".join(str(i) for i in range(n, -1, -1))

def solicitar_numero():
    while True:
        try:
            numero = int(input("Introduce un número entero positivo: "))
            
            if numero < 0:
                raise NumeroInvalidoError("El número debe ser un entero positivo.")
            
            return numero
        
        except NumeroInvalidoError as e:
            print(f"Error: {e} no se puden numeros negativo")
        except ValueError:
            print("Error: Debes introducir un número entero válido.")

def main():
    numero = solicitar_numero()
    
    print(cuenta_atras(numero))

if __name__ == "__main__":
    main()
