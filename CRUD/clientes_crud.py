"""
Module: clientes_crud.py
Contiene las operaciones CRUD para clientes del sistema.
La persistencia se maneja en memoria mediante un diccionario.
"""

from typing import Dict, List, Optional
from Model.cliente import Cliente
from Model.factura import Factura

# Base de datos en memoria
_clientes: Dict[str, Cliente] = {}

#  CLIENTES

def crear_cliente(nombre: str, cedula: str) -> Cliente:
    """
    Crea un nuevo cliente y lo almacena en memoria.
    """
    if cedula in _clientes:
        raise ValueError(f"Ya existe un cliente con la cédula {cedula}.")

    cliente = Cliente(nombre, cedula)
    _clientes[cedula] = cliente
    return cliente


def obtener_cliente(cedula: str) -> Optional[Cliente]:
    """
    Obtiene un cliente por su cédula.
    """
    return _clientes.get(cedula)


def actualizar_cliente(cedula: str, nuevo_nombre: Optional[str] = None) -> Cliente:
    """
    Actualiza el nombre de un cliente existente.
    """
    cliente = obtener_cliente(cedula)
    if not cliente:
        raise ValueError("No existe un cliente con esa cédula.")

    if nuevo_nombre:
        cliente.nombre = nuevo_nombre

    return cliente


def eliminar_cliente(cedula: str) -> None:
    """
    Elimina un cliente del sistema.
    """
    if cedula not in _clientes:
        raise ValueError("No existe un cliente con esa cédula.")

    del _clientes[cedula]

#  OPERACIONES ESPECIALES

def agregar_factura_a_cliente(cedula: str, factura: Factura) -> None:
    """
    Agrega una factura a un cliente específico.
    """
    cliente = obtener_cliente(cedula)
    if not cliente:
        raise ValueError("No existe un cliente con esa cédula.")

    cliente.agregar_factura(factura)


def buscar_por_cedula(cedula: str) -> List[Factura]:
    """
    Devuelve todas las facturas asociadas a un cliente,
    según lo requerido en el proyecto.
    """
    cliente = obtener_cliente(cedula)
    if not cliente:
        raise ValueError("No existe un cliente con esa cédula.")

    return cliente.listar_facturas()

#  UTILIDADES

def listar_clientes() -> List[Cliente]:
    """
    Retorna todos los clientes del sistema.
    """
    return list(_clientes.values())