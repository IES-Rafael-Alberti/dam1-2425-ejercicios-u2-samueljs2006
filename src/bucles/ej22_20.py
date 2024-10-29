def buscar_letra_en_frase(frase, letra):
    for i, caracter in enumerate(frase):  
        if caracter == letra:
            print(f"¡Coincidencia encontrada en la posición {i}!")
            return  
        else:
            print(f"No hay coincidencia en la posición {i}.")
    
    print("La letra no se encontró en la frase.")  

def main():
    frase = input("Ingrese una frase: ")  
    letra = input("Ingrese una letra a buscar: ")  
    
    if len(letra) != 1:  
        print("Por favor, ingrese solo una letra.")
        return
    
    buscar_letra_en_frase(frase, letra) 

if __name__ == "__main__":
    main()
