"""
Módulo: antibiotico
Define la clase Antibiotico y la enumeración TipoAnimal.
"""

from enum import Enum
from .producto import Producto


class TipoAnimal(Enum):
    """
    Enumeración que representa el tipo de animal para el cual se usa el antibiótico.
    """
    BOVINO = "BOVINO"
    CAPRINO = "CAPRINO"
    PORCINO = "PORCINO"


class Antibiotico(Producto):
    """
    Modelo de un antibiótico veterinario.
    Incluye dosis (validada entre 400 y 600 kg) y tipo de animal.
    """

    def __init__(self, nombre: str, dosis: float, tipo_animal: TipoAnimal, precio: float) -> None:
        super().__init__(nombre, precio)
        self.dosis = dosis
        self.tipo_animal = tipo_animal

    # -------------------- PROPIEDADES --------------------

    @property
    def dosis(self) -> float:
        return self._dosis

    @dosis.setter
    def dosis(self, valor: float) -> None:
        if not isinstance(valor, (int, float)):
            raise TypeError("La dosis debe ser un número.")
        if valor < 400 or valor > 600:
            raise ValueError("La dosis debe estar entre 400 y 600 kg.")
        self._dosis = float(valor)

    @property
    def tipo_animal(self) -> TipoAnimal:
        return self._tipo_animal

    @tipo_animal.setter
    def tipo_animal(self, valor: TipoAnimal) -> None:
        if not isinstance(valor, TipoAnimal):
            raise ValueError("El tipo de animal debe ser una instancia de TipoAnimal.")
        self._tipo_animal = valor

    # -------------------- MÉTODOS --------------------

    def __repr__(self) -> str:
        return (
            f"Antibiotico(ID={self.id}, Nombre='{self.nombre}', "
            f"Dosis={self.dosis}kg, Tipo='{self.tipo_animal.value}', Precio={self.precio})"
        )