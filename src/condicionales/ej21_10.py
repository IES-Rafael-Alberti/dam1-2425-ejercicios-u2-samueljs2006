def mostrar_menu_ingredientes(ingredientes):
    """Muestra el menú de ingredientes y permite al usuario elegir uno."""
    for i, ingrediente in enumerate(ingredientes, 1):
        print(f"{i}. {ingrediente}")
    eleccion = int(input("Elige un ingrediente (ingresa el número correspondiente): "))
    return ingredientes[eleccion - 1]


def main():
    ingredientes_vegetarianos = ["Pimiento", "Tofu"]
    ingredientes_no_vegetarianos = ["Peperoni", "Jamón", "Salmón"]
    
    tipo_pizza = input("¿Quieres una pizza vegetariana? (sí/no): ").strip().lower()
    
    if tipo_pizza == "sí":
        print("Ingredientes vegetarianos disponibles:")
        ingrediente_elegido = mostrar_menu_ingredientes(ingredientes_vegetarianos)
        es_vegetariana = True
    elif tipo_pizza == "no":
        print("Ingredientes no vegetarianos disponibles:")
        ingrediente_elegido = mostrar_menu_ingredientes(ingredientes_no_vegetarianos)
        es_vegetariana = False
    else:
        print("Opción no válida.")
        return tipo_pizza

    tipo = "vegetariana" if es_vegetariana else "no vegetariana"
    print(f"\nTu pizza {tipo} llevará los siguientes ingredientes:")
    print(f"- Mozzarella\n- Tomate\n- {ingrediente_elegido}")
    





if __name__ =="__main__":
    main()