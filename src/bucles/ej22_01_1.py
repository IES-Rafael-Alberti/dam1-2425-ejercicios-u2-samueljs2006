# En este codigo si me funciona el pytest en el ej22_01.py no me funciono 
def monstra_mas_veces(palabra):
    return [palabra for _ in range(10)]

def main():
    palabra = input("Introduce una palabra: ")
    palabras_repetidas = monstra_mas_veces(palabra)
    for palabra in palabras_repetidas:
        print(palabra)

if __name__ == "__main__":
    main()
