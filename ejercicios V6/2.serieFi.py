a = 0
b = 1
c = 0
cond = int(input("Ingrese el número de valores que desea ver: "))

for i in range(cond + 1):
    c = a + b
    a = b 
    b = c
    print("vuelta", i, "numero ", c)

