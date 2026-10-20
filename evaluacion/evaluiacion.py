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
        # TODO 1: agrega el nodo al final sin perder los anteriores
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
            print(f"{actual.codigo} - {actual.descripcion}")
            actual = actual.siguiente

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        # TODO 2: agrega el elemento a la cima
        self.items.append(elemento)

    def desapilar(self):
        # TODO 3: devuelve y elimina el último elemento; controla pila vacía
        if len(self.items) == 0:
            return "Error: La pila de farmacia está vacía"
        return self.items.pop()

    # RETO INDIVIDUAL (Farmacia)
    def consultar_cima(self):
        if len(self.items) == 0:
            return "Error: La pila está vacía, no hay medicamentos para consultar"
        return self.items[-1] # Retorna el último sin eliminarlo

class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, elemento):
        # TODO 4: agrega el elemento al final
        self.items.append(elemento)

    def desencolar(self):
        # TODO 5: devuelve y elimina el primer elemento; controla cola vacía
        if len(self.items) == 0:
            return "Error: La cola de atención está vacía"
        return self.items.pop(0)

# ==========================================
# PRUEBAS DEL CASO: FARMACIA
# ==========================================
if __name__ == "__main__":
    print("--- SISTEMA DE GESTIÓN: FARMACIA ---\n")

    # 1. Lista Enlazada (Inventario)
    print("1. REGISTRO EN LISTA ENLAZADA (Inventario):")
    inventario = ListaEnlazada()
    inventario.agregar("F01", "Paracetamol 500mg")
    inventario.agregar("F02", "Ibuprofeno 400mg")
    inventario.agregar("F03", "Amoxicilina 250mg")
    inventario.mostrar()

    # 2. Cola (Atención de clientes / FIFO)
    print("\n2. ATENCIÓN EN COLA (Turnos de recetas - FIFO):")
    turnos = Cola()
    turnos.encolar("Cliente A - Receta Paracetamol")
    turnos.encolar("Cliente B - Receta Ibuprofeno")
    print(f"Atendiendo: {turnos.desencolar()}")
    print(f"Atendiendo: {turnos.desencolar()}")

    # 3. Pila (Lote de medicamentos / LIFO)
    print("\n3. GESTIÓN EN PILA (Lote de recepción - LIFO):")
    lote = Pila()
    lote.apilar("Caja 1: Paracetamol")
    lote.apilar("Caja 2: Ibuprofeno")
    lote.apilar("Caja 3: Amoxicilina")

    # 4. RETO INDIVIDUAL
    print("\n--- RETO INDIVIDUAL ---")
    ultimo = lote.consultar_cima()
    print(f"Último medicamento agregado (sin eliminar): {ultimo}")
    
    print("\nDespachando lote:")
    print(lote.desapilar())
    print(lote.desapilar())
    print(lote.desapilar())

2. Versión BIBLIOTECA (main_biblioteca.py)
Consulta el último libro agregado a la pila sin eliminarlo.

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
        # TODO 1: agrega el nodo al final sin perder los anteriores
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
            print(f"{actual.codigo} - {actual.descripcion}")
            actual = actual.siguiente

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        # TODO 2: agrega el elemento a la cima
        self.items.append(elemento)

    def desapilar(self):
        # TODO 3: devuelve y elimina el último elemento; controla pila vacía
        if len(self.items) == 0:
            return "Error: La pila de biblioteca está vacía"
        return self.items.pop()

    # RETO INDIVIDUAL (Biblioteca)
    def consultar_cima(self):
        if len(self.items) == 0:
            return "Error: La pila está vacía, no hay libros para consultar"
        return self.items[-1] # Retorna el último sin eliminarlo

class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, elemento):
        # TODO 4: agrega el elemento al final
        self.items.append(elemento)

    def desencolar(self):
        # TODO 5: devuelve y elimina el primer elemento; controla cola vacía
        if len(self.items) == 0:
            return "Error: La cola de préstamos está vacía"
        return self.items.pop(0)

# ==========================================
# PRUEBAS DEL CASO: BIBLIOTECA
# ==========================================
if __name__ == "__main__":
    print("--- SISTEMA DE GESTIÓN: BIBLIOTECA ---\n")

    # 1. Lista Enlazada (Catálogo)
    print("1. REGISTRO EN LISTA ENLAZADA (Catálogo):")
    catalogo = ListaEnlazada()
    catalogo.agregar("L01", "Cien años de soledad")
    catalogo.agregar("L02", "Don Quijote de la Mancha")
    catalogo.agregar("L03", "El principito")
    catalogo.mostrar()

    # 2. Cola (Préstamos / FIFO)
    print("\n2. ATENCIÓN EN COLA (Solicitudes de préstamo - FIFO):")
    prestamos = Cola()
    prestamos.encolar("Estudiante 1 - Solicita Cien años de soledad")
    prestamos.encolar("Estudiante 2 - Solicita Don Quijote")
    print(f"Procesando: {prestamos.desencolar()}")
    print(f"Procesando: {prestamos.desencolar()}")

    # 3. Pila (Devoluciones / LIFO)
    print("\n3. GESTIÓN EN PILA (Pila de devoluciones - LIFO):")
    devoluciones = Pila()
    devoluciones.apilar("Libro: Cien años de soledad")
    devoluciones.apilar("Libro: Don Quijote")
    devoluciones.apilar("Libro: El principito")

    # 4. RETO INDIVIDUAL
    print("\n--- RETO INDIVIDUAL ---")
    ultimo = devoluciones.consultar_cima()
    print(f"Último libro agregado a devoluciones (sin eliminar): {ultimo}")
    
    print("\nArchivando libros:")
    print(devoluciones.desapilar())
    print(devoluciones.desapilar())
    print(devoluciones.desapilar())

3. Versión VETERINARIA (main_veterinaria.py)
Consulta la última mascota agregada a la pila sin eliminarla.

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
        # TODO 1: agrega el nodo al final sin perder los anteriores
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
            print(f"{actual.codigo} - {actual.descripcion}")
            actual = actual.siguiente

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        # TODO 2: agrega el elemento a la cima
        self.items.append(elemento)

    def desapilar(self):
        # TODO 3: devuelve y elimina el último elemento; controla pila vacía
        if len(self.items) == 0:
            return "Error: La pila de veterinaria está vacía"
        return self.items.pop()

    # RETO INDIVIDUAL (Veterinaria)
    def consultar_cima(self):
        if len(self.items) == 0:
            return "Error: La pila está vacía, no hay mascotas para consultar"
        return self.items[-1] # Retorna el último sin eliminarlo

class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, elemento):
        # TODO 4: agrega el elemento al final
        self.items.append(elemento)

    def desencolar(self):
        # TODO 5: devuelve y elimina el primer elemento; controla cola vacía
        if len(self.items) == 0:
            return "Error: La sala de espera está vacía"
        return self.items.pop(0)

# ==========================================
# PRUEBAS DEL CASO: VETERINARIA
# ==========================================
if __name__ == "__main__":
    print("--- SISTEMA DE GESTIÓN: VETERINARIA ---\n")

    # 1. Lista Enlazada (Historial Clínico)
    print("1. REGISTRO EN LISTA ENLAZADA (Historial de Mascotas):")
    historial = ListaEnlazada()
    historial.agregar("M01", "Firulais (Perro) - Vacunación")
    historial.agregar("M02", "Michi (Gato) - Desparasitación")
    historial.agregar("M03", "Rocky (Perro) - Cirugía menor")
    historial.mostrar()

    # 2. Cola (Sala de Espera / FIFO)
    print("\n2. ATENCIÓN EN COLA (Sala de espera - FIFO):")
    sala_espera = Cola()
    sala_espera.encolar("Dueño A con Firulais")
    sala_espera.encolar("Dueño B con Michi")
    print(f"Llamando a consulta: {sala_espera.desencolar()}")
    print(f"Llamando a consulta: {sala_espera.desencolar()}")

    # 3. Pila (Urgencias / LIFO)
    print("\n3. GESTIÓN EN PILA (Registro de Urgencias - LIFO):")
    urgencias = Pila()
    urgencias.apilar("Urgencia: Firulais (Herida en pata)")
    urgencias.apilar("Urgencia: Michi (Intoxicación)")
    urgencias.apilar("Urgencia: Rocky (Dificultad respiratoria)")

    # 4. RETO INDIVIDUAL
    print("\n--- RETO INDIVIDUAL ---")
    ultima_mascota = urgencias.consultar_cima()
    print(f"Última mascota en urgencias (sin eliminar): {ultima_mascota}")
    
    print("\nAtendiendo urgencias:")
    print(urgencias.desapilar())
    print(urgencias.desapilar())
    print(urgencias.desapilar())