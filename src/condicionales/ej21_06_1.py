# En este codigo si me funciona el pytest en el ej21_06.py no me funciono 


def tu_nombre(): 
    return input("¿Cuál es tu nombre? ").strip().upper()

def cual_sexo():
    sexo = input("¿Qué sexo eres (hombre/mujer)? ").strip().lower()
    if sexo not in ["hombre", "mujer"]:
        print("Entrada no válida. Introduce 'hombre' o 'mujer'.")
        return cual_sexo()
    return sexo
def determinar_grupo(nombre, sexo):
    if sexo == "mujer" and nombre[0].upper() < "M":
        return "Grupo A (mujer)"
    elif sexo == "hombre" and nombre[0].upper() > "N": 
        return "Grupo A (hombre)"
    else:
        return "Grupo B"


def main():
    nombre = tu_nombre()
    sexo = cual_sexo()
    determinar_grupo(nombre,sexo)

if __name__ == "__main__":
    main()