def ordenamiento_por_seleccion(lista):
  
  for i in range(len(lista)):
    indice_minimo = i
    for x in range(i + 1, len(lista)):
      if lista[x] < lista[indice_minimo]:
        indice_minimo = x

    if indice_minimo != i:
      lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]

  return lista

lista_desordenada = [5, 2, 4, 1, 3]
lista_ordenada = ordenamiento_por_seleccion(lista_desordenada)
print(f"Lista desordenada: {lista_desordenada}")
print(f"Lista ordenada: {lista_ordenada}")