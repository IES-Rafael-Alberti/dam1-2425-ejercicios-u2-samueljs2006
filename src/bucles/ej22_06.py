def triangulo(altura):
    for i in range(1, altura + 1):
        print('*' * i)

def main():
    altura = int(input("Introduce un número entero para la altura del triángulo: "))
    triangulo(altura)

if __name__ == "__main__":
    main()