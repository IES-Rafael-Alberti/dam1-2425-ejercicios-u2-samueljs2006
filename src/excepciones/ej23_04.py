def solicitar_numero():
    try:
        # Solicitar al usuario un número entero
        numero = int(input("Introduce un número entero: "))
        print(f"Has introducido el número: {numero}")
    except ValueError as e:
        print("La entrada no es correcta")
        raise e

def main():
    try:
        solicitar_numero()
    except ValueError:
        print("Programa finalizado debido a una entrada incorrecta.")


if __name__ == "__main__":
    main()
