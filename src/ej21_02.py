id_contraseña = "123abc"

def comprobar_contraseña(contraseña: str ):
    if contraseña.lower() == id_contraseña.lower():
        print("correcta")  
    else:
        print("incorrecto")



def main():
    contraseña = input("Introduce contraseña: ")

    comprobar_contraseña(contraseña)


if __name__ == "__main__":
    main()