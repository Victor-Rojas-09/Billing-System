"""
Pruebas unitarias del directorio CRUD.
"""

import pytest
from datetime import date

from crud.clientes_crud import (
    crear_cliente, obtener_cliente, actualizar_cliente, eliminar_cliente,
    agregar_factura_a_cliente, buscar_por_cedula
)

from crud.productos_crud import registrar_producto, obtener_producto
from crud.facturas_crud import crear_factura

from model.control_plagas import ControlPlagas
from model.factura import Factura


# ------------------- CRUD CLIENTES -------------------

def test_crear_y_obtener_cliente():
    crear_cliente("Luis", "999")
    c = obtener_cliente("999")
    assert c.nombre == "Luis"


def test_cliente_duplicado():
    crear_cliente("Ana", "888")
    with pytest.raises(ValueError):
        crear_cliente("Ana2", "888")


def test_actualizar_cliente():
    crear_cliente("Pedro", "777")
    actualizar_cliente("777", "Pedro Gomez")
    c = obtener_cliente("777")
    assert c.nombre == "Pedro Gomez"


def test_eliminar_cliente():
    crear_cliente("Laura", "666")
    eliminar_cliente("666")
    assert obtener_cliente("666") is None


# ------------------ CRUD PRODUCTOS -------------------

def test_registrar_producto():
    p = ControlPlagas("ICA123", "PlagaTest", 10, 5, 25.0)
    registrar_producto(p)
    assert obtener_producto(p.id) == p


# -------------------- CRUD FACTURAS -------------------

def test_crear_factura():
    p = ControlPlagas("ICA321", "Producto X", 10, 5, 10.0)
    f = crear_factura(date.today(), [p])
    assert isinstance(f, Factura)
    assert f.valor_total == 10.0


# ---------------- ESPECIAL: buscar_por_cedula -------------------

def test_buscar_por_cedula():
    # Crear cliente y factura asociada
    c = crear_cliente("Mario", "555")
    p = ControlPlagas("ICA333", "PlagaZ", 15, 10, 30.0)
    factura = crear_factura(date.today(), [p])
    agregar_factura_a_cliente("555", factura)

    facturas = buscar_por_cedula("555")
    assert len(facturas) == 1
    assert facturas[0].valor_total == 30.0
