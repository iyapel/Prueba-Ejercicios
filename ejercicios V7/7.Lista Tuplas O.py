def ordenar_por_segundo_coso(datos_usuario):
  n = len(datos_usuario)
  for i in range(n):
    for x in range(n - i - 1):
      if datos_usuario[x][1] > datos_usuario[x + 1][1]:
        datos_usuario[x], datos_usuario[x + 1] = datos_usuario[x + 1], datos_usuario[x]
  return datos_usuario

cantidad_tuplas = int(input("¿Cuántas tuplas desea ingresar?: "))
datos_usuario = []

for i in range(cantidad_tuplas):
  nombre = input(f"Ingrese el nombre para la tupla {i + 1}:")
  edad = int(input(f"Ingrese la edad para la tupla {i + 1}:"))
  datos_usuario.append((nombre, edad))

datos_ordenados = ordenar_por_segundo_coso(datos_usuario)

print("Lista ordenada por edad:")
for tupla in datos_ordenados:
  print(f"- {tupla}")
