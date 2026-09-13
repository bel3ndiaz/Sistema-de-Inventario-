# inventario.py
# Funciones propias del sistema de inventario.
# Cada función hace UNA sola tarea, recibe parámetros y retorna un valor.
# Se conectan entre sí: unas usan el resultado de otras.


def calcularTotal(precio, cantidad):
    """
    Calcula el valor total de un producto.
    Parámetros:
        precio (float): precio unitario del producto
        cantidad (int): cantidad disponible o vendida
    Retorna:
        float: precio * cantidad
    """
    return precio * cantidad


def validarStock(cantidad, umbral=5):
    """
    Determina si el stock de un producto está bajo.
    Parámetros:
        cantidad (int): cantidad actual del producto
        umbral (int): cantidad mínima aceptable (por defecto 5)
    Retorna:
        bool: True si el stock está bajo, False si está bien
    """
    return cantidad < umbral




def buscarProducto(nombre, inventario):
    """
    Busca un producto por nombre dentro del inventario.
    Parámetros:
        nombre (str): nombre a buscar (no distingue mayúsculas/minúsculas)
        inventario (list): lista de productos
    Retorna:
        dict o None: el producto encontrado, o None si no existe
    """
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            return producto
    return None


def generarReporte(inventario):
    """
    Genera un resumen general del inventario: valor total y
    lista de productos con stock bajo.
    Parámetros:
        inventario (list): lista de productos
    Retorna:
        dict: {"valor_total": float, "productos_bajo_stock": list}
    """
    valor_total = 0
    productos_bajo_stock = []

    for producto in inventario:
        valor_total += producto["total"]
        if producto["stock_bajo"]:
            productos_bajo_stock.append(producto["nombre"])

    reporte = {
        "valor_total": valor_total,
        "productos_bajo_stock": productos_bajo_stock,
    }
    return reporte
