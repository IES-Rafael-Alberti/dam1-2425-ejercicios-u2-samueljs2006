def tipo_de_impositivo(renta):
    if renta < 10000 :
      print("tipo de impositivo 5%") 
    elif renta <= 10000  and renta < 20000:
      print("tipo de impositivo 15%")
    elif renta <= 20000 and renta < 35000:
       print("tipo de impositivo 20%")
    elif renta <= 35000 and renta < 60000:
       print("tipo de impositivo 30%")
    elif renta >= 60000:
       print("tipo de impositivo 45%")
      
      



def main():
    try:
        renta = int(input("introduce tu renta: "))
        tipo_de_impositivo(renta)
    except ValueError:
       print("*ERROR*introduce numeros no letras")






if __name__ == "__main__":
    main()