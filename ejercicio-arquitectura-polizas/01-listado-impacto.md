# Listado de Impacto — Solución de Pólizas de Inventario

## Contexto

Se requiere construir/ampliar la solución de tienda para permitir la **generación,
actualización y eliminación de pólizas** de inventario (faltante, sobrante, dañado,
incompleto), afectando el stock del centro y cargando la responsabilidad de pago
al empleado y centro correspondientes cuando aplique.

## Reglas de negocio consideradas

| Tipo de póliza | Movimiento de inventario | ¿Genera cargo al empleado? |
|---|---|---|
| Sobrante | Entrada | No |
| Faltante | Salida | Sí |
| Dañado | Salida | Sí |
| Incompleto | Salida | Sí |

## Componentes Front-end

| Componente | Tipo | Descripción |
|---|---|---|
| Módulo "Pólizas de Inventario" (listado, alta, edición, baja) | Nuevo | Pantalla principal para captura y gestión de pólizas |
| Formulario de captura de póliza | Nuevo | Selección de tipo de póliza, artículos, cantidades, empleado responsable y centro |
| Componente de confirmación de eliminación | Nuevo | Modal de confirmación antes de eliminar una póliza |
| Selector de artículos (buscador/autocomplete) | Nuevo | Búsqueda de artículos del catálogo para el detalle de la póliza |
| Vista de detalle/histórico de póliza | Nuevo | Consulta de una póliza ya generada y sus movimientos asociados |
| Menú de navegación / módulo de tienda existente | Modificado | Agregar acceso al nuevo módulo de Pólizas |
| Servicio de autenticación/sesión del portal de tienda | Modificado | Reutilizar sesión existente para validar permisos sobre el módulo |

## Componentes Back-end

| Componente | Tipo | Descripción |
|---|---|---|
| `PolizaService` (API) | Nuevo | Expone endpoints CRUD de pólizas (crear, consultar, actualizar, eliminar) |
| `PolizaValidator` | Nuevo | Valida reglas de negocio (tipo de póliza, existencia de artículo, stock disponible en caso de salida) |
| `InventoryService` — endpoint de afectación de stock | Modificado | Se agrega operación de ajuste de inventario (entrada/salida) invocada desde `PolizaService` |
| `EmployeeChargeService` | Nuevo | Registra el cargo pendiente de pago al empleado/centro responsable cuando el tipo de póliza lo requiere |
| `EmployeeService` / `CenterService` (consulta de catálogos) | Existente sin cambios | Se consume para validar empleado y centro al momento de generar la póliza |
| API Gateway / capa de enrutamiento | Modificado | Se agregan rutas nuevas del módulo de Pólizas y se aplican políticas de autorización |
| Módulo de auditoría / bitácora de cambios | Nuevo | Registra alta, edición y eliminación de pólizas (quién, cuándo, qué cambió) |

## Componentes de Base de Datos

| Componente | Tipo | Descripción |
|---|---|---|
| Tabla `Poliza` | Nueva | Encabezado de la póliza (tipo, fecha, empleado, centro, estatus) |
| Tabla `PolizaDetalle` | Nueva | Detalle de artículos, cantidades e importes de cada póliza |
| Tabla `TipoPoliza` (catálogo) | Nueva | Catálogo de tipos de póliza y su comportamiento (genera cargo, tipo de movimiento) |
| Tabla `MovimientoInventario` | Nueva | Bitácora de movimientos de entrada/salida generados a partir de una póliza |
| Tabla `CargoEmpleado` | Nueva | Registro del importe a cargo del empleado/centro derivado de una póliza |
| Tabla `Inventario` (stock por centro/artículo) | Modificada | Se actualiza el stock disponible a partir de los movimientos generados |
| Tablas `Empleado` / `Centro` / `Articulo` | Existentes sin cambios | Se referencian como llaves foráneas desde las tablas nuevas |
| Procedimiento almacenado / transacción `sp_AplicarMovimientoPoliza` | Nuevo | Encapsula en una sola transacción: alta de póliza, detalle, movimiento de inventario y cargo al empleado |
| Índices sobre `Poliza(id_centro, fecha_creacion)` y `MovimientoInventario(id_articulo, id_centro)` | Nuevos | Soportar las altas cargas de transacciones y consultas por centro/fecha |

## Resumen de impacto

- **Front-end:** 5 componentes nuevos, 2 modificados.
- **Back-end:** 4 componentes nuevos, 2 modificados, 2 reutilizados sin cambio.
- **Base de datos:** 5 tablas nuevas, 1 tabla modificada, 3 tablas reutilizadas, 1 procedimiento transaccional nuevo, 2 índices nuevos.
