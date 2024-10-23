def pedir_edad() -> int:
    edad_incorrecta = False
    while not edad_incorrecta :
        try:
            edad= None
            edad = int(input("introduce edad: "))
            if edad < 0:
                raise ValueError("La edad debe ser un numero positivo")
            if edad == 0:
                raise ValueError("La edad debe ser un numero positivo mayor que cero")
            if edad > 125:
                raise ValueError("La edad debe ser un numero inferior o igual a 125")
            edad_incorrecta = True
        except ValueError as e:
            if edad is None:
                print(f"*ERROR* El numero introducido no es un numero entero valido")
            else:
                print(f"*ERROR* {e}. Intentalo de nuevo")
    return edad






def monstrar_años_cumplidos(edad: int):
    for i in range(1, edad + 1):
        if i == edad:
            print(i)
        else:
            print(i, end=",")





def main():
    edad = pedir_edad()
    print(f"Has cumplido los siguientes años:")
    monstrar_años_cumplidos(edad)




if __name__ =="__main__":
    main()