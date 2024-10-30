def division(n1: int, n2: int) -> str:
    try:
        if n2 == 0:
            return "*ERROR* No se puede dividir entre 0"
        return str(n1 / n2)
    except ValueError:
        return "*ERROR* de conversión!"

def main():
    try:
        n1 = int(input("Introduce un numero: "))
        n2 = int(input("Introduce un numero: "))
        print(division(n1, n2))
    except ValueError:
        print("*ERROR* de conversión!")

if __name__ == "__main__":
    main()
