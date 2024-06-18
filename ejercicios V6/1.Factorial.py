#explicacion del codigo:
#https://youtu.be/8FzEhlt6fk4

Valor_Ingresado = int(input("Ingrese un valor para sacar su factorial: "))
Auxiliar = 1
Resultado = Valor_Ingresado

def Resolver(Resultado, Auxiliar):
  if Auxiliar == Valor_Ingresado:
    print(Resultado)
    return
  else:
    Resultado = Resultado * Auxiliar
    print(Resultado)
    Resolver(Resultado, Auxiliar +1)  
Resolver(Resultado, Auxiliar)