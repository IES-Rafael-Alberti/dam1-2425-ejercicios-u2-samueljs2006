# Lista original
a = [8, 3, 1, 19, 14]

print("Lista original:", a)

# 1. Imprimir cada elemento de la lista y su índice
print("\nÍndices y valores en la lista:")
for enumerar, valor in enumerate(a):
    print(f"Índice: {enumerar}, Valor: {valor}")

# 2. Ordenar la lista para inspeccionar valores en orden
ordena = sorted(a)
print("\nLista ordenada:", ordena)

# 3. Buscar valores fuera de un rango esperado (ej. 1-20)
print("\nVerificación de valores fuera del rango 1-20:")
for valor in a:
    if valor < 1 or valor > 20:
        print(f"Valor fuera de rango detectado: {valor}")
    else:
        print(f"Valor dentro del rango: {valor}")

# 4. Remover duplicados en la lista (si los hubiera)
duplicado = list(set(a))
print("\nLista sin duplicados:", duplicado)

# 5. Buscar un valor específico (ej. 3)
valor_buscado = 3
if valor_buscado in a:
    print(f"\nEl valor {valor_buscado} se encuentra en la lista.")
else:
    print(f"\nEl valor {valor_buscado} no se encuentra en la lista.")
