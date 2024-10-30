def es_mayor(edad):
    if edad < 18:
        return "eres menor de edad"
    else:
        return "eres mayor de edad"


def main():
    edad = int(input("introduce tu edad: "))
    print(es_mayor(edad))

if __name__ == "__main__":
    main()

    
