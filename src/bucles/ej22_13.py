def eco():
    texto = ""
    while texto != "salir":
        texto = input("Escribe algo (o 'salir' para terminar): ")
        if texto.lower() == "salir":
            print("Programa terminado.")
        else:
            print(texto)

def main():
    eco()

if __name__ == "__main__":
    main()

