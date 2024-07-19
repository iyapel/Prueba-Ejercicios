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