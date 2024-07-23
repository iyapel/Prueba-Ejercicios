class Nodo:
  def __init__(self, dato):
    self.dato = dato
    self.izquierdo = None
    self.derecho = None

  def insertar(self, dato):
    def insertar_recursivo(nodo, dato):
      if nodo is None:
        return Nodo(dato)
      elif dato < nodo.dato:
        nodo.izquierdo = insertar_recursivo(nodo.izquierdo, dato)
      else:
        nodo.derecho = insertar_recursivo(nodo.derecho, dato)
      return nodo

    self.raiz = insertar_recursivo(self.raiz, dato)

abb = ABB()
abb.insertar(10)
abb.insertar(5)
abb.insertar(15)
