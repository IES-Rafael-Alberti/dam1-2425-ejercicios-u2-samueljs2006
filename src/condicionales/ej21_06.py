def tu_nombre(): 
    return input("Cual es tu nombre :").upper()



def cual_sexo():
    return input("que sexo eres hombre/mujer: ").lower()


def determinar_grupo(nombre, sexo):
    if  sexo == "mujer" and nombre[0] < "M":
        return "Grupo A (mujer)"
    elif  sexo == "hombre" and nombre[0] > "N": 
        return "Grupo A (hombre)"
    else:
        return "grupo B"



def main():
    nombre = tu_nombre()
    sexo = cual_sexo()
    determinar_grupo(nombre, sexo)


if __name__ =="__main__":
    main()