"""
Módulo: menu
Contiene el menú principal del sistema y las opciones de interacción.
"""

from datetime import date

# Importar CRUD
from crud.clientes_crud import (
    crear_cliente,
    obtener_cliente,
    listar_clientes,
    agregar_factura_a_cliente,
    buscar_por_cedula
)

from crud.productos_crud import (
    registrar_producto,
    listar_productos,
    obtener_producto
)

from crud.facturas_crud import crear_factura, listar_facturas

# Importar vistas
from ui.vistas import (
    mostrar_cliente,
    mostrar_lista_clientes,
    mostrar_producto,
    mostrar_lista_productos,
    mostrar_factura,
    mostrar_lista_facturas
)

# Importar modelos para creación manual
from model.control_plagas import ControlPlagas
from model.fertilizante import Fertilizante
from model.antibiotico import Antibiotico, TipoAnimal


# ----------------------------------------------------------------------
# ---------------------------- MENÚ PRINCIPAL ---------------------------
# ----------------------------------------------------------------------

def mostrar_menu() -> None:
    print("\n========== SISTEMA DE FACTURACIÓN AGRÍCOLA ==========")
    print("1. Registrar cliente")
    print("2. Registrar producto")
    print("3. Crear factura")
    print("4. Mostrar clientes")
    print("5. Buscar facturas por cédula")
    print("6. Mostrar todos los productos")
    print("7. Mostrar todas las facturas")
    print("0. Salir")
    print("=====================================================")


def iniciar_menu() -> None:
    """
    Función principal del menú.
    """
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_cliente_ui()

        elif opcion == "2":
            registrar_producto_ui()

        elif opcion == "3":
            crear_factura_ui()

        elif opcion == "4":
            mostrar_lista_clientes(listar_clientes())

        elif opcion == "5":
            cedula = input("Ingrese la cédula del cliente: ")
            try:
                facturas = buscar_por_cedula(cedula)
                mostrar_lista_facturas(facturas)
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "6":
            mostrar_lista_productos(listar_productos())

        elif opcion == "7":
            mostrar_lista_facturas(listar_facturas())

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


# ----------------------------------------------------------------------
# ------------------------- FUNCIONES DE UI ----------------------------
# ----------------------------------------------------------------------

def registrar_cliente_ui() -> None:
    nombre = input("Nombre del cliente: ")
    cedula = input("Cédula del cliente: ")

    try:
        cliente = crear_cliente(nombre, cedula)
        print("Cliente registrado exitosamente.")
        mostrar_cliente(cliente)
    except ValueError as e:
        print(f"Error: {e}")


def registrar_producto_ui() -> None:
    print("\n--- Registrar Producto ---")
    print("1. Control de Plagas")
    print("2. Fertilizante")
    print("3. Antibiótico")

    tipo = input("Seleccione el tipo de producto: ")

    if tipo == "1":
        registro = input("Registro ICA: ")
        nombre = input("Nombre: ")
        frecuencia = int(input("Frecuencia de aplicación (días): "))
        carencia = int(input("Periodo de carencia (días): "))
        precio = float(input("Precio: "))

        producto = ControlPlagas(registro, nombre, frecuencia, carencia, precio)

    elif tipo == "2":
        from datetime import datetime
        registro = input("Registro ICA: ")
        nombre = input("Nombre: ")
        frecuencia = int(input("Frecuencia de aplicación (días): "))
        fecha_str = input("Fecha última aplicación (AAAA-MM-DD): ")
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        precio = float(input("Precio: "))

        producto = Fertilizante(registro, nombre, frecuencia, fecha, precio)

    elif tipo == "3":
        nombre = input("Nombre: ")
        dosis = float(input("Dosis (400–600 kg): "))
        animal = input("Tipo animal (BOVINO/CAPRINO/PORCINO): ")
        precio = float(input("Precio: "))

        animal_enum = TipoAnimal[animal.upper()]
        producto = Antibiotico(nombre, dosis, animal_enum, precio)

    else:
        print("Tipo no válido.")
        return

    registrar_producto(producto)
    print("Producto registrado:")
    mostrar_producto(producto)


def crear_factura_ui() -> None:
    print("\n--- Crear Factura ---")
    cedula = input("Cédula del cliente: ")

    cliente = obtener_cliente(cedula)
    if not cliente:
        print("No existe un cliente con esa cédula.")
        return

    productos = []
    while True:
        print("\nProductos disponibles:")
        mostrar_lista_productos(listar_productos())
        idp = input("ID del producto a agregar (o 'fin' para terminar): ")

        if idp.lower() == "fin":
            break

        producto = obtener_producto(idp)
        if producto:
            productos.append(producto)
            print("Producto agregado.")
        else:
            print("ID inválido.")

    if not productos:
        print("No se agregaron productos. No se crea factura.")
        return

    factura = crear_factura(date.today(), productos)
    agregar_factura_a_cliente(cedula, factura)

    print("Factura creada exitosamente.")
    mostrar_factura(factura)
