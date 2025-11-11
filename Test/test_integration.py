"""
Pruebas de integración del sistema completo.
"""

from datetime import date

from crud.clientes_crud import crear_cliente, agregar_factura_a_cliente, buscar_por_cedula
from crud.productos_crud import registrar_producto
from crud.facturas_crud import crear_factura

from model.control_plagas import ControlPlagas
from model.antibiotico import Antibiotico, TipoAnimal


def test_flujo_completo_cliente_producto_factura():
    # 1. Crear cliente
    cliente = crear_cliente("Carlos", "1010")
    assert cliente.cedula == "1010"

    # 2. Registrar productos
    p1 = ControlPlagas("ICA001", "PlagaA", 20, 10, 50.0)
    p2 = Antibiotico("AntibioX", 450, TipoAnimal.BOVINO, 120.0)

    registrar_producto(p1)
    registrar_producto(p2)

    # 3. Crear factura
    factura = crear_factura(date.today(), [p1, p2])
    valor = p1.precio + p2.precio
    assert factura.valor_total == valor

    # 4. Asociar factura al cliente
    agregar_factura_a_cliente("1010", factura)

    # 5. Recuperar facturas del cliente y validar
    facturas = buscar_por_cedula("1010")

    assert len(facturas) == 1
    assert facturas[0].valor_total == valor
    assert len(facturas[0].productos) == 2
