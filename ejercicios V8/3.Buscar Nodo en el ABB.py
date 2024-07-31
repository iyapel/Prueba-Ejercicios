class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def buscar(self, valor):

        if valor == self.data:
            return True
        elif valor < self.data:
            if self.left is None:
                return False
            else:
                return self.left.buscar(valor)
        else:
            if self.right is None:
                return False
            else:
                return self.right.buscar(valor)


# Creando un Arbol a ver si funciona
root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)

# Buscando un valor a ver si funciona
if root.buscar(40):
    print("El valor 40 se encuentra en el árbol")
else:
    print("El valor 40 no se encuentra en el árbol")