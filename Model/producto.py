"""
Módulo: producto
Clase base abstracta para todos los productos del sistema.
"""

from abc import ABC, abstractmethod
import uuid


class Producto(ABC):
    """
    Clase abstracta que representa un producto general.
    Contiene atributos comunes a todos los tipos de productos.
    """

    def __init__(self, nombre: str, precio: float) -> None:
        self._id = str(uuid.uuid4())
        self.nombre = nombre
        self.precio = precio

    # -------------------- PROPIEDADES --------------------

    @property
    def id(self) -> str:
        """Identificador único del producto (solo lectura)."""
        return self._id

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not valor or not isinstance(valor, str):
            raise ValueError("El nombre del producto debe ser un texto no vacío.")
        self._nombre = valor

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float) -> None:
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("El precio debe ser un número mayor que cero.")
        self._precio = float(valor)

    # -------------------- MÉTODOS --------------------

    @abstractmethod
    def __repr__(self) -> str:
        """Representación legible del producto."""
        pass