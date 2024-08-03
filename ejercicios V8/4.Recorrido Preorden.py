class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def preorden(nodo):
    if nodo is not None:
        print(nodo.valor, end=" ")
        preorden(nodo.izquierdo)
        preorden(nodo.derecho)

raiz = Nodo(5)
raiz.izquierdo = Nodo(3)
raiz.derecho = Nodo(7)
raiz.izquierdo.izquierdo = Nodo(2)
raiz.izquierdo.derecho = Nodo(4)

print("Recorrido en preorden:")
preorden(raiz)