#  Proyecto de Facturación Agrícola  
### Programación Orientada a Objetos — Herencia, Relaciones y Arquitectura por Capas

Este proyecto implemente un **sistema de facturación agrícola** utilizando **Programación Orientada a Objetos (POO)**, aplicando:

- Herencia  
- Relaciones entre clases  
- Composición y agregación  
- Buenas prácticas de arquitectura por capas  
- Separación clara entre Modelo, CRUD e Interfaz de Usuario  
- Pruebas unitarias y de integración con *pytest*  

El sistema permite gestionar **clientes**, **productos agrícolas** y **facturas**, aplicando las reglas del enunciado académico.

---

# Objetivo del Sistema

El proyecto simula el funcionamiento básico de una tienda agrícola:

- Registrar clientes  
- Registrar diferentes tipos de productos agrícolas  
- Crear facturas con múltiples productos  
- Buscar facturas por cédula del cliente  
- Mostrar listados del sistema  

El proyecto está diseñado con **arquitectura por capas**, lo que lo hace mantenible, escalable y fácil de depurar.

---

# Arquitectura del Proyecto

El sistema está dividido en cuatro capas principales:


### **1. Capa Model (Dominio)**
Contiene todas las clases del sistema, cada una en un archivo independiente:

- `Producto` (abstracta)  
- `ProductoControl`  
- `ControlPlagas`  
- `Fertilizante`  
- `Antibiotico` + `TipoAnimal` (Enum)  
- `Factura`  
- `Cliente`  

Se incluyen validaciones, setters/getters (`@property`) y composición:

- Un **Cliente** tiene muchas **Facturas**
- Una **Factura** contiene una lista de **Productos**

---

### **2. Capa CRUD**
Maneja la “persistencia” en memoria usando diccionarios.

- `clientes_crud.py`
- `productos_crud.py`
- `facturas_crud.py`

Funciones disponibles:

- Crear, obtener, actualizar y eliminar clientes
- Registrar y listar productos
- Crear y recuperar facturas
- **buscar_por_cedula()** → función especial pedida en el enunciado

---

### **3. Capa UI**
Interacción con el usuario por consola:

- `menu.py` → menú principal  
- `vistas.py` → funciones de visualización  

La UI **solo pide datos y llama al CRUD**.  
No contiene lógica del sistema.

---

### **4. Capa Test**
Pruebas usando `pytest`:

- `test_model.py` → pruebas a cada clase del modelo  
- `test_crud.py` → pruebas unitarias de CRUD  
- `test_integration.py` → prueba del flujo completo:  
  Cliente → Producto → Factura → Asociación  
