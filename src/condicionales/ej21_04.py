def es_impar_o_par(num):
    if num % 2 == 0:
        return "Es par"
    elif num % 1 == 1:
        return "Es impar"






def main():
    num = int(input("Escribe un numero: "))
    es_impar_o_par(num)




if __name__ =="__main__":
    main()