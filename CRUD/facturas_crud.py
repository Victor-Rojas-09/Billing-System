"""
Módulo: facturas_crud
Administra la creación y consulta de facturas.
"""

from typing import Dict, List, Optional
from datetime import date
from model.factura import Factura
from model.producto import Producto

# Almacenamiento en memoria
_facturas: Dict[int, Factura] = {}
_contador_facturas = 1


# ------------------ CRUD DE FACTURAS ------------------

def crear_factura(fecha: date, productos: List[Producto]) -> Factura:
    """
    Crea una factura nueva y la almacena.
    """
    global _contador_facturas

    factura = Factura(fecha, productos)
    factura_id = _contador_facturas

    _facturas[factura_id] = factura
    _contador_facturas += 1

    return factura


def obtener_factura(id_factura: int) -> Optional[Factura]:
    """
    Obtiene una factura por su ID.
    """
    return _facturas.get(id_factura)


def listar_facturas() -> List[Factura]:
    """
    Retorna todas las facturas registradas.
    """
    return list(_facturas.values())