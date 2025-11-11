from .clientes_crud import (
    crear_cliente,
    obtener_cliente,
    actualizar_cliente,
    eliminar_cliente,
    agregar_factura_a_cliente,
    buscar_por_cedula,
    listar_clientes
)

from .productos_crud import (
    registrar_producto,
    obtener_producto,
    eliminar_producto,
    listar_productos
)

from .facturas_crud import (
    crear_factura,
    obtener_factura,
    listar_facturas
)

__all__ = [
    # clientes
    "crear_cliente",
    "obtener_cliente",
    "actualizar_cliente",
    "eliminar_cliente",
    "agregar_factura_a_cliente",
    "buscar_por_cedula",
    "listar_clientes",

    # productos
    "registrar_producto",
    "obtener_producto",
    "eliminar_producto",
    "listar_productos",

    # facturas
    "crear_factura",
    "obtener_factura",
    "listar_facturas",
]