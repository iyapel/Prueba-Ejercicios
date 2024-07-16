def radix_sort(lista):
    numero_maximo = max(lista)
    exponente = 1
    while numero_maximo // exponente > 0:
        cubos = [[] for x in range(10)]
        for numero in lista:
            digito = (numero // exponente) % 10
            cubos[digito].append(numero)
        lista = []
        for cubo in cubos:
            lista.extend(cubo)

        exponente *= 10

    return lista

Mis_datos = [31,4325,535,767,323,434,1,2]

print(radix_sort(Mis_datos))