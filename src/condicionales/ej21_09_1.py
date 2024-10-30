# En este codigo si me funciona el pytest en el ej21_09.py no me funciono 
def precio_entrada(edad):
    if edad < 4:
        return "entra gratis"
    elif edad < 18:
        return "paga 5€"
    else:
        return "paga 10€"





def main():
    try:
        edad = int(input("Introduce tu edad: "))
        precio_entrada(edad)
    except ValueError:
        print("*ERROR*introduce numeros no letras")






if __name__ == "__main__":
    main()