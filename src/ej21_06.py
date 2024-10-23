def tu_nombre(): 
    return input("Cual es tu nombre :").upper()



def cual_sexo():
    return input("que sexo eres hombre/mujer: ").lower()






def main():
    nombre = tu_nombre()
    sexo = cual_sexo()
    if  sexo == "mujer" and nombre[0] < "M":
        print("grupo A es mujer")
    elif  sexo == "hombre" and nombre[0] > "N": 
        print("grupo A es hombre")
    else:
        print("grupo B")







if __name__ =="__main__":
    main()