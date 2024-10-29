def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Comenzar programa")
    print("2. Imprimir listado")
    print("3. Finalizar programa")

def main():
    while True:
        mostrar_menu()  
        opcion = input("Seleccione una opción (1, 2 o 3): ")  
        
        if opcion == '1':
            print("Programa comenzado.")
        elif opcion == '2':
            print("Imprimiendo listado...")
        elif opcion == '3':
            print("Finalizando el programa...")
            break  
        else:
            print("Opción incorrecta. Por favor, elija 1, 2 o 3.")


if __name__ == "__main__":
    main()
