#explicacion del codigo:
#https://youtu.be/8FzEhlt6fk4

Valor_Ingresado = int(input("Ingrese un valor para sacar su factorial: "))

Resultado = Valor_Ingresado

for i in range(1, Valor_Ingresado): 

    Resultado = Resultado * i
    print(Resultado)