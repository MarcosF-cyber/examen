class Nodo:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, codigo, descripcion):
        nuevo = Nodo(codigo, descripcion)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.codigo, actual.descripcion)
            actual = actual.siguiente

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if len(self.items) == 0:
            return "Error: la pila está vacía"
        return self.items.pop()

    def consultar_cima(self):  # Reto individual
        if len(self.items) == 0:
            return "Error: la pila está vacía"
        return self.items[-1]

class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, elemento):
        self.items.append(elemento)

    def desencolar(self):
        if len(self.items) == 0:
            return "Error: la cola está vacía"
        return self.items.pop(0)

if __name__ == "__main__":
    datos = [("F01", "Alcohol"), ("F02", "Gasas"), ("F03", "Termómetro")]

    print("--- LISTA ENLAZADA ---")
    lista = ListaEnlazada()
    for codigo, desc in datos:
        lista.agregar(codigo, desc)
    lista.mostrar()

    print("\n--- COLA (FIFO) ---")
    cola = Cola()
    for codigo, desc in datos:
        cola.encolar(f"{codigo} {desc}")
    print(cola.desencolar())
    print(cola.desencolar())
    print(cola.desencolar())
    print(cola.desencolar())  # cola vacía

    print("\n--- PILA (LIFO) ---")
    pila = Pila()
    for codigo, desc in datos:
        pila.apilar(f"{codigo} {desc}")
    print("Cima sin eliminar:", pila.consultar_cima())
    print(pila.desapilar())
    print(pila.desapilar())
    print(pila.desapilar())
    print(pila.desapilar())  # pila vacía