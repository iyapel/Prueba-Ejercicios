#Link de la explicacion del codigo:
#https://youtu.be/fWP0CFsvB7Y

def encontrar_max_divisor_propio(numero, actual_divisor=1, valores=[]):
    
    if actual_divisor == numero:
        return max(valores) if valores else -1

    if numero % actual_divisor == 0:
        valores.append(actual_divisor)

    return encontrar_max_divisor_propio(numero, actual_divisor + 1, valores)

Numero = int(input("Ingrese un número: "))

resultado = encontrar_max_divisor_propio(Numero)

# Mostrar el resultado
print("El máximo divisor propio de", Numero, "es:", resultado)
