#link de la explicacion del codigo
#https://youtu.be/ggFE9DbX8HE

Palabra = input("Ingrese una palabra: ")

def es_palindromo(palabra):
    palabra = palabra.lower()
    if len(palabra) <= 1:
        return True
    else:
        if palabra[0] == palabra[-1]:
            return es_palindromo(palabra[1:-1])
        else:
            return False

if es_palindromo(Palabra):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")