def calcular_total():
    total = 0.0  # Inicializamos el total a 0
    while True:
        monto = float(input("Ingrese el monto de la compra (0 para terminar): "))  

        if monto == 0:  
            break
        elif monto < 0: 
            print("Monto negativo no válido. Por favor, ingrese un monto positivo o 0 para terminar.")
            continue  
        
        total += monto  
    
    if total > 1000:
        descuento = total * 0.10  
        total -= descuento  
        print(f"Se aplicó un descuento del 10%. Total después del descuento: ${total:.2f}")
    else:
        print(f"Total a pagar: ${total:.2f}")

def main():
    calcular_total()  


if __name__ == "__main__":
    main()
