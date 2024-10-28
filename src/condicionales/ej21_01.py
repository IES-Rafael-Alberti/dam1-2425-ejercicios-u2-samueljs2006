def es_mayor(edad):
    if edad < 18:
        print("eres menor de edad")
    else:
        print("eres mayor de edad")




def main():
    edad = int(input("introduze tu edad: "))

    es_mayor(edad)

    
if __name__ == "__main__":
    main()