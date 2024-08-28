class Producto:
    def __init__(self, nombre, precio, stock=0):
        self._nombre = nombre
        self._precio = precio
        self._stock = max(stock, 0)  # Asegurarse de que el stock no sea negativo

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        self._stock = max(value, 0)  # Asegurarse de que el stock no sea negativo

    def __add__(self, other):
        if self._nombre == other.nombre:
            return Producto(self._nombre, self._precio, self._stock + other.stock)
        raise ValueError("Los productos deben tener el mismo nombre para sumar stock")

    def __sub__(self, cantidad):
        if self._stock - cantidad < 0:
            cantidad = self._stock
        self._stock -= cantidad
        return cantidad

    def __eq__(self, other):
        return self._nombre == other.nombre

    def __str__(self):
        return f"{self._nombre}: ${self._precio} (Stock: {self._stock})"
