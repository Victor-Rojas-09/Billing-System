"""
Module: factura.py
Este modulo implementa la clase Factura.
"""

from datetime import date
from typing import List
from .producto import Producto


class Factura:
    """
    Modelo de una factura que contiene productos comprados por un cliente.
    """

    def __init__(self, fecha: date, productos: List[Producto]) -> None:
        self.fecha = fecha
        self.productos = productos
        self._valor_total = self.calcular_total()

    #  PROPIEDADES

    @property
    def fecha(self) -> date:
        return self._fecha

    @fecha.setter
    def fecha(self, valor: date) -> None:
        if not isinstance(valor, date):
            raise ValueError("La fecha debe ser un objeto date válido.")
        self._fecha = valor

    @property
    def productos(self) -> List[Producto]:
        return self._productos

    @productos.setter
    def productos(self, lista: List[Producto]) -> None:
        if not isinstance(lista, list):
            raise ValueError("Los productos deben almacenarse en una lista.")
        if not all(isinstance(p, Producto) for p in lista):
            raise ValueError("Todos los elementos deben ser instancias de Producto.")
        self._productos = lista

    @property
    def valor_total(self) -> float:
        return self._valor_total

    #  METODOS

    def agregar_producto(self, producto: Producto) -> None:
        """
        Agrega un producto a la factura y actualiza el total.
        """
        if not isinstance(producto, Producto):
            raise TypeError("El elemento agregado debe ser un Producto.")
        self._productos.append(producto)
        self._valor_total = self.calcular_total()

    def calcular_total(self) -> float:
        """
        Calcula el valor total de la factura sumando los precios de los productos.
        """
        return sum(p.precio for p in self._productos)

    def __repr__(self) -> str:
        return (
            f"Factura(Fecha={self.fecha}, Productos={len(self.productos)}, "
            f"Valor_total={self.valor_total})"
        )