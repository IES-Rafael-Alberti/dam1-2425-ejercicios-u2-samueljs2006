def nivel(puntuacion):
    if puntuacion == 0.0:
        return f"nivel inaceptable {2400*puntuacion}"
    elif puntuacion == 0.4:
        return f"nivel aceptable {2400*puntuacion}"
    elif puntuacion >= 0.6:
        return f"nivel meritorio {2400*puntuacion}"








def  main():
    try:
        puntuacion= float(input("Introduce puntuacion:"))
        nivel(puntuacion)
    except ValueError:
        print("*ERROR*introduce numeros no letras")






if __name__ == "__main__":
    main()