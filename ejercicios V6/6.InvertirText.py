#Link de la explicacion del codigo
#https://youtu.be/MgsEhcNAKTE

Texto = input("Ingrese un texto: ")
Texto_invertido_F = ""
Texto_invertido_A = ""
resultado = False
cantidad = len(Texto_invertido_A) + 1        

def Resolver(Texto_invertido_F,Texto_invertido_A , resultado, cantidad):
    if Texto_invertido_F == Texto_invertido_A:
        resultado = True
        print(resultado)
    else:
        for x in Texto_invertido_A:
            Texto_invertido_F = Texto_invertido_F + x 
        print(Texto_invertido_F)
        
        Resolver(Texto_invertido_F, Texto_invertido_A,resultado, cantidad - 1)
        
for i in Texto:
    
    Texto_invertido_A = i + Texto_invertido_A
    
Resolver(Texto_invertido_F, Texto_invertido_A,+resultado, cantidad)
