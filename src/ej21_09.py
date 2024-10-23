def precio_entrada(edad):
    if edad < 4:
        print("entra gratis")
    elif edad <= 4 and edad < 18:
        print("paga 5€")
    elif edad >= 18:
        print("paga 10€")






def main():
    try:
        edad = int(input("Introduce tu edad: "))
        precio_entrada(edad)
    except ValueError:
        print("*ERROR*introduce numeros no letras")






if __name__ == "__main__":
    main()