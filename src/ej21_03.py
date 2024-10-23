def division():
    try:
        n1= int(input("Introduce un numero: "))
        n2= int(input("Introduce un numero: "))
    except ValueError:
        print("*ERROR* de conversión!")
    else:
        if n2 == 0:
            print("*ERROR* No se puede dividir entre 0")
        else:
            print(n1/n2)

def main():
    division()



if __name__ =="__main__":
    main()