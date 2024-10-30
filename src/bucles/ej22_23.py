def contar_digitos(titulos):
    total_digitos = 0
    for titulo in titulos:
        total_digitos += sum(c.isdigit() for c in titulo)  
    return total_digitos

def main():
    lineas_completas = 0  
    titulos_actuales = []  

    while True:
        libro = input("Libro: ") 
        
        if libro == "*":  
            break
        elif libro == "/":  
            if titulos_actuales:  
                total_digitos = contar_digitos(titulos_actuales)  
                lineas_completas += 1  
                print(f"Línea completa. Aparecen {total_digitos} dígitos numéricos.")
                titulos_actuales = []  
            else:
                print("No se ingresaron títulos en esta línea.")  
        else:
            titulos_actuales.append(libro)  
    print(f"Fin. Se leyeron {lineas_completas} líneas completas.")

if __name__ == "__main__":
    main()
