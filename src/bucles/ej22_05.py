def capital_optenida(cantidad_a_inventir, interes_anual, num_años):
    capital = cantidad_a_inventir
    print("Año\tCapital")
    print("-----------------")
    for año in range(1, num_años + 1):
        capital *= 1 + interes_anual / 100
        print(f"{año}\t{capital:.2f}")




def main():
    cantidad_a_invetir = float(input("Cuanto vas a invertir: "))
    interes_anual = float(input("Cuanto interes anual: "))
    num_años = int(input("Cuantos años: "))
    capital_optenida(cantidad_a_invetir, interes_anual, num_años)




if __name__ == "__main__":
    main()