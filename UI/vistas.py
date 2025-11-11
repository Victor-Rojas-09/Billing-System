"""
Module: vistas.py
Contiene funciones que muestran información al usuario.
No incluye ninguna lógica de negocio ni lógica CRUD.
"""

from typing import List
from Model.cliente import Cliente
from Model.factura import Factura
from Model.producto import Producto


#  VISTAS DE CLIENTES

def mostrar_cliente(cliente: Cliente) -> None:
    """
    Muestra la información básica de un cliente.
    """
    print(f"\n--- Cliente ---")
    print(f"Nombre : {cliente.nombre}")
    print(f"Cédula : {cliente.cedula}")
    print(f"Facturas registradas : {len(cliente.facturas)}")


def mostrar_lista_clientes(clientes: List[Cliente]) -> None:
    """
    Muestra una lista de clientes.
    """
    print("\n--- Lista de clientes ---")
    if not clientes:
        print("No hay clientes registrados.")
        return

    for c in clientes:
        print(f"- {c.nombre} (Cédula: {c.cedula}) — Facturas: {len(c.facturas)}")


#  VISTAS DE PRODUCTOS

def mostrar_producto(producto: Producto) -> None:
    """
    Muestra la información de un producto genérico.
    """
    print("\n--- Producto ---")
    print(repr(producto))


def mostrar_lista_productos(productos: List[Producto]) -> None:
    """
    Muestra una lista de productos.
    """
    print("\n--- Lista de productos ---")
    if not productos:
        print("No hay productos registrados.")
        return

    for p in productos:
        print(f"- {repr(p)}")


#  VISTAS DE FACTURAS

def mostrar_factura(factura: Factura) -> None:
    """
    Muestra la información completa de una factura.
    """
    print("\n--- Factura ---")
    print(f"Fecha: {factura.fecha}")
    print(f"Productos: {len(factura.productos)}")
    print(f"Valor total: {factura.valor_total}")

    print("\nDetalle de productos:")
    for producto in factura.productos:
        print(f"  - {repr(producto)}")


def mostrar_lista_facturas(facturas: List[Factura]) -> None:
    """
    Muestra todas las facturas de un cliente o del sistema.
    """
    print("\n--- Lista de facturas ---")

    if not facturas:
        print("No hay facturas registradas.")
        return

    for i, factura in enumerate(facturas, start=1):
        print(f"\nFactura #{i}:")
        mostrar_factura(factura)