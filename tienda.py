from producto import Producto

class Tienda:
    def __init__(self, nombre, costo_delivery):
        self._nombre = nombre
        self._costo_delivery = costo_delivery
        self._productos = []

    def ingresar_producto(self, nombre, precio, stock=0):
        producto = Producto(nombre, precio, stock)
        for p in self._productos:
            if p == producto:
                p.stock += stock
                return
        self._productos.append(producto)

    def listar_productos(self):
        raise NotImplementedError("Este método debe ser implementado en las subclases")

    def realizar_venta(self, nombre, cantidad):
        raise NotImplementedError("Este método debe ser implementado en las subclases")


class Restaurante(Tienda):
    def __init__(self, nombre, costo_delivery):
        super().__init__(nombre, costo_delivery)

    def listar_productos(self):
        productos_listados = [f"{p.nombre}: ${p.precio}" for p in self._productos]
        return "\n".join(productos_listados)

    def realizar_venta(self, nombre, cantidad):
        for producto in self._productos:
            if producto.nombre == nombre:
                return producto.precio  # En Restaurante, siempre se vende el producto si se encuentra 
        return None


class Supermercado(Tienda):
    def __init__(self, nombre, costo_delivery):
        super().__init__(nombre, costo_delivery)

    def listar_productos(self):
        productos_listados = []
        for p in self._productos:
            stock_info = f" Pocos productos disponibles ({p.stock})" if p.stock < 10 else ""
            productos_listados.append(f"{p.nombre}: ${p.precio}{stock_info}")
        return "\n".join(productos_listados)

    def realizar_venta(self, nombre, cantidad):
        for producto in self._productos:
            if producto.nombre == nombre:
                if producto.stock >= cantidad:
                    producto.stock -= cantidad
                    return producto.precio * cantidad
                else:
                    return producto.precio * producto.stock
        return None


class Farmacia(Tienda):
    def __init__(self, nombre, costo_delivery):
        super().__init__(nombre, costo_delivery)

    def listar_productos(self):
        productos_listados = []
        for p in self._productos:
            envio_gratis = " Envío gratis al solicitar este producto" if p.precio > 15000 else ""
            productos_listados.append(f"{p.nombre}: ${p.precio}{envio_gratis}")
        return "\n".join(productos_listados)

    def realizar_venta(self, nombre, cantidad):
        if cantidad > 3:
            return None
        for producto in self._productos:
            if producto.nombre == nombre:
                if producto.stock >= cantidad:
                    producto.stock -= cantidad
                    return producto.precio * cantidad
                else:
                    return producto.precio * producto.stock
        return None
