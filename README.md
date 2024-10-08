# Proyecto de Aplicación de Compra y Reparto de Productos

Este proyecto consiste en una aplicación de consola en Python para gestionar tiendas, productos y ventas. La aplicación permite crear tiendas de diferentes tipos (Restaurante, Supermercado, Farmacia), ingresar productos, listar productos y realizar ventas.

## Estructura del Proyecto

El proyecto está dividido en tres archivos principales:

1. **`producto.py`**: Define la clase `Producto` que encapsula la información del producto y sobrecarga operadores para manejar operaciones de suma y resta de stock.
2. **`tienda.py`**: Define la clase base `Tienda` y las clases derivadas `Restaurante`, `Supermercado`, y `Farmacia`. Cada clase maneja la lógica específica para el ingreso de productos, listado y realización de ventas.
3. **`programa.py`**: Contiene la lógica principal de la aplicación, permitiendo al usuario crear una tienda, ingresar productos, listar productos y realizar ventas a través de la consola.

## Instalación y Requisitos

Este proyecto está escrito en Python 3. Asegúrate de tener Python 3 instalado en tu sistema.

1. **Clona el repositorio** (si está disponible en un repositorio remoto) o descarga los archivos `producto.py`, `tienda.py` y `programa.py` a tu directorio local.

2. **Instala Python 3** (si aún no lo tienes). Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

3. **Ejecuta la aplicación**: Abre una terminal o línea de comandos, navega al directorio donde se encuentran los archivos y ejecuta el archivo `programa.py` usando el siguiente comando:

   ```bash
   python programa.py

## Uso de la Aplicación

    Crear una Tienda:
        Selecciona el tipo de tienda (1: Restaurante, 2: Supermercado, 3: Farmacia).
        Ingresa el nombre de la tienda y el costo de delivery.

    Ingresar Productos:
        Selecciona la opción para ingresar un producto.
        Proporciona el nombre del producto, precio y stock (si aplica).

    Listar Productos:
        Selecciona la opción para listar los productos. La visualización de los productos varía según el tipo de tienda:
            Restaurante: Muestra el nombre y el precio.
            Supermercado: Muestra el nombre, precio y mensaje de stock bajo si el stock es menor a 10.
            Farmacia: Muestra el nombre, precio y mensaje de envío gratis si el precio es mayor a $15,000.

    Realizar Venta:
        Selecciona la opción para realizar una venta.
        Proporciona el nombre del producto y la cantidad deseada. El precio total de la venta se mostrará si la venta es válida.

    Salir:
        Selecciona la opción para salir del programa.

## Detalles de Implementación

    Encapsulamiento: La clase Producto utiliza propiedades para manejar el nombre, precio y stock del producto. La clase Tienda y sus derivadas encapsulan la lógica específica para cada tipo de tienda.
    Abstracción: La clase Tienda actúa como una clase base abstracta que define métodos que deben ser implementados por las clases derivadas (Restaurante, Supermercado, Farmacia).
    Composición y Colaboración: La clase Tienda mantiene una lista de objetos Producto y colabora con estos objetos para realizar operaciones de ingreso y venta de productos.

## Autores
Arlenis Gonzalez
Karen Limari
Ambar Zambrano

## Contribuciones

Las contribuciones al proyecto son bienvenidas. Si tienes alguna sugerencia o encuentras algún error, por favor, abre un issue en el repositorio (si está disponible) o contacta con el mantenedor del proyecto.

## Licencia

Este proyecto está licenciado bajo la MIT License - consulta el archivo LICENSE para más detalles.
