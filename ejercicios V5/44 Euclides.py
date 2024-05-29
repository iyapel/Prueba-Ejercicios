print("-----Metodo de euclides-----")

Num1 = int(input("Ingrese el primer numero "))
Num2 = int(input("Ingrese el segundo numero numero "))

Residuo = 1
while Residuo != 0:
    cociente, Residuo = divmod(Num1, Num2)
    Num1 = Num2
    Num2 = Residuo
    print(f"{cociente, Residuo}")

