"""
Módulo: fertilizante
Clase para productos del tipo fertilizante.
"""

from datetime import date
from .producto_control import ProductoControl


class Fertilizante(ProductoControl):
    """
    Modelo de un fertilizante agrícola.
    """

    def __init__(self, registro_ica: str, nombre: str, frecuencia_aplicacion: int,
                 fecha_ultima_aplicacion: date, precio: float) -> None:
        super().__init__(registro_ica, nombre, frecuencia_aplicacion, precio)
        self.fecha_ultima_aplicacion = fecha_ultima_aplicacion

    # -------------------- PROPIEDADES --------------------

    @property
    def fecha_ultima_aplicacion(self) -> date:
        return self._fecha_ultima_aplicacion

    @fecha_ultima_aplicacion.setter
    def fecha_ultima_aplicacion(self, valor: date) -> None:
        if not isinstance(valor, date):
            raise ValueError("La fecha de última aplicación debe ser un objeto date válido.")
        self._fecha_ultima_aplicacion = valor

    # -------------------- MÉTODOS --------------------

    def __repr__(self) -> str:
        return (
            f"Fertilizante(ID={self.id}, Nombre='{self.nombre}', "
            f"Registro_ICA='{self.registro_ica}', Frecuencia={self.frecuencia_aplicacion} días, "
            f"Fecha_ultima={self.fecha_ultima_aplicacion}, Precio={self.precio})"
        )