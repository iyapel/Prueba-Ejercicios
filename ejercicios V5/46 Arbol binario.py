class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            self._insertar(nuevo_nodo, self.raiz)

    def _insertar(self, nuevo_nodo, nodo_actual):
        if nuevo_nodo.dato < nodo_actual.dato:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = nuevo_nodo
            else:
                self._insertar(nuevo_nodo, nodo_actual.izquierdo)
        else:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = nuevo_nodo
            else:
                self._insertar(nuevo_nodo, nodo_actual.derecho)

    def buscar(self, dato):
        if self.raiz is None:
            return None
        else:
            return self._buscar(dato, self.raiz)

    def _buscar(self, dato, nodo_actual):
        if nodo_actual is None:
            return None
        elif dato == nodo_actual.dato:
            return nodo_actual
        elif dato < nodo_actual.dato:
            return self._buscar(dato, nodo_actual.izquierdo)
        else:
            return self._buscar(dato, nodo_actual.derecho)

    def eliminar(self, dato):
        if self.raiz is None:
            return
        else:
            self._eliminar(dato, self.raiz)

    def _eliminar(self, dato, nodo_actual):
        if dato < nodo_actual.dato:
            if nodo_actual.izquierdo is not None:
                self._eliminar(dato, nodo_actual.izquierdo)
        elif dato > nodo_actual.dato:
            if nodo_actual.derecho is not None:
                self._eliminar(dato, nodo_actual.derecho)
        else:
            if nodo_actual.izquierdo is None and nodo_actual.derecho is None:
                nodo_actual = None
            elif nodo_actual.izquierdo is None:
                nodo_actual = nodo_actual.derecho
            elif nodo_actual.derecho is None:
                nodo_actual = nodo_actual.izquierdo
            else:
                nodo_auxiliar = self._minimo(nodo_actual.derecho)
                nodo_actual.dato = nodo_auxiliar.dato
                self._eliminar(nodo_auxiliar.dato, nodo_actual.derecho)

    def _minimo(self, nodo_actual):
        while nodo_actual.izquierdo is not None:
            nodo_actual = nodo_actual.izquierdo
        return nodo_actual

    def _recorrido_inorden(self, nodo_actual):
        if nodo_actual is not None:
            self._recorrido_inorden(nodo_actual.izquierdo)
            print(nodo_actual.dato)
            self._recorrido_inorden(nodo_actual.derecho)

    def recorrido_inorden(self):
        self._recorrido_inorden(self.raiz)

# Ejemplo de uso
arbol = ArbolBinarioBusqueda()
arbol.insertar(10)
arbol.insertar(5)
arbol.insertar(15)
arbol.insertar(3)
arbol.insertar(7)
arbol.insertar(12)
arbol.insertar(20)

arbol.recorrido_inorden()

print("--------------------")

nodo_encontrado = arbol.buscar(15)
if nodo_encontrado is not None:
    print("Nodo encontrado:", nodo_encontrado.dato)
else:
    print("Nodo no encontrado")

arbol.eliminar(15)

print("--------------------")

arbol.recorrido_inorden()
