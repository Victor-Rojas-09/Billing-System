"""
Módulo: control_plagas
Clase para productos de control de plagas.
"""

from .producto_control import ProductoControl


class ControlPlagas(ProductoControl):
    """
    Modelo de un producto para control de plagas.
    """

    def __init__(self, registro_ica: str, nombre: str, frecuencia_aplicacion: int,
                 periodo_de_carencia: int, precio: float) -> None:
        super().__init__(registro_ica, nombre, frecuencia_aplicacion, precio)
        self.periodo_de_carencia = periodo_de_carencia

    # -------------------- PROPIEDADES --------------------

    @property
    def periodo_de_carencia(self) -> int:
        return self._periodo_de_carencia

    @periodo_de_carencia.setter
    def periodo_de_carencia(self, valor: int) -> None:
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("El periodo de carencia debe ser un número entero mayor o igual a 0.")
        self._periodo_de_carencia = valor

    # -------------------- MÉTODOS --------------------

    def __repr__(self) -> str:
        return (
            f"ControlPlagas(ID={self.id}, Nombre='{self.nombre}', "
            f"Registro_ICA='{self.registro_ica}', Frecuencia={self.frecuencia_aplicacion} días, "
            f"Carencia={self.periodo_de_carencia} días, Precio={self.precio})"
        )