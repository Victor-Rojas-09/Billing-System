"""
Pruebas unitarias del paquete model.
"""

import pytest
from datetime import date
from Model.producto import Producto
from Model.producto_control import ProductoControl
from Model.control_plagas import ControlPlagas
from Model.fertilizante import Fertilizante
from Model.antibiotico import Antibiotico, TipoAnimal
from Model.factura import Factura
from Model.cliente import Cliente


#  PRUEBAS PRODUCTO

def test_producto_no_permite_instancia_directa():
    """
    Producto es abstracta y no debe poder instanciarse.
    """
    with pytest.raises(TypeError):
        Producto("Genérico", 10.0)


#  PRUEBAS PRODUCTO CONTROL

def test_producto_control_creacion_correcta():
    pc = ProductoControl("ICA123", "Control Base", 15, 100.0)
    assert pc.nombre == "Control Base"
    assert pc.registro_ica == "ICA123"
    assert pc.frecuencia_aplicacion == 15
    assert pc.precio == 100.0


def test_producto_control_frecuencia_invalida():
    with pytest.raises(ValueError):
        ProductoControl("ICA999", "Control", -5, 100.0)


#  PRUEBAS CONTROL DE PLAGAS

def test_control_plagas_creacion():
    p = ControlPlagas("ICA111", "Plagas X", 30, 20, 80.0)
    assert p.periodo_de_carencia == 20


def test_control_plagas_carencia_invalida():
    with pytest.raises(ValueError):
        ControlPlagas("ICA111", "Plagas X", 30, -1, 80.0)


#  PRUEBAS FERTILIZANTE

def test_fertilizante_creacion():
    f = Fertilizante("ICA222", "Ferti Y", 45, date.today(), 50.0)
    assert f.frecuencia_aplicacion == 45
    assert isinstance(f.fecha_ultima_aplicacion, date)


#  PRUEBAS ANTIBIOTICO

def test_antibiotico_creacion_correcta():
    a = Antibiotico("Antibio", 450, TipoAnimal.BOVINO, 120.0)
    assert a.dosis == 450
    assert a.tipo_animal == TipoAnimal.BOVINO


def test_antibiotico_dosis_incorrecta():
    with pytest.raises(ValueError):
        Antibiotico("Antibio", 200, TipoAnimal.BOVINO, 100.0)


def test_antibiotico_tipo_incorrecto():
    with pytest.raises(ValueError):
        Antibiotico("Antibio", 450, "PERRO", 100.0)


#  PRUEBAS FACTURA

def test_factura_calcula_total():
    p1 = ControlPlagas("ICA111", "PlagaX", 20, 10, 30.0)
    p2 = ControlPlagas("ICA333", "PlagaY", 20, 10, 20.0)

    f = Factura(date.today(), [p1, p2])
    assert f.valor_total == 50.0


def test_factura_agregar_producto():
    p = ControlPlagas("ICA999", "PlagaZ", 15, 8, 40.0)
    f = Factura(date.today(), [])

    f.agregar_producto(p)
    assert len(f.productos) == 1
    assert f.valor_total == 40.0


#  PRUEBAS CLIENTE

def test_cliente_agregar_factura():
    c = Cliente("Juan", "123")
    factura = Factura(date.today(), [])

    c.agregar_factura(factura)
    assert len(c.facturas) == 1