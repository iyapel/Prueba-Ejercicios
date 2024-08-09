class Nodo:
    def __init__(self, dato):
        self.izquierdo = None
        self.derecho = None
        self.dato = dato

    def __str__(self):
        return str(self.dato)

class Arbol:
    def __init__(self):
        self.raiz = None

    def recorrido_postorden(self, nodo):
        if nodo:
            self.recorrido_postorden(nodo.izquierdo)
            self.recorrido_postorden(nodo.derecho)
            print(nodo.dato, end=' ')

arbol = Arbol()
raiz = Nodo(1)
raiz.izquierdo = Nodo(2)
raiz.derecho = Nodo(3)
raiz.izquierdo.izquierdo = Nodo(4)
raiz.izquierdo.derecho = Nodo(5)

print("Recorrido en postorden: ", end="")
arbol.recorrido_postorden(raiz)