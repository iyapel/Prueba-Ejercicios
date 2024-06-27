def modificar_lista(la_lista):
    la_lista.append(25)
    la_lista[1] = 10

# Crea la lista fuera de la función
mi_lista = [1, 2, 3]

# Llama a la función y pasa la lista como argumento
modificar_lista(mi_lista)

# Verifica los cambios
print(mi_lista)  # Salida: [1, 10, 3, "nuevo elemento"]