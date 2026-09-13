# main.py
# Programa principal: conecta las funciones de inventario.py

from inventario import registrarProducto, buscarProducto, generarReporte


def mostrarMenu():
    print("\n--- SISTEMA DE INVENTARIO ---")
    print("1. Registrar producto")
    print("2. Buscar producto")
    print("3. Ver reporte general")
    print("4. Salir")


def main():
    inventario = []
    opcion = ""

    while opcion != "4":
        mostrarMenu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            inventario = registrarProducto(nombre, precio, cantidad, inventario)
            print(f"Producto '{nombre}' registrado correctamente.")

        elif opcion == "2":
            nombre = input("Nombre del producto a buscar: ")
            resultado = buscarProducto(nombre, inventario)
            if resultado is not None:
                print(resultado)
            else:
                print("Producto no encontrado.")

        elif opcion == "3":
            reporte = generarReporte(inventario)
            print(f"Valor total del inventario: {reporte['valor_total']}")
            if reporte["productos_bajo_stock"]:
                print("Productos con stock bajo:", reporte["productos_bajo_stock"])
            else:
                print("Ningún producto con stock bajo.")

        elif opcion == "4":
            print("Saliendo del sistema...")

        else:
            print("Opción no válida, intenta de nuevo.")


# --- Pruebas automáticas con 3 casos distintos (puedes correr esto en vez del menú) ---
def pruebas():
    inventario = []
    inventario = registrarProducto("Cuaderno", 1.50, 3, inventario)   # stock bajo
    inventario = registrarProducto("Lapicero", 0.75, 20, inventario)  # stock normal
    inventario = registrarProducto("Mochila", 25.00, 4, inventario)   # stock bajo

    for p in inventario:
        print(p)

    print(buscarProducto("Lapicero", inventario))
    print(generarReporte(inventario))


if __name__ == "__main__":
    main()
