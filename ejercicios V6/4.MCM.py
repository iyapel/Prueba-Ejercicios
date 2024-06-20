#Link de la explicacion del codigo:
#https://youtu.be/asObeoHlaDQ

def encontrar_divisores(numero, divisor=2, valores=[]):

    if divisor == numero:
        return valores

    if numero % divisor == 0:
        valores.append(divisor)
        
    return encontrar_divisores(numero, divisor + 1, valores)

def calcular_mcm(valores):
    if not valores:
        return None

    def mcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def mcm(a, b):
        return a * (b // mcd(a, b))

    resultado = valores[0]

    for valor in valores[1:]:
        resultado = mcm(resultado, valor)
    
    return resultado

Numero = int(input("Ingrese un número: "))

valores_divisores = encontrar_divisores(Numero)

mcm_numero = calcular_mcm(valores_divisores)

# Mostrar el resultado
print("El mínimo común múltiplo de", Numero, "es:", mcm_numero)