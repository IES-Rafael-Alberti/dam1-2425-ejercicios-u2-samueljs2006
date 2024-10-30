def imprimir_tabla(numero):
    print(f"\nTabla del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def main():
    for numero in range(1, 11):
        imprimir_tabla(numero)

if __name__ == "__main__":
    main()