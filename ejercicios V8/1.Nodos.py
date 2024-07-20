class Nodo:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class ABB:
    def __init__(self):
        self.root = None

    def insert(self, data):
        nuevo_nodo = Nodo(data)
        if self.root is None:
            self.root = nuevo_nodo
        else:
            actual = self.root
            while True:
                if data < actual.data:
                    if actual.left is None:
                        actual.left = nuevo_nodo
                        break
                    else:
                        actual = actual.left
                else:
                    if actual.right is None:
                        actual.right = nuevo_nodo
                        break
                    else:
                        actual = actual.right

    def search(self, data):
        actual = self.root
        while actual:
            if data == actual.data:
                return True
            elif data < actual.data:
                actual = actual.left
            else:
                actual = actual.right
        return False

abb = ABB()

abb.insert(5)
abb.insert(3)
abb.insert(7)
abb.insert(2)
abb.insert(4)
abb.insert(6)
abb.insert(8)

print(abb.search(3))  # Deberia imprimir True
print(abb.search(9))  # Deberia imprimir False