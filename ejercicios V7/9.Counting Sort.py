def counting_sort(lista):
  minimo = min(lista)
  maximo = max(lista)
  rango = maximo - minimo + 1

  conteo = [0] * rango

  for numero in lista:
    conteo[numero - minimo] += 1

  i = 0
  for valor in range(minimo, maximo + 1):
    for _ in range(conteo[valor - minimo]):
      lista[i] = valor
      i += 1

  return lista

Datos = [9, 3 ,4 ,6, 5, 2, 8, 7]
print(counting_sort(Datos))