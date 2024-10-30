def generar_triangulo(n):
    for i in range(1, n + 1, 2): 
        for j in range(i, 0, -2):  
            print(j, end=" ")
        print()  

def main():
    numero = int(input("Ingrese un número entero: "))
    generar_triangulo(numero)


if __name__ == "__main__":
    main()