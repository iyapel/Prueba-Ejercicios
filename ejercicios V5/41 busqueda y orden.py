def busqueda_binaria(lista, valor):
  
  izquierda = 0
  derecha = len(lista) - 1
  medio = (derecha) // 2
  if izquierda > derecha:
    return -1
  if valor == lista[medio]: 
    return medio
  if lista[medio] < valor:
    derecha = medio + 1
    return busqueda_binaria(lista[izquierda:medio], valor)
  elif lista[medio] > valor:
    izquierda = medio - 1
    return busqueda_binaria(lista[medio:derecha], valor)
  else:
    return -1

lista = []
condicion = 1
while condicion == 1:
  dato = int(input("Ingrese un dato a la lista: "))
  lista.append(dato)
  condicion = int(input("¿Son todos los datos que quiere agregar a la lista? 1-NO 2-SI: "))
  
valor = int(input("Ingrese el valor que quiere buscar: "))

indice = busqueda_binaria(lista, valor)

if indice is None:
  print(f"El valor {valor} no está en la lista.")
else:
  print(f"El valor {valor} está en la posición {indice} de la lista.")
