def cuenta_atras(num):
    atras = [str(i) for i in range(num, -1, -1)]
    print(", ".join(atras))






def main():
    num = int(input("Introduce un número entero positivo: "))
    if num >= 0:
        cuenta_atras(num)
    else:
        print("Por favor, introduce un número entero positivo.")


if __name__ == "__main__":
    main()