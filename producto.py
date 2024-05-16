class Producto:
    contador_id = 1  # Contador para generar IDs únicos

    def __init__(self, nombre, precio, stock):
        self.id = str(Producto.contador_id).zfill(2)  # Genera el ID y lo formatea con dos dígitos, p. ej., 01, 02, ...
        Producto.contador_id += 1
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
