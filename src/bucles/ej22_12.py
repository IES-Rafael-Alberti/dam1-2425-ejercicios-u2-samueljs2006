def contar_letra(frase, letra) :
    return frase.count(letra) 

def main():
    frase = input("Introduce una frase: ")
    letra = input("Introduce una letra: ")
    cantidad = contar_letra(frase, letra)
    print(f"La letra '{letra}' aparece {cantidad} veces en la frase.")

if __name__ == "__main__":
    main()