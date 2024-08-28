from tienda import Restaurante, Supermercado, Farmacia

def crear_tienda():
    print("Selecciona el tipo de tienda (1: Restaurante, 2: Supermercado, 3: Farmacia):")
    tipo = int(input())
    print("Ingrese el nombre de la tienda:")
    nombre = input()
    print("Ingrese el costo de delivery:")
    costo_delivery = float(input())
    
    if tipo == 1:
        return Restaurante(nombre, costo_delivery)
    elif tipo == 2:
        return Supermercado(nombre, costo_delivery)
    elif tipo == 3:
        return Farmacia(nombre, costo_delivery)
    else:
        print("Tipo de tienda no válido.")
        return None

def ingresar_producto(tienda):
    print("Ingrese el nombre del producto:")
    nombre = input()
    print("Ingrese el precio del producto:")
    precio = float(input())
    print("Ingrese el stock del producto (deje en blanco si no aplica):")
    stock = input()
    stock = int(stock) if stock else 0
    tienda.ingresar_producto(nombre, precio, stock)

def listar_productos(tienda):
    print(tienda.listar_productos())

def realizar_venta(tienda):
    print("Ingrese el nombre del producto para vender:")
    nombre = input()
    print("Ingrese la cantidad deseada:")
    cantidad = int(input())
    precio_total = tienda.realizar_venta(nombre, cantidad)
    if precio_total is not None:
        print(f"Venta realizada. Precio total: ${precio_total}")
    else:
        print("Venta no realizada. Verifique el stock o el producto.")

def main():
    tienda = crear_tienda()
    if tienda is None:
        return

    while True:
        print("\nSelecciona una opción:")
        print("1: Ingresar producto")
        print("2: Listar productos")
        print("3: Realizar venta")
        print("4: Salir")

        opcion = int(input())
        if opcion == 1:
            ingresar_producto(tienda)
        elif opcion == 2:
            listar_productos(tienda)
        elif opcion == 3:
            realizar_venta(tienda)
        elif opcion == 4:
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
