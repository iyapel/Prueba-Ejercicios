#link de la explicacion del codigo
#https://youtu.be/ggFE9DbX8HE

Palabra = input("Ingrese una palabra: ")
Auxiliar = Palabra.lower()

Resultado = False
Invertida = ""

for i in Auxiliar:
    for h in Auxiliar:
        Invertida = h + Invertida
        if Auxiliar == Invertida:
            Resultado = True
            
print(Resultado)