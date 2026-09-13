# **Sistema de Inventario en Python**





#### ¿Qué hace el programa?



Sistema de inventario con menú interactivo que permite registrar productos, buscarlos por

nombre y generar un reporte general (valor total del inventario y productos con stock bajo).

El flujo integrado es:



main.py → registrarProducto() / buscarProducto() / generarReporte()

→ calcularTotal() + validarStock()

→ inventario



#### ¿Cómo puede ejecutarse?



1\. Nos aseguramos de tener Python 3 instalado.

2\. Se coloca calculos.py , inventario.py y main.py en la misma carpeta.

3\. Ejecuta:

&#x09;python3 main.py

&#x09;Por defecto corre pruebas() (3 casos automáticos, no interactivo). Para usar el menú

&#x09;interactivo, dentro de main.py comenta pruebas() y descomenta main() .



#### Funciones del sistema



calcularTotal(precio, cantidad) — calculos.py



Parámetros: precio (float), cantidad (int).

Retorna: float — el total ( precio \* cantidad ).



validarStock(cantidad, umbral=5) — calculos.py



Parámetros: cantidad (int), umbral (int, por defecto 5).

Retorna: bool — True si cantidad < umbral (stock bajo).



registrarProducto(nombre, precio, cantidad, inventario) — inventario.py



Parámetros: nombre (str), precio (float), cantidad (int), inventario (list).

Retorna: list — el inventario actualizado con el nuevo producto.

Usa internamente calcularTotal() y validarStock() .



buscarProducto(nombre, inventario) — inventario.py



Parámetros: nombre (str) a buscar, inventario (list).

Retorna: dict del producto si lo encuentra, o None si no existe.



generarReporte(inventario) — inventario.py



Parámetros: inventario (list).

Retorna: dict con valor\_total (suma de todos los totales) y productos\_bajo\_stock

(lista de nombres con stock bajo).



main() / pruebas() — main.py

main(): menú interactivo controlado por while / if (registrar, buscar, reporte, salir).

pruebas() : 3 casos automáticos de prueba sin necesidad de escribir en consola.



###### Casos de prueba (función pruebas() )



|#|Producto|Precio|Cantidad|Resultado esperado|
|-|-|-|-|-|
|1|Cuaderno|1.50|3|Stock bajo|
|2|Lapicero|0.75|20|Stock suficiente|
|3|Mochila|25.00|4|Stock bajo|





Reporte esperado: valor\_total = 119.5 , productos\_bajo\_stock = \['Cuaderno',

'Mochila'] .



#### Trabajo por integrante



|**Integrante**|**Trabajo**|**Archivos**|
|-|-|-|

|**Juan Miguel Posada**|Cálculo y validación|inventario.py |
|**María Belén Díaz**|Registro, búsqueda y reporte|inventario.py|
|**José Daniel Gregg**|Programa principal y pruebas|main.py|
|**Rafael Avalos**|Integración y documentación|README.md|
|**Horacio A Larios C**| Debbuging y Dirreciòn general| main.py |


#### Notas de integración



Se confirmó que inventario.py importa y usa correctamente calcularTotal() y

validarStock() de calculos.py .



Se confirmó que main.py importa registrarProducto() , buscarProducto() y

generarReporte() sin errores.



Se corrieron ambos modos ( pruebas() automático y main() interactivo) end-to-end

sin errores.

