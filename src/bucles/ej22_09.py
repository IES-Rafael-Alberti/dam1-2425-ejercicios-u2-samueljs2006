def verificar_contraseña(contraseña_correcta):
    while True:
        contraseña = input("Introduce la contraseña: ")
        if contraseña == contraseña_correcta:
            print("Contraseña correcta.")
        else:
            print("Contraseña incorrecta. Inténtalo de nuevo.")

def main():
    contraseña_correcta = "contraseña"  
    verificar_contraseña(contraseña_correcta)

if __name__ == "__main__":
    main()
