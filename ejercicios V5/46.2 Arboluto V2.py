class ArbolBinario:
    def __init__(self):
        self.raiz = None
        self.lista_predefinida = [10, 5, 15, 2, 7, 12, 20]

    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self._insertar(dato, self.raiz)

    def _insertar(self, dato, nodo):
        if dato < nodo.dato:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(dato)
            else:
                self._insertar(dato, nodo.izquierdo)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(dato)
            else:
                self._insertar(dato, nodo.derecho)

    def imprimir(self):
        self._imprimir(self.raiz)

    def _imprimir(self, nodo):
        if nodo is not None:
            print(nodo.dato)
            self._imprimir(nodo.izquierdo)
            self._imprimir(nodo.derecho)


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None


def main():
    arbol = ArbolBinario()

    # Insertar datos predefinidos
    for dato in arbol.lista_predefinida:
        arbol.insertar(dato)

    # Interfaz de usuario
    while True:
        opcion = input("¿Desea insertar un nuevo dato? (s/n): ")

        if opcion.lower() == "s":
            dato = int(input("Ingrese el nuevo dato: "))
            arbol.insertar(dato)
        else:
            break

    # Imprimir árbol
    print("Arbol binario:")
    arbol.imprimir()


if __name__ == "__main__":
    main()


