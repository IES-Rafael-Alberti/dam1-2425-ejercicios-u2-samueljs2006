# Lista original
a = [8, 3, 1, 19, 14]
print("Lista original:", a)


def imprimir_indices_y_valores(lista):
    """
    Imprime cada elemento de la lista y su índice.
    
    Args:
        lista (list): Lista de elementos a imprimir con sus índices.
    """
    print("\nÍndices y valores en la lista:")
    for indice, valor in enumerate(lista):
        print(f"Índice: {indice}, Valor: {valor}")


def ordenar_lista(lista):
    """
    Ordena la lista en orden ascendente sin modificar la lista original.
    
    Args:
        lista (list): Lista de elementos a ordenar.
    
    Returns:
        list: Lista ordenada en orden ascendente.
    """
    ordenada = sorted(lista)
    print("\nLista ordenada:", ordenada)
    return ordenada


def verificar_valores_fuera_de_rango(lista, min_valor=1, max_valor=20):
    """
    Verifica y muestra qué valores de la lista están fuera del rango especificado.
    
    Args:
        lista (list): Lista de elementos a verificar.
        min_valor (int): Valor mínimo del rango (incluido). Por defecto es 1.
        max_valor (int): Valor máximo del rango (incluido). Por defecto es 20.
    """
    print(f"\nVerificación de valores fuera del rango {min_valor}-{max_valor}:")
    for valor in lista:
        if valor < min_valor or valor > max_valor:
            print(f"Valor fuera de rango detectado: {valor}")
        else:
            print(f"Valor dentro del rango: {valor}")


def remover_duplicados(lista):
    """
    Elimina los valores duplicados en la lista.
    
    Args:
        lista (list): Lista de elementos de la cual eliminar duplicados.
    
    Returns:
        list: Lista sin elementos duplicados.
    """
    sin_duplicados = list(set(lista))
    print("\nLista sin duplicados:", sin_duplicados)
    return sin_duplicados


def buscar_valor(lista, valor):
    """
    Busca un valor específico en la lista e imprime si está presente.
    
    Args:
        lista (list): Lista en la que buscar el valor.
        valor (int): Valor a buscar en la lista.
    """
    if valor in lista:
        print(f"\nEl valor {valor} se encuentra en la lista.")
    else:
        print(f"\nEl valor {valor} no se encuentra en la lista.")


# Llamadas a las funciones con la lista original
imprimir_indices_y_valores(a)
ordenar_lista(a)
verificar_valores_fuera_de_rango(a)
remover_duplicados(a)
buscar_valor(a, 3)
