x = int(input("Cantidad de discos: "))

cond = 0
discos = 0
mi_lista = []
while discos < x:
    discos = discos + 1 
    mi_lista.append(discos)
    
pilar_1 = mi_lista
pilar_2 = []
pilar_3 = []

Ultimo_Valor_1 = 0
Ultimo_Valor_2 = 0
Ultimo_Valor_3 = 0

Ultimo_Indice_1 = 0
Ultimo_Indice_2 = 0
Ultimo_Indice_3 = 0

print(mi_lista)

while pilar_3 != mi_lista:
    
    #Izquierda, Derecha
    
    cond = cond + 1
    print(cond)
    
    Ultimo_Indice_1 = len(pilar_1) - 1
    Ultimo_Indice_2 = len(pilar_2) - 1
    Ultimo_Indice_3 = len(pilar_3) - 1
    
    if Ultimo_Indice_1 < 0:
        Ultimo_Indice_1 = Ultimo_Indice_1 + 1
    elif Ultimo_Indice_2 < 0:
        Ultimo_Indice_2 = Ultimo_Indice_2 + 1
    elif Ultimo_Indice_3 < 0:
        Ultimo_Indice_3 = Ultimo_Indice_3 + 1
    
    if pilar_2 and pilar_3:
        Ultimo_Valor_1 = pilar_1[Ultimo_Indice_1]
        Ultimo_Valor_2 = pilar_2[Ultimo_Indice_2]
        Ultimo_Valor_3 = pilar_3[Ultimo_Indice_3]   
    else:
        Ultimo_Valor_1 = Ultimo_Indice_1
        if pilar_2:
            Ultimo_Valor_2 = pilar_2
        elif pilar_3:
            Ultimo_Valor_3 = pilar_3
            
    if Ultimo_Valor_1 > Ultimo_Indice_2 and Ultimo_Indice_2 < len(pilar_2):
        pilar_1.append(pilar_2[Ultimo_Indice_2]) 
        del pilar_2[Ultimo_Indice_2] 
        Ultimo_Indice_2 = len(pilar_2) - 1  
        
    if Ultimo_Valor_2 > Ultimo_Indice_3 and Ultimo_Indice_3 < len(pilar_3) and pilar_3:
        pilar_2.append(pilar_3[Ultimo_Indice_3])  
        del pilar_3[Ultimo_Indice_3] 
        Ultimo_Indice_3 = len(pilar_3) - 1 
        
    #Derecha, Izquierda
    
    Ultimo_Indice_1 = len(pilar_1) - 1
    Ultimo_Indice_2 = len(pilar_2) - 1
    Ultimo_Indice_3 = len(pilar_3) - 1
    
    if Ultimo_Indice_1 < 0:
        Ultimo_Indice_1 = Ultimo_Indice_1 + 1
    elif Ultimo_Indice_2 < 0:
        Ultimo_Indice_2 = Ultimo_Indice_2 + 1
    elif Ultimo_Indice_3 < 0:
        Ultimo_Indice_3 = Ultimo_Indice_3 + 1
    
    if pilar_2 and pilar_3:
        Ultimo_Valor_1 = pilar_1[Ultimo_Indice_1]
        Ultimo_Valor_2 = pilar_2[Ultimo_Indice_2]
        Ultimo_Valor_3 = pilar_3[Ultimo_Indice_3]   
    else:
        Ultimo_Valor_1 = Ultimo_Indice_1
        if pilar_2:
            Ultimo_Valor_2 = pilar_2
        elif pilar_3:
            Ultimo_Valor_3 = pilar_3
            
    Ultimo_Indice_1 = len(pilar_1) - 1
    Ultimo_Indice_2 = len(pilar_2) - 1
    Ultimo_Indice_3 = len(pilar_3) - 1
    
    if Ultimo_Indice_1 < 0:
        Ultimo_Indice_1 = Ultimo_Indice_1 + 1
    elif Ultimo_Indice_2 < 0:
        Ultimo_Indice_2 = Ultimo_Indice_2 + 1
    elif Ultimo_Indice_3 < 0:
        Ultimo_Indice_3 = Ultimo_Indice_3 + 1
    
    if pilar_2 and pilar_3:
        Ultimo_Valor_1 = pilar_1[Ultimo_Indice_1]
        Ultimo_Valor_2 = pilar_2[Ultimo_Indice_2]
        Ultimo_Valor_3 = pilar_3[Ultimo_Indice_3]   
    else:
        Ultimo_Valor_1 = Ultimo_Indice_1
        if pilar_2:
            Ultimo_Valor_2 = pilar_2
        elif pilar_3:
            Ultimo_Valor_3 = pilar_3
            
    if Ultimo_Valor_2 > Ultimo_Indice_1 and Ultimo_Indice_2 < len(pilar_2) and pilar_2:
        pilar_1.append(pilar_2[Ultimo_Indice_2])
        del pilar_2[Ultimo_Indice_2]  
        Ultimo_Indice_2 = len(pilar_2) - 1  
        
    if Ultimo_Valor_2 > Ultimo_Indice_3 and Ultimo_Indice_3 < len(pilar_3) and pilar_3:
        pilar_2.append(pilar_3[Ultimo_Indice_3])  
        del pilar_3[Ultimo_Indice_3]  
        Ultimo_Indice_3 = len(pilar_3) - 1

print("Pilar 1:", pilar_1)
print("Pilar 2:", pilar_2)
print("Pilar 3:", pilar_3)
