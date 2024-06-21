#link de la explicacion del codigo
#https://youtu.be/ggFE9DbX8HE

Palabra = input("Ingrese una palabra: ")
Auxiliar = Palabra.lower()

def Resolver(Auxiliar):
    Invertida = Auxiliar[::-1]  # Invierte la cadena utilizando slicing
    if Invertida == Auxiliar:
        return True
    else:
        return False

Resultado = Resolver(Auxiliar)
print(Resultado)