def analizar_frase(frase):
    palabras = frase.split()
    
    if not palabras:
        return None, 0

    palabra_mas_larga = max(palabras, key=len)
    cantidad_palabras = len(palabras)  

    return palabra_mas_larga, cantidad_palabras

def main():
    while True:
        frase = input("Ingrese una frase (o presione Enter para terminar): ")  
        
        if frase == "":  
            break

        palabra_mas_larga, cantidad_palabras = analizar_frase(frase)  

        # Imprimir los resultados
        if palabra_mas_larga is not None:
            print(f"La palabra más larga es: '{palabra_mas_larga}'")
            print(f"Cantidad de palabras: {cantidad_palabras}")
        else:
            print("No se ingresaron palabras.")


if __name__ == "__main__":
    main()
