def pedir_edad(edad):
    if edad < 16:
        return False
    else:
        return True




def pedir_ingreso(ingreso):
    if ingreso >= 1000:
       return True
    else:
        return False







def main():
    edad = int(input("Introduce edad: "))
    ingreso = float (input("Cuanto ganas: "))
    if pedir_edad(edad) and pedir_ingreso(ingreso):
        print("si tributa")
    else:
        print("no tributa")





if __name__ == "__main__":
    main()