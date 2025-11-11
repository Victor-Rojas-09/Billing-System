"""
Module: productos_crud.py
Administra el registro, consulta y eliminación de productos en memoria.
"""

from typing import Dict, List, Optional
from Model.producto import Producto

# Almacenamiento en memoria: map id -> Producto
_productos: Dict[str, Producto] = {}


def registrar_producto(producto: Producto) -> None:
    """
    Registra un producto en el sistema en memoria.
    Lanza ValueError si ya existe un producto con el mismo id.
    """
    if not isinstance(producto, Producto):
        raise TypeError("Se debe proporcionar una instancia de Producto.")

    if producto.id in _productos:
        raise ValueError(f"Ya existe un producto con ID {producto.id}")

    _productos[producto.id] = producto


def obtener_producto(id_producto: str) -> Optional[Producto]:
    """
    Devuelve el producto con el id especificado, o None si no existe.
    """
    if not isinstance(id_producto, str):
        raise TypeError("El id del producto debe ser una cadena.")
    return _productos.get(id_producto)


def listar_productos() -> List[Producto]:
    """
    Retorna la lista de todos los productos registrados.
    """
    return list(_productos.values())


def eliminar_producto(id_producto: str) -> None:
    """
    Elimina el producto con el id dado. Lanza ValueError si no existe.
    """
    if not isinstance(id_producto, str):
        raise TypeError("El id del producto debe ser una cadena.")

    if id_producto not in _productos:
        raise ValueError(f"No existe un producto con ID {id_producto}")

    del _productos[id_producto]


def actualizar_producto(producto: Producto) -> None:
    """
    Actualiza un producto existente (reemplaza por id).
    Lanza ValueError si no existe previamente.
    """
    if not isinstance(producto, Producto):
        raise TypeError("Se debe proporcionar una instancia de Producto.")

    if producto.id not in _productos:
        raise ValueError(f"No existe un producto con ID {producto.id} para actualizar.")

    _productos[producto.id] = producto
