def mostrar_letras_invertidas(palabra):
    for letra in palabra[::-1]: 
        print(letra)

def main():
    palabra = input("Introduce una palabra: ")
    mostrar_letras_invertidas(palabra)

if __name__ == "__main__":
    main()