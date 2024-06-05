Palabra = input("Ingrese una palabra: ")
Auxiliar = Palabra.lower()

Resultado = False

Invertida = ""

for i in Palabra:
    for h in Palabra:
        Invertida = h + Invertida
        if Palabra == Invertida:
            Resultado = True
            
print(Resultado)    
