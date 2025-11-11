"""
Module: cliente.py
Este modulo implementa la clase Cliente.
"""

from typing import List
from .factura import Factura


class Cliente:
    """
    Modelo que representa a un cliente, quien puede tener múltiples facturas.
    """

    def __init__(self, nombre: str, cedula: str) -> None:
        self.nombre = nombre
        self.cedula = cedula
        self._facturas: List[Factura] = []

    #  PROPIEDADES

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not valor or not isinstance(valor, str):
            raise ValueError("El nombre debe ser un texto válido.")
        self._nombre = valor

    @property
    def cedula(self) -> str:
        return self._cedula

    @cedula.setter
    def cedula(self, valor: str) -> None:
        if not valor or not isinstance(valor, str):
            raise ValueError("La cédula debe ser un texto válido.")
        self._cedula = valor

    @property
    def facturas(self) -> List[Factura]:
        return self._facturas

    # -------------------- MÉTODOS --------------------

    def agregar_factura(self, factura: Factura) -> None:
        """
        Agrega una factura al cliente.
        """
        if not isinstance(factura, Factura):
            raise TypeError("Solo se pueden agregar objetos de tipo Factura.")
        self._facturas.append(factura)

    def listar_facturas(self) -> List[Factura]:
        """
        Retorna la lista completa de facturas asociadas al cliente.
        """
        return self._facturas

    def __repr__(self) -> str:
        return (
            f"Cliente(Nombre='{self.nombre}', Cédula='{self.cedula}', "
            f"Facturas={len(self.facturas)})"
        )