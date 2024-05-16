from producto import Producto

class Ventas:
    def __init__(self):
        self.productos = []
        self.cantidadVentas = 0
        self.totalVentas = 0
        self.piezasVendidas = 0

    def agregar(self, producto):
        self.productos.append(producto)

    def mostrarProducto(self):
        print("Lista de productos disponibles:")
        for producto in self.productos:
            if producto.stock > 0:
                print(f"ID: {producto.id.zfill(2)}")
                print(f"Nombre: {producto.nombre}")
                print(f"Stock: {producto.stock}")
                print(f"Precio: ${producto.precio}\n")
            else:
                print(f"ID: {producto.id.zfill(2)} - {producto.nombre} (No disponible)\n")

    def Vender(self):
        carrito = []
        while True:
            self.mostrarProducto()
            opcion = input("Elige un producto por su ID para agregar al carrito (Escribe 'F' para terminar la venta): ")
            if opcion == 'F':
                break
            
            producto = self.buscarProducto(opcion)
            if producto:
                if producto.stock > 0:
                    cantidad = int(input("Cantidad: "))
                    if cantidad <= producto.stock:
                        carrito.append((producto, cantidad))
                        producto.stock -= cantidad
                        if producto.stock <= 0:
                            producto.stock = 0  
                            print("***AVISO: EL PRODUCTO SE HA AGOTADO***")
                        self.piezasVendidas += cantidad
                        self.totalVentas += cantidad * producto.precio
                    else:
                        print("***ERROR: NO HAY SUFICIENTE STOCK DISPONIBLE***")
                else:
                    print("***ERROR: EL PRODUCTO NO ESTÁ DISPONIBLE***")
            else:
                print("Producto no encontrado.")

        cantidadArticulos = sum(item[1] for item in carrito)
        print("\nVenta realizada exitosamente:")
        print(f"Importe total de ventas: ${self.totalVentas}")
        print(f"Cantidad de artículos: {cantidadArticulos}")

        self.cantidadVentas += 1

    def buscarProducto(self, id):
        for producto in self.productos:
            if producto.id == id:
                return producto
        return None

    def reporte(self):
        cantidadArticulos = len(self.productos)
        print(f"Cantidad de ventas: {self.cantidadVentas}")
        print(f"Importe total de ventas: ${self.totalVentas}")
        print(f"Cantidad de artículos: {cantidadArticulos}")
        print(f"Total de piezas vendidas: {self.piezasVendidas}")


if __name__ == "__main__":
    Ventas = Ventas()

    Ventas.agregar(Producto("Papel higiénico biodegradable", 180.50, 30))
    Ventas.agregar(Producto("Cargador portátil para teléfono móvil", 150.50, 5))
    Ventas.agregar(Producto("Esponja de silicona multiusos", 50.50, 10))
    Ventas.agregar(Producto("Set de herramientas básicas", 1500, 0))
    Ventas.agregar(Producto("Bolsas reutilizables para compras", 99.50, 1))
    Ventas.agregar(Producto("Barra de proteína energética", 89.50, 9))
    Ventas.agregar(Producto("Lámpara de lectura recargable", 60.50, 3))
    Ventas.agregar(Producto("Organizador de cables y cargadores", 200.50, 20))
    Ventas.agregar(Producto("Crema hidratante facial con protección solar", 600.50, 31))
    Ventas.agregar(Producto("Plantas de interior purificadoras de aire", 40.50, 84))

    while True:
        print("\nCarrito de compras")
        print("A. Listar productos")
        print("B. Agregar productos")
        print("C. Realizar venta")
        print("S. Salir")
        opcion = input("\nElige una opción: ").upper()

        if opcion == "A":
            Ventas.mostrarProducto()
        elif opcion == "B":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))
            stock = int(input("Stock del producto: "))
            Ventas.agregar(Producto(nombre, precio, stock))
            print("*Producto agregado existosamente al catálogo*")
        elif opcion == "C":
            Ventas.Vender()
        elif opcion == "S":
            Ventas.reporte()
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")