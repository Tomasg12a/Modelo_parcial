"""
Gestión de Inventario
La Empresa “Empire Inventory” necesita desarrollar un sistema de administración de
productos para sus almacenes. Para cada producto se almacenará:
• Nombre del producto.
• Precio del producto.
• Cantidad del producto.
La información de los productos se almacenará en un arreglo bidimensional, donde cada fila
representara un producto y las columnas contendrán los datos mencionados.

Requerimientos:
El sistema deberá constar de los siguientes puntos:
1. Menú Principal: Mostrar un menú con las siguientes opciones disponibles:
• Cargar producto/s.
• Buscar producto.
• Ordenar inventario.
• Mostrar producto más caro y más barato.
• Mostrar productos con precio mayor a 15000.
• Salir
2. Cargar inventario:
• Desarrollar una función que permita al usuario ingresar los datos del o los
productos en una matriz (nombre, precio, cantidad).
• El sistema debe permitir al usuario ingresar la cantidad deseada de productos.
3. Buscar producto:
• Implementar un algoritmo de búsqueda que permita al usuario encontrar un
producto específico por su nombre y muestre por pantalla todos los datos de
ese producto (nombre, precio y cantidad).
4. Ordenar inventario:
• Utilizar un algoritmo de ordenamiento para ordenar los productos en función
de su precio de manera ascendente y luego mostrar por pantalla los productos
ordenados.
5. Mostrar producto más caro:
• Desarrollar una función que identifique y muestre el producto más caro del
inventario.
6. Mostrar producto más barato:
• Desarrollar una función que identifique y muestre el producto más barato del
inventario.
Requisitos técnicos:
▪ Utilizar funciones para cada una de las operaciones mencionadas.
▪ Mantener una estructura de código limpia y bien comentada.
▪ Si el usuario selecciona cualquier opción sin que existan productos registrados en el
sistema, aparecerá un mensaje en pantalla notificando que no hay productos
disponibles para la operación solicitada.
Entrega del programa
▪ La entrega se deberá realizar mediante el link al repositorio de GitHub.

"""
# Gestión de Inventario
# La Empresa “Empire Inventory” necesita desarrollar un sistema de administración de
# productos para sus almacenes. Para cada producto se almacenará:
# • Nombre del producto.
# • Precio del producto.
# • Cantidad del producto.
# La información de los productos se almacenará en un arreglo bidimensional, donde cada fila
# representara un producto y las columnas contendrán los datos mencionados.

INVENTARIO = []

# Requerimientos:
# El sistema deberá constar de los siguientes puntos:
# 1. Menú Principal: Mostrar un menú con las siguientes opciones disponibles:
# • Cargar producto/s.
# • Buscar producto.
# • Ordenar inventario.
# • Mostrar producto más caro y más barato.
# • Mostrar productos con precio mayor a 15000.
# • Salir
def menu():
    while True:
      print("""
        [Menu principal]
          Seleccione una opcion:
        1• Cargar producto/s.
        2• Buscar producto.
        3• Ordenar inventario.
        4• Mostrar producto más caro y más barato.
        5• Mostrar productos con precio mayor a 15000.
        6• Salir
          """)
      opcion = int(input("Seleccione una opción (1-6): "))
      match opcion:
          case 1:
            cargar_productos()
          case 2:
            buscar_producto()
          case 3:
            ordenar_inventario()
          case 4:
            producto_mas_caro()
          case 5:
            producto_mas_barato()
          case  6:
            productos_precio_mayor()
          case 7:
            print('Saliendo del menu...')
            break
          case _:
            print("Opcion invalida, selleccionar un numero del 1 al 6")

# 2. Cargar inventario:
# • Desarrollar una función que permita al usuario ingresar los datos del o los
# productos en una matriz (nombre, precio, cantidad).
# • El sistema debe permitir al usuario ingresar la cantidad deseada de productos.
def cargar_productos():
  while True:
    nombre_producto = input("Ingrese el nombre del producto a agregar: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio por unidad del producto: "))
    producto = [nombre_producto, cantidad, precio]
    INVENTARIO.append(producto)

    continuar = input("¿Desea cargar otro producto? (s/n): ")
    if continuar == "n":
        break

# 3. Buscar producto:
# • Implementar un algoritmo de búsqueda que permita al usuario encontrar un
# producto específico por su nombre y muestre por pantalla todos los datos de
# ese producto (nombre, precio y cantidad).

def buscar_producto():
    buscar_nombre = input("Ingrese el nombre del producto a buscar: ")  
    for producto in INVENTARIO:  
        if producto[0].lower() == buscar_nombre.lower():  
            print(f"Producto encontrado: Nombre: {producto[0]}, Cantidad: {producto[1]}, Precio: {producto[2]}")  
            return  
    print("Producto no encontrado.")  


# 4. Ordenar inventario:
# • Utilizar un algoritmo de ordenamiento para ordenar los productos en función
# de su precio de manera ascendente y luego mostrar por pantalla los productos ordenados.
def ordenar_inventario():  
    n = len(INVENTARIO)  
    # Implementacion de bubble sort
    for i in range(n):  
        for j in range(0, n-i-1):
            if INVENTARIO[j][2] > INVENTARIO[j+1][2]: 
                INVENTARIO[j], INVENTARIO[j+1] = INVENTARIO[j+1], INVENTARIO[j]

    print("Inventario ordenado por precio:")  
    for producto in INVENTARIO:  
        print(f"Nombre: {producto[0]}, Cantidad: {producto[1]}, Precio: {producto[2]}")  

# 5. Mostrar producto más caro:
# • Desarrollar una función que identifique y muestre el producto más caro del inventario.
def producto_mas_caro():  
    if not INVENTARIO:  
        print("El inventario está vacío.")  
        return  

    producto_mas_caro = INVENTARIO[0]  

    for producto in INVENTARIO:  
        if producto[2] > producto_mas_caro[2]:
            producto_mas_caro = producto  

    print(f"Producto más caro: Nombre: {producto_mas_caro[0]}, Cantidad: {producto_mas_caro[1]}, Precio: {producto_mas_caro[2]}")   

# 6. Mostrar producto más barato:
# • Desarrollar una función que identifique y muestre el producto más barato del inventario.
def producto_mas_barato():
    if not INVENTARIO:  
        print("El inventario está vacío.")  
        return  
    producto_mas_barato = INVENTARIO[0]   
    for producto in INVENTARIO:  
        if producto[2] < producto_mas_barato[2]: 
          producto_mas_barato = producto
    print(f"Producto más barato: Nombre: {producto_mas_barato[0]}, Cantidad: {producto_mas_barato[1]}, Precio: {producto_mas_barato[2]}") 


# • Mostrar productos con precio mayor a 15000.
def productos_precio_mayor():  
    productos_filtrados = [producto for producto in INVENTARIO if producto[2] > 15000]  
    
    if not productos_filtrados:  
        print("No hay productos con precio mayor a 15000.")  
        return  

    print("Productos con precio mayor a 15000:")  
    for producto in productos_filtrados:  
        print(f"Nombre: {producto[0]}, Cantidad: {producto[1]}, Precio: {producto[2]}")

menu()