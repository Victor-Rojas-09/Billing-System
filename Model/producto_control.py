"""
Módulo: producto_control
Clase intermedia para los productos de control agrícola.
"""

from .producto import Producto


class ProductoControl(Producto):
    """
    Clase base para productos de control (fertilizantes y control de plagas).
    """

    def __init__(self, registro_ica: str, nombre: str,
                 frecuencia_aplicacion: int, precio: float) -> None:
        super().__init__(nombre, precio)
        self.registro_ica = registro_ica
        self.frecuencia_aplicacion = frecuencia_aplicacion

    # -------------------- PROPIEDADES --------------------

    @property
    def registro_ica(self) -> str:
        return self._registro_ica

    @registro_ica.setter
    def registro_ica(self, valor: str) -> None:
        if not valor or not isinstance(valor, str):
            raise ValueError("El registro ICA debe ser un texto válido.")
        self._registro_ica = valor

    @property
    def frecuencia_aplicacion(self) -> int:
        return self._frecuencia_aplicacion

    @frecuencia_aplicacion.setter
    def frecuencia_aplicacion(self, valor: int) -> None:
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("La frecuencia de aplicación debe ser un número entero positivo.")
        self._frecuencia_aplicacion = valor

    # -------------------- MÉTODOS --------------------

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(ID={self.id}, Nombre='{self.nombre}', "
            f"Registro_ICA='{self.registro_ica}', Frec_aplic={self.frecuencia_aplicacion} días, "
            f"Precio={self.precio})"
        )