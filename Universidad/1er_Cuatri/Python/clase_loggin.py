import os

usuarios = [
    {"user": "cajero1", "password": "1234"},
    {"user": "cajero2", "password": "5678"}
]

archivo_productos = "productos.txt"

def cargar_productos():
    productos = []
    if not os.path.exists(archivo_productos):
        return productos
    with open(archivo_productos, "r", encoding="utf-8") as f:
        for linea in f:
            datos = linea.strip().split(",")
            if len(datos) == 3:
                sku, nombre, precio = datos
                productos.append({"sku": sku, "nombre": nombre, "precio": float(precio)})
    return productos

def guardar_productos(productos):
    with open(archivo_productos, "w", encoding="utf-8") as f:
        for p in productos:
            f.write(f'{p["sku"]},{p["nombre"]},{p["precio"]}\n')

productos = cargar_productos()

def login():
    intentos = 0
    while intentos < 3:
        usuario = input("Usuario: ")
        password = input("Contraseña: ")
        for u in usuarios:
            if u["user"] == usuario and u["password"] == password:
                print("Acceso concedido")
                return True
        print("Usuario o contraseña inválidos")
        intentos += 1
    print("Demasiados intentos. Saliendo del sistema")
    return False

def pausar():
    input("...Presiona <enter> para continuar...")

def limpiar_pantalla():
    print("\n" * 100)

def mostrar_productos():
    print("----- Lista de productos ------")
    for p in productos:
        print(f'SKU: {p["sku"]} | Nombre: {p["nombre"]} | Precio: {p["precio"]}')

def registrar_venta():
    total = 0
    print("\nIngrese SKU de productos o -1 para terminar")
    while True:
        sku = input("sku: ")
        if sku == "-1":
            break
        cantidad = int(input("Cantidad: "))
        encontrado = False
        for p in productos:
            if p["sku"] == sku:
                subtotal = p["precio"] * cantidad
                total += subtotal
                print(f'Agregado: {p["nombre"]} x {cantidad} = {subtotal}')
                encontrado = True
        if not encontrado:
            print("Producto no encontrado")
    print(f"Total de la venta: ${total}")
    pago = float(input("Cantidad pagada por el cliente: "))
    cambio = pago - total
    print(f"Cambio a entregar ${cambio}")

def agregar_producto():
    sku = input("Ingresa nuevo SKU: ")
    nombre = input("Ingresa nombre: ")
    precio = float(input("Ingresa precio: "))
    prod = {"sku": sku, "nombre": nombre, "precio": precio}
    productos.append(prod)
    guardar_productos(productos)
    print("Producto agregado\n")

def eliminar_producto():
    sku = input("Ingresa el SKU a eliminar: ")
    for p in productos:
        if p["sku"] == sku:
            productos.remove(p)
            guardar_productos(productos)
            print("Producto eliminado\n")
            return
    print("Producto no encontrado")

def menu():
    while True:
        limpiar_pantalla()
        print("-----Menú principal-----")
        print("1. Mostrar productos")
        print("2. Registrar venta")
        print("3. Agregar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        opc = input("Elija una opción: ")

        if opc == "1":
            mostrar_productos()
            pausar()
        elif opc == "2":
            registrar_venta()
            pausar()
        elif opc == "3":
            agregar_producto()
            pausar()
        elif opc == "4":
            eliminar_producto()
            pausar()
        elif opc == "5":
            print("Saliendo sistema")
            break
        else:
            print("Opción inválida")

if login():
    menu()
 