# Programa de Estudio — Preguntas de Entrevista para Arquitectura de Tecnología

Programa de estudio basado en el banco de **60 preguntas** de
[`architectural-interview-questions.json`](architectural-interview-questions.json) y en el
caso práctico [Pólizas de Inventario](ejercicio-arquitectura-polizas/01-listado-impacto.md).

El objetivo no es memorizar respuestas, sino poder **explicar cada concepto, comparar
alternativas y justificar decisiones con trade-offs** en una entrevista de Arquitecto de
Software / Ingeniero Senior.

## Contenido

1. Resumen del proyecto y alcance
2. Método de estudio
3. Mapa de cobertura de las 60 preguntas
4. Plan de 6 semanas
5. Lecciones (15)
6. Chuleta de comparaciones
7. Cómo responder en una entrevista
8. Simulacros y registro de errores
9. Checklist de cobertura
10. Glosario de siglas
11. Recursos del repositorio

---

## 1. Resumen del proyecto y alcance

El repositorio contiene cuatro piezas que se complementan:

| Recurso                                  | Qué aporta                                                                                           | Cómo usarlo                                 |
|------------------------------------------|------------------------------------------------------------------------------------------------------|---------------------------------------------|
| `README.md`                              | Las 60 preguntas con respuesta y explicación detallada                                               | Lectura de referencia                       |
| `architectural-interview-questions.json` | Banco estructurado por nivel, categoría y explicación                                                | Fuente de la app y de este programa         |
| `self-test-app/`                         | Quiz de consola y quiz gráfico (completo, rápido, personalizado, por nivel/categoría y modo estudio) | Diagnóstico, práctica y simulacros          |
| `ejercicio-arquitectura-polizas/`        | Caso real: pólizas de inventario, arquitectura general, tecnológica, secuencia y datos               | Aplicar cada concepto a un sistema concreto |

El banco cubre tres niveles:

- **Básico (preguntas 1–20):** fundamentos, principios, estilos clásicos, APIs, datos,
  escalabilidad y disponibilidad.
- **Intermedio (preguntas 21–40):** arquitecturas modernas, DDD, resiliencia, mensajería,
  contenedores, Kubernetes y serverless.
- **Avanzado (preguntas 41–60):** sistemas distribuidos, consistencia, seguridad,
  multi-tenancy, observabilidad, despliegues progresivos y arquitectura evolutiva.

Este programa reorganiza esos conceptos en **15 lecciones temáticas**. Cada pregunta del
banco aparece exactamente una vez en el mapa de cobertura, y la checklist final permite
verificar que no quede ningún concepto sin estudiar.

### Qué serás capaz de hacer al terminar

- Definir arquitectura, rol del arquitecto, stakeholders y documentación.
- Explicar y aplicar atributos de calidad, acoplamiento, cohesión y SOLID.
- Comparar estilos: capas, tres capas, cliente-servidor, MVC, monolito y microservicios.
- Diseñar APIs REST idempotentes y elegir entre bases relacionales y NoSQL.
- Escalar, balancear carga y usar caché con criterio.
- Elegir comunicación síncrona/asíncrona y modelos de mensajería.
- Aplicar arquitectura hexagonal, DDD, CQRS y Event Sourcing.
- Diseñar resiliencia con Circuit Breaker, Saga y Bulkhead.
- Entender API Gateway, Service Mesh, Sidecar, contenedores, Kubernetes y serverless.
- Razonar sobre CAP, consistencia eventual, consistent hashing, CRDTs y Kafka.
- Comparar 2PC vs Saga, backpressure, Lambda vs Kappa.
- Modernizar con Strangler Fig y desplegar con blue-green, canary y feature flags.
- Aplicar observabilidad, chaos engineering, fitness functions, Zero Trust, multi-tenancy,
  Data Mesh y TOGAF ADM.

---

## 2. Método de estudio

### 2.1 Diagnóstico inicial

Antes de empezar, ejecuta el quiz completo de consola:

```bash
python self-test-app/architecture_quiz_console.py
```

Registra:

- Puntaje total y por nivel.
- Preguntas falladas y, sobre todo, **por qué** fallaste.
- Conceptos que crees dominar pero no sabrías explicar en voz alta.

Interpretación sugerida:

| Resultado     | Punto de partida                                             |
|---------------|--------------------------------------------------------------|
| Menos de 60 % | Lecciones 1–15 en orden, sin saltos                          |
| 60–80 %       | Repaso rápido de L1–L6 y foco en L7–L15                      |
| Más de 80 %   | Empezar en L7; usar L1–L6 solo para vocabulario y simulacros |

### 2.2 Ciclo de cada lección (90 minutos)

1. **Recuperación activa (10 min):** sin apuntes, escribe o di en voz alta lo que recuerdas
   de la lección anterior.
2. **Lectura activa (25 min):** lee la lección y subraya definiciones, comparaciones y
   trade-offs.
3. **Conexión con el caso Pólizas (15 min):** identifica cómo aplicaría el concepto al
   ejercicio del repositorio.
4. **Práctica (25 min):** responde las preguntas del banco asociadas y explica por qué las
   otras opciones son incorrectas.
5. **Cierre (10 min):** escribe un resumen de 60 segundos y actualiza el registro de errores.

### 2.3 Repaso espaciado

Cada lección se repasa en cinco momentos:

| Momento | Qué repasar                                |
|---------|--------------------------------------------|
| Día 1   | Resumen propio y definiciones              |
| Día 3   | Comparaciones y tablas                     |
| Día 7   | Preguntas del banco asociadas              |
| Día 14  | Explicación en voz alta sin apuntes        |
| Día 30  | Simulacro o pregunta de entrevista abierta |

Una forma simple: usa tarjetas con una pregunta conceptual en el anverso y la explicación
con un ejemplo en el reverso. No copies la respuesta literal del banco; reformúlala.

### 2.4 Registro de errores

Cada fallo se convierte en una tarjeta de estudio. Plantilla:

| Fecha | Pregunta | Concepto | Por qué fallé | Corrección | Repaso 1 | Repaso 2 |
|-------|----------|----------|---------------|------------|----------|----------|
|       |          |          |               |            |          |          |

Clasifica el error:

- **Concepto:** no conocía el tema.
- **Confusión:** confundí dos conceptos parecidos (por ejemplo, CQRS vs Event Sourcing).
- **Lectura:** la opción correcta estaba bien, pero interpreté mal el enunciado.
- **Descarte:** no supe eliminar distractores.

### 2.5 Ritmos posibles

| Ritmo     | Duración  | Dedicación     | Recomendado para                    |
|-----------|-----------|----------------|-------------------------------------|
| Estándar  | 6 semanas | 5–6 h/semana   | Compatible con trabajo              |
| Intensivo | 3 semanas | 10–12 h/semana | Entrevista próxima                  |
| Repaso    | 1 semana  | 8–10 h total   | Ya tienes base; solo puntos débiles |

El programa completo requiere aproximadamente **32 horas**: 22.5 h de lecciones, 4.5 h de
repasos, 4.5 h de simulacros y 1 h de entrevista simulada.

---

## 3. Mapa de cobertura de las 60 preguntas

| Lección | Preguntas                  | Nivel               | Conceptos centrales                                   | Tiempo |
|---------|----------------------------|---------------------|-------------------------------------------------------|--------|
| L1      | 1, 2, 4, 18                | Básico              | Arquitectura, diseño, stakeholders, C4/ADRs           | 90 min |
| L2      | 3, 17, 19                  | Básico              | Atributos de calidad, alta disponibilidad, SPOF       | 90 min |
| L3      | 8, 9, 10, 11, 12           | Básico              | SRP, OCP, acoplamiento, cohesión, SoC                 | 90 min |
| L4      | 5, 6, 7, 15, 20            | Básico              | Capas, tres capas, cliente-servidor, MVC, monolito    | 90 min |
| L5      | 13, 14                     | Básico              | REST idempotente, relacional vs NoSQL                 | 90 min |
| L6      | 16, 32, 33                 | Básico/Intermedio   | Escalabilidad, balanceo, caché                        | 90 min |
| L7      | 21, 31, 34                 | Intermedio          | EDA, síncrono/asíncrono, colas vs pub/sub             | 90 min |
| L8      | 22, 25, 26                 | Intermedio          | Hexagonal, Bounded Context, Aggregate                 | 90 min |
| L9      | 23, 24                     | Intermedio          | CQRS, Event Sourcing                                  | 90 min |
| L10     | 27, 28, 55                 | Intermedio/Avanzado | Circuit Breaker, Saga, Bulkhead                       | 90 min |
| L11     | 29, 30, 38, 39, 40, 43, 49 | Intermedio/Avanzado | Gateway, mesh, sidecar, contenedores, K8s, serverless | 90 min |
| L12     | 35, 36, 41, 42, 46, 50     | Intermedio/Avanzado | CAP, consistencia, hashing, CRDTs, Kafka              | 90 min |
| L13     | 44, 45, 56                 | Avanzado            | Backpressure, 2PC vs Saga, Lambda vs Kappa            | 90 min |
| L14     | 37, 47, 48, 54, 57, 59, 60 | Intermedio/Avanzado | Strangler, despliegues, caos, observabilidad, fitness | 90 min |
| L15     | 51, 52, 53, 58             | Avanzado            | Zero Trust, multi-tenant, Data Mesh, TOGAF            | 90 min |

**Verificación:** L1–L6 cubren las preguntas 1–20; L7–L15 cubren las preguntas 21–60.
Cada ID del 1 al 60 aparece exactamente una vez.

---

## 4. Plan de 6 semanas

| Semana | Sesiones | Contenido                                                        | Entregable                                  |
|--------|----------|------------------------------------------------------------------|---------------------------------------------|
| 1      | 3        | L1, L2, L3                                                       | Resumen de fundamentos + 10 tarjetas        |
| 2      | 3        | L4, L5, L6                                                       | Simulacro de preguntas 1–20; meta ≥ 16/20   |
| 3      | 3        | L7, L8, L9                                                       | Diagrama hexagonal/DDD del caso Pólizas     |
| 4      | 3        | L10, L11, L12                                                    | Simulacro de preguntas 21–50; meta ≥ 80 %   |
| 5      | 3        | L13, L14, L15                                                    | Tabla de decisiones del caso Pólizas        |
| 6      | 3        | Repaso de errores + 2 simulacros completos + entrevista simulada | Puntaje ≥ 80 % y registro de errores limpio |

Sugerencia de distribución semanal:

- **Sesión 1:** lección nueva + preguntas del banco.
- **Sesión 2:** lección nueva + repaso espaciado de la anterior.
- **Sesión 3:** lección nueva + mini-simulacro o explicación en voz alta.

Si eliges el ritmo intensivo, haz una lección por día y dedica el día 6 a repasar errores;
el día 7, a un simulacro.

---

## 5. Lecciones

### Módulo I — Fundamentos y estilos clásicos

#### Lección 1 — Qué es arquitectura, rol del arquitecto y documentación

**Objetivo:** definir arquitectura con precisión, distinguirla del diseño, identificar
stakeholders y comunicar decisiones con diagramas C4 y ADRs.

**Preguntas del banco:** 1, 2, 4, 18.

##### 1.1 Definición operativa

La arquitectura de software es el conjunto de **decisiones estructurales fundamentales**
sobre cómo se organiza un sistema: sus componentes principales, las relaciones entre ellos
y los principios que guían su diseño y evolución. Son decisiones **caras de cambiar** y que
condicionan los atributos de calidad.

No es un diagrama, no es el código y no es una fase inicial. Un diagrama es una **vista** de
la arquitectura; el código es una **implementación** de ella. La arquitectura existe aunque
no esté documentada; documentarla sirve para explicar el **por qué** y facilitar el cambio.

Ejemplos de decisiones arquitectónicas:

- Monolito modular vs microservicios.
- Comunicación síncrona vs asíncrona.
- Base de datos relacional vs NoSQL.
- Modelo de tenancy: instancia dedicada vs multi-tenant.
- Modelo de seguridad: perímetro vs Zero Trust.
- Topología de despliegue: una región vs multi-región.

##### 1.2 Arquitectura vs diseño

| Criterio        | Arquitectura                                             | Diseño                                            |
|-----------------|----------------------------------------------------------|---------------------------------------------------|
| Alcance         | Todo el sistema o grandes partes                         | Un módulo, clase o componente                     |
| Coste de cambio | Alto; decisiones difíciles de revertir                   | Bajo; decisiones locales y reversibles            |
| Ejemplos        | Estilo, límites, tecnologías clave, atributos de calidad | Patrones de clase, estructura interna, algoritmos |
| Influencia      | Restringe el diseño posterior                            | Opera dentro de las restricciones arquitectónicas |

Grady Booch lo resume así: la arquitectura representa las **decisiones significativas que
son costosas de cambiar**. La frontera no es absoluta; es un continuo de alcance y coste.

##### 1.3 Stakeholders

Un stakeholder es cualquier persona o grupo con interés legítimo en el sistema o capacidad
de influir en sus decisiones.

| Stakeholder | Le preocupa | Cómo se le comunica |
|---|---|---|
| Usuarios finales | Usabilidad, rendimiento, disponibilidad | Demos, diagramas de contexto, SLAs |
| Producto / negocio | Time-to-market, alcance, coste | Roadmap, riesgos, trade-offs |
| Desarrollo | Mantenibilidad, testabilidad, claridad | Diagramas de componentes, ADRs, contratos |
| Operaciones | Despliegue, monitoreo, recuperación | Diagramas de despliegue, runbooks, SLOs |
| Seguridad | Vulnerabilidades, cumplimiento, acceso | Modelo de amenazas, diagramas de flujo |
| Gerencia | Coste, plazos, riesgo | Resúmenes ejecutivos, decisiones y consecuencias |

El arquitecto es un **mediador**: traduce intereses contrapuestos en decisiones explícitas
y documenta las razones. No decide en solitario ni impone tecnología sin contexto.

##### 1.4 Documentación: C4 y ADRs

El modelo **C4** propone cuatro niveles de zoom:

1. **Contexto:** el sistema y los actores/sistemas externos. Para audiencia no técnica.
2. **Contenedores:** aplicaciones, servicios, bases de datos y su comunicación. Para
   arquitectos y equipos técnicos.
3. **Componentes:** módulos dentro de un contenedor. Para desarrolladores.
4. **Código:** clases y relaciones. Opcional; suele generarse o no mantenerse.

Un **ADR** (Architecture Decision Record) registra una decisión: título, estado, contexto,
decisión y consecuencias. Es inmutable: si cambia la decisión, se crea otro ADR que
reemplaza al anterior. Sirve para preservar el contexto y evitar reabrir debates sin
información.

##### En la entrevista

- Empieza con una definición breve y añade "decisiones difíciles de cambiar".
- Da un ejemplo concreto y menciona un trade-off.
- Si te preguntan por la diferencia con un senior developer: el arquitecto trabaja con
  incertidumbre, límites del sistema, stakeholders y decisiones transversales; el senior
  developer profundiza en implementación y calidad local.
- Evita decir que la arquitectura es UML o que es sinónimo de microservicios.

##### Aplicación al caso Pólizas

Decisiones arquitectónicas del ejercicio: arquitectura general por capas con API Gateway;
base de datos relacional transaccional; despliegue en clúster con balanceador; separación
front-end/back-end; auditoría como módulo transversal. Decisiones de diseño: estructura de
`PolizaService`, validaciones, nombres de endpoints y forma de los DTOs.

##### Práctica de recuperación activa

1. Explica qué es arquitectura en 60 segundos, sin jerga.
2. Escribe cinco decisiones arquitectónicas y cinco de diseño para Pólizas.
3. Dibuja un C4 de contexto y otro de contenedores para Pólizas.
4. Redacta un ADR: "Usar una única base de datos relacional para las transacciones de
   pólizas en la primera versión".

- [ ] Puedo definir arquitectura y diferenciarla del diseño.
- [ ] Puedo identificar stakeholders y sus preocupaciones.
- [ ] Sé para qué sirven C4 y un ADR.

---

#### Lección 2 — Atributos de calidad, alta disponibilidad y SPOF

**Objetivo:** conectar requisitos no funcionales con decisiones arquitectónicas, diseñar
alta disponibilidad y detectar puntos únicos de falla.

**Preguntas del banco:** 3, 17, 19.

##### 2.1 Atributos de calidad

Los atributos de calidad (quality attributes) son propiedades **no funcionales** que
determinan qué tan bien el sistema cumple sus objetivos: rendimiento, disponibilidad,
escalabilidad, seguridad, mantenibilidad, testabilidad, usabilidad, recuperabilidad,
observabilidad, etc. También se llaman "-ilities".

No basta con nombrarlos: deben ser **medibles** mediante escenarios. Un escenario de
calidad tiene fuente, estímulo, artefacto, entorno, respuesta y medida.

Ejemplo para Pólizas: "Durante el pico de cierre de mes, con 500 solicitudes por minuto,
el 99 % de las creaciones de póliza debe completarse en menos de 800 ms y ningún movimiento
de inventario debe perderse".

Los atributos suelen entrar en conflicto:

| Trade-off | Ejemplo |
|---|---|
| Seguridad vs rendimiento | Cifrado y verificaciones adicionales añaden latencia |
| Consistencia vs disponibilidad | Una réplica puede responder con datos desactualizados |
| Coste vs resiliencia | Multi-región y redundancia duplican infraestructura |
| Mantenibilidad vs time-to-market | Abstracciones y pruebas cuestan tiempo inicial |
| Simplicidad vs escalabilidad | Un monolito es simple, pero escala como unidad |

La arquitectura consiste, en gran medida, en **negociar y documentar estos trade-offs**.

##### 2.2 Alta disponibilidad

La alta disponibilidad (HA) es la capacidad de permanecer operativo y accesible durante un
porcentaje muy alto del tiempo, minimizando el downtime. Se mide en "nueves":

| Disponibilidad | Downtime aproximado al año |
|---|---|
| 99 % | 3.65 días |
| 99.9 % | 8.76 horas |
| 99.99 % | 52.6 minutos |
| 99.999 % | 5.26 minutos |

Mecanismos habituales:

- **Redundancia:** varias instancias de cada componente crítico (activa-activa o
  activa-pasiva).
- **Balanceo de carga:** distribuye tráfico entre réplicas.
- **Health checks y failover:** detectan fallos y redirigen tráfico.
- **Multi-AZ / multi-región:** tolerancia a fallos de zona o región.
- **Degradación elegante:** mantener funciones esenciales aunque fallen las secundarias.
- **Backups y replicación:** protegen la durabilidad, no solo la disponibilidad.

Distinciones importantes:

- **Alta disponibilidad:** minimiza interrupciones; puede haber una breve pausa durante el
  failover.
- **Tolerancia a fallos:** el sistema sigue operando sin interrupción perceptible.
- **Durabilidad:** los datos sobreviven a fallos; se logra con backups, replicación y
  almacenamiento durable.

##### 2.3 Punto único de falla (SPOF)

Un SPOF es un componente cuyo fallo provoca la caída de todo el sistema o de una parte
crítica, porque no existe redundancia que lo reemplace.

Ejemplos típicos: una única base de datos primaria, un único balanceador, un único servidor
de autenticación, una única zona de disponibilidad, un DNS mal configurado o una única
cola sin réplicas.

Para eliminarlo: identificar dependencias, añadir réplicas, balanceadores redundantes,
failover automático y planes de recuperación. Cuidado: la redundancia puede **mover** el
SPOF (por ejemplo, un balanceador único delante de dos servidores sigue siendo un SPOF).
No existe disponibilidad infinita; se gestiona riesgo y coste.

##### En la entrevista

- Define HA con los nueves y explica redundancia, failover y eliminación de SPOF.
- Distingue HA de tolerancia a fallos y de durabilidad.
- Si te piden diseñar HA: empieza por RTO/RPO, identifica SPOFs, añade redundancia y
  **prueba** el failover.
- Menciona el coste: cada nueve adicional suele ser mucho más caro.

##### Aplicación al caso Pólizas

El ejercicio tiene balanceador, dos servidores web, dos servidores de aplicación, Redis y
una base de datos con primario y réplica. SPOFs restantes: el primario de base de datos
para escrituras, el balanceador si es único, Redis si se vuelve obligatorio y el DNS. Se
mitigan con failover, réplicas, caché tolerante a fallos y monitoreo.

##### Práctica de recuperación activa

1. Escribe un escenario de calidad medible para disponibilidad y otro para rendimiento.
2. Calcula el downtime anual de 99.95 %.
3. Identifica tres SPOFs en una arquitectura web típica y su mitigación.
4. Explica por qué backups no equivalen a alta disponibilidad.

- [ ] Puedo definir atributos de calidad y dar ejemplos medibles.
- [ ] Sé calcular y comparar nueves de disponibilidad.
- [ ] Puedo identificar SPOFs y proponer redundancia.

---

#### Lección 3 — Principios de diseño: SRP, OCP, acoplamiento, cohesión y SoC

**Objetivo:** aplicar principios de diseño a nivel de clase y de módulo, y reconocer sus
síntomas en un sistema real.

**Preguntas del banco:** 8, 9, 10, 11, 12.

##### 3.1 Single Responsibility Principle (SRP)

Una clase o módulo debe tener **una única razón para cambiar**, es decir, una sola
responsabilidad bien definida. "Razón para cambiar" suele estar ligada a un **actor** o
stakeholder: si dos personas distintas pueden pedir cambios por motivos distintos, hay dos
responsabilidades.

Ejemplo: una clase que calcula el total de una póliza y además la guarda en base de datos
tiene dos razones para cambiar: cambia una regla de negocio o cambia el esquema de
persistencia. SRP no significa "un método por clase"; significa una responsabilidad
cohesionada.

A nivel arquitectónico: módulos o servicios alineados con capacidades de negocio, no con
detalles técnicos.

##### 3.2 Open/Closed Principle (OCP)

Las entidades de software deben estar **abiertas a extensión y cerradas a modificación**.
Se añade comportamiento nuevo sin tocar el código existente y probado, normalmente mediante
interfaces, polimorfismo, Strategy, plugins o puntos de extensión.

Ejemplo: los tipos de póliza (faltante, sobrante, dañado, incompleto) pueden modelarse con
polimorfismo o un registro de estrategias; añadir un tipo nuevo no debería obligar a editar
un `switch` gigante en varios lugares.

Cuidado con la sobreabstracción: abstraer antes de conocer los cambios reales añade coste
y complejidad. OCP se aplica donde la variación es probable y valiosa.

##### 3.3 Acoplamiento

El acoplamiento mide el **grado de interdependencia** entre módulos. Un acoplamiento alto
implica que un cambio en un módulo probablemente obliga a cambiar el otro. El bajo
acoplamiento (loose coupling) permite modificar, probar o reemplazar un módulo sin afectar
a los demás.

Tipos y señales:

- Acoplamiento por implementación: depender de clases concretas y detalles internos.
- Acoplamiento temporal: el emisor espera la respuesta inmediata del receptor.
- Acoplamiento por datos compartidos: varios módulos escriben la misma tabla o estructura.
- Síntomas: cambios en cadena, pruebas frágiles, ciclos de dependencias, "shotgun surgery".

Herramientas para reducirlo: interfaces y contratos, inversión de dependencias, eventos,
módulos con límites claros y comunicación asíncrona cuando el acoplamiento temporal no es
necesario. No todo acoplamiento es malo: cierto grado es inevitable y necesario.

##### 3.4 Cohesión

La cohesión mide qué tan **relacionados funcionalmente** están los elementos dentro de un
módulo y si contribuyen a un propósito común. Una cohesión alta facilita entender, probar y
mantener el módulo; una cohesión baja indica una "bolsa de cosas" sin propósito claro.

Objetivo clásico: **alta cohesión dentro de cada módulo, bajo acoplamiento entre módulos**.
Así los cambios quedan contenidos y se propagan menos.

##### 3.5 Separation of Concerns (SoC)

Separar el sistema en secciones distintas, cada una encargada de una preocupación:
presentación, lógica de negocio, persistencia, validación, seguridad, etc. Los cambios en
una preocupación deben impactar mínimamente en las demás.

SoC subyace a capas, arquitectura hexagonal, MVC y microservicios. Las preocupaciones
transversales (logging, seguridad, métricas) se abordan con middleware, aspectos, filtros,
sidecars o service mesh, evitando duplicarlas en cada módulo.

##### 3.6 SOLID completo, por si preguntan

| Principio | Idea central |
|---|---|
| SRP | Una razón para cambiar |
| OCP | Extender sin modificar |
| LSP | Los subtipos deben poder sustituir a sus tipos base |
| ISP | Interfaces pequeñas y específicas; no obligar a implementar lo que no se usa |
| DIP | Depender de abstracciones, no de implementaciones concretas |

##### En la entrevista

- Define cada principio en una frase y añade un ejemplo.
- Conecta SRP/OCP con límites de módulos y servicios, no solo con clases.
- Menciona el coste de abstraer de más.
- Si te piden "alta cohesión y bajo acoplamiento", explica qué síntomas concretos se
  reducen.

##### Aplicación al caso Pólizas

`PolizaService` puede separar orquestación, validación de reglas, persistencia y
notificación. Los tipos de póliza son un candidato natural a Strategy/polimorfismo. La
persistencia debe depender de un repositorio/interfaz, no de detalles del motor de base de
datos. La auditoría es una preocupación transversal.

##### Práctica de recuperación activa

1. Encuentra dos responsabilidades mezcladas en un servicio que conozcas.
2. Propón cómo añadir un nuevo tipo de póliza sin modificar el código existente.
3. Explica la diferencia entre acoplamiento y cohesión con un ejemplo.
4. Identifica una preocupación transversal y cómo la separarías.

- [ ] Puedo definir SRP y OCP con ejemplos.
- [ ] Sé distinguir acoplamiento de cohesión.
- [ ] Puedo aplicar SoC a un sistema real.

---

#### Lección 4 — Estilos clásicos: capas, tres capas, cliente-servidor, MVC y monolito

**Objetivo:** comparar los estilos arquitectónicos clásicos y saber cuándo elegir cada uno.

**Preguntas del banco:** 5, 6, 7, 15, 20.

##### 4.1 Arquitectura en capas

Organiza el sistema en capas horizontales (presentación, lógica de negocio, acceso a datos),
donde cada capa expone servicios a la superior y consume servicios de la inferior. Puede
haber capas cerradas (solo se comunican con la adyacente) o relajadas (pueden saltar capas).

- **Ventajas:** simplicidad, separación de responsabilidades, aislamiento de cambios,
  facilidad para entender y probar.
- **Desventajas:** el anti-patrón **sinkhole** (llamadas que atraviesan capas sin lógica
  real), acoplamiento al orden de capas, escalabilidad como unidad y despliegue monolítico.
- **Uso típico:** aplicaciones empresariales, CRUD, equipos que necesitan una estructura
  conocida.

##### 4.2 Arquitectura de tres capas (three-tier)

Es una especialización **física** de las capas: presentación, lógica de negocio y datos se
despliegan en servidores o procesos separados y se comunican por red.

- **Ventajas:** escalar y actualizar cada capa por separado; aislar la base de datos;
  límites claros.
- **Desventajas:** latencia de red, más infraestructura y complejidad operativa.
- **Diferencia clave:** "capas" es una organización lógica; "tres capas" suele implicar
  despliegue físico separado.

##### 4.3 Cliente-servidor

El servidor centraliza recursos, datos o servicios; los clientes inician solicitudes y
consumen las respuestas. El cliente suele manejar la presentación.

- **Ventajas:** control centralizado de datos, mantenimiento y seguridad más simples.
- **Desventajas:** dependencia de la disponibilidad del servidor, posible cuello de botella
  y SPOF; se mitiga con balanceo, réplicas y caché.
- **Variantes:** cliente grueso (más lógica local) vs cliente delgado (más lógica en el
  servidor).

##### 4.4 Modelo-Vista-Controlador (MVC)

Separa la aplicación interactiva en tres componentes:

- **Modelo:** estado y reglas de negocio.
- **Vista:** representación al usuario.
- **Controlador:** recibe la entrada, actualiza el modelo y selecciona la vista.

Permite cambiar la interfaz sin tocar la lógica de negocio y viceversa. Ha inspirado MVP y
MVVM. MVC es un patrón de presentación/UI, no un estilo completo de sistema; suele
combinarse con capas. Error común: creer que toda la lógica debe vivir en el controlador.

##### 4.5 Monolito vs microservicios

| Criterio | Monolito | Microservicios |
|---|---|---|
| Unidad de despliegue | Una sola aplicación | Servicios independientes |
| Escalado | Toda la aplicación | Por servicio |
| Datos | Comúnmente una base compartida | Una base por servicio (ideal) |
| Acoplamiento | Alto si no se modulariza | Bajo en teoría; alto si se diseña mal |
| Autonomía de equipos | Limitada por el despliegue común | Alta, alineada a servicios |
| Complejidad operativa | Baja | Alta: red, observabilidad, despliegues |
| Consistencia | Transacciones locales simples | Transacciones distribuidas/Sagas |
| Latencia | Llamadas en proceso | Llamadas de red |
| Fallos | Un fallo puede tumbar todo | Aislables, pero con fallos parciales |

El **monolito modular** es un punto medio válido: un solo despliegue, pero módulos con
límites claros y bajo acoplamiento. Microservicios no es sinónimo de buena arquitectura;
exige madurez operativa, equipos autónomos y límites de dominio bien entendidos. Evita el
**monolito distribuido**: servicios desplegados por separado pero acoplados por una base de
datos compartida y despliegues coordinados.

##### En la entrevista

- No digas "microservicios son mejores"; explica contexto, escala, equipos y coste.
- Menciona el monolito modular como alternativa legítima.
- Si te piden elegir para Pólizas: empieza por monolito modular/N-tier; extrae servicios
  solo cuando haya una razón de escalado, autonomía o límites de dominio.

##### Aplicación al caso Pólizas

El ejercicio es una arquitectura de tres capas con API Gateway, servicios de aplicación y
base de datos relacional. Los candidatos a servicios independientes serían Pólizas,
Inventario y Cargos; el reto es la transacción que afecta inventario y genera el cargo. Si
se separan, se necesita Saga y consistencia eventual; si se mantiene la base única, una
transacción local es más simple y segura.

##### Práctica de recuperación activa

1. Dibuja una arquitectura en capas y marca el flujo de una petición.
2. Explica la diferencia entre capas lógicas y tres capas físicas.
3. ¿Qué es el anti-patrón sinkhole?
4. Compara monolito y microservicios en cinco criterios.
5. ¿Dónde vive la lógica de negocio en MVC?

- [ ] Puedo describir capas, tres capas y cliente-servidor.
- [ ] Sé explicar MVC y sus límites.
- [ ] Puedo argumentar monolito vs microservicios con trade-offs.

---

#### Lección 5 — APIs REST y persistencia: idempotencia, relacional vs NoSQL

**Objetivo:** diseñar operaciones REST seguras ante reintentos y elegir el tipo de base de
datos según los requisitos.

**Preguntas del banco:** 13, 14.

##### 5.1 Fundamentos de REST

REST es un estilo arquitectónico para APIs basado en recursos, interfaz uniforme,
statelessness, representaciones (normalmente JSON) y comunicación cliente-servidor.

| Verbo | Uso | Seguro | Idempotente |
|---|---|---|---|
| GET | Leer recurso | Sí | Sí |
| POST | Crear recurso / acción | No | No |
| PUT | Reemplazar recurso | No | Sí |
| PATCH | Modificar parcialmente | No | No necesariamente |
| DELETE | Eliminar recurso | No | Sí |

**Seguro** significa que no modifica el estado. **Idempotente** significa que ejecutar la
misma operación varias veces produce el mismo efecto que ejecutarla una vez.

La idempotencia es esencial en sistemas distribuidos con reintentos: si una respuesta se
pierde y el cliente reintenta, no debe duplicar el efecto. Un POST que crea una póliza no
es idempotente por defecto; se puede hacer "efectivamente idempotente" con una
**Idempotency-Key** y deduplicación en el servidor. PUT y DELETE suelen ser idempotentes.

##### 5.2 Bases de datos relacionales

Organizan datos en tablas con esquema fijo, claves primarias/foráneas, restricciones y
relaciones. Ofrecen transacciones **ACID**:

- **Atomicity:** todo o nada.
- **Consistency:** se respetan las reglas e invariantes.
- **Isolation:** las transacciones concurrentes no interfieren indebidamente.
- **Durability:** lo confirmado sobrevive a fallos.

Fortalezas: integridad, consultas complejas con joins, transacciones, herramientas maduras.
Escalado: vertical, réplicas de lectura, particionado y sharding (con más complejidad).

##### 5.3 Bases de datos NoSQL

Familia de bases con modelos distintos al relacional:

- **Documentales:** documentos JSON/BSON (MongoDB, CouchDB).
- **Clave-valor:** pares clave-valor (Redis, DynamoDB).
- **Columnas anchas:** familias de columnas (Cassandra, HBase).
- **Grafos:** nodos y relaciones (Neo4j).

Suelen ofrecer esquema flexible, escalado horizontal y alta disponibilidad, a cambio de
relajar transacciones fuertes o joins. El modelo se diseña según los **patrones de acceso**,
no según la normalización. "NoSQL" no significa que nunca use SQL; significa "not only SQL".

##### 5.4 Cómo elegir

| Necesidad dominante | Opción razonable |
|---|---|
| Transacciones fuertes, integridad, consultas complejas | Relacional |
| Grandes volúmenes de documentos semiestructurados | Documental |
| Claves simples, caché, sesiones, altísima velocidad | Clave-valor |
| Series temporales o escritura masiva por columnas | Columnas anchas |
| Relaciones profundas y consultas de red | Grafos |
| Búsqueda de texto completo | Motor de búsqueda dedicado |

La **persistencia políglota** usa varios tipos de almacenamiento en el mismo sistema, cada
uno para lo que mejor hace. No añadas una base de datos sin una razón clara: cada una
aumenta la complejidad operativa y la consistencia entre almacenes.

##### En la entrevista

- Explica idempotencia con PUT/DELETE y el problema de POST con reintentos.
- Menciona Idempotency-Key para POST.
- Compara relacional y NoSQL por consistencia, esquema, consultas, escalado y patrones de
  acceso; evita afirmaciones absolutas.
- Pregunta por el patrón de acceso antes de recomendar una base.

##### Aplicación al caso Pólizas

Pólizas encaja en una base relacional: encabezado, detalle, movimiento de inventario y cargo
deben confirmarse atómicamente. `sp_AplicarMovimientoPoliza` encapsula la transacción. El
endpoint `POST /polizas` debería aceptar una Idempotency-Key para evitar duplicados si el
cliente reintenta tras un timeout. Si en el futuro se separan servicios, la transacción
local se reemplaza por una Saga.

##### Práctica de recuperación activa

1. Clasifica GET, POST, PUT, PATCH y DELETE como seguros/idempotentes.
2. Explica cómo evitar duplicados en un POST reintentado.
3. Da un caso donde NoSQL es mejor que relacional y otro al revés.
4. Define ACID con un ejemplo de transferencia.

- [ ] Puedo explicar idempotencia y su relación con reintentos.
- [ ] Sé comparar relacional y NoSQL sin dogmatismo.
- [ ] Puedo elegir persistencia según el patrón de acceso.

---

#### Lección 6 — Escalabilidad, balanceo de carga y caché

**Objetivo:** escalar un sistema, distribuir tráfico y usar caché sin sacrificar
consistencia de forma inadvertida.

**Preguntas del banco:** 16, 32, 33.

##### 6.1 Escalabilidad vertical vs horizontal

| Criterio | Vertical (scale up) | Horizontal (scale out) |
|---|---|---|
| Estrategia | Más CPU, RAM o disco en una máquina | Más instancias o nodos |
| Facilidad | Alta; a menudo sin cambios de código | Requiere statelessness, balanceo y coordinación |
| Límite | Físico y económico | Práctico; depende del diseño |
| Disponibilidad | No mejora por sí sola; sigue habiendo un nodo | Mejora si hay redundancia |
| Complejidad | Baja | Mayor: estado compartido, consistencia, red |
| Ejemplo | Servidor de base de datos más grande | Varias réplicas de un servicio web |

Para escalar horizontalmente, los servicios deben ser **stateless**: el estado de sesión se
externaliza (Redis, base de datos, token firmado). Las sesiones pegajosas (sticky sessions)
pueden ser un parche, pero reducen la flexibilidad y complican el failover.

##### 6.2 Balanceo de carga

Un balanceador distribuye solicitudes entre réplicas. Puede operar en capa 4 (TCP) o capa 7
(HTTP), con health checks y distintas políticas:

- **Round Robin:** asigna cada solicitud al siguiente servidor en una lista circular. Simple;
  funciona bien con servidores homogéneos y solicitudes de coste similar.
- **Least Connections:** envía al servidor con menos conexiones activas. Mejor cuando las
  solicitudes varían en duración o coste.
- **Weighted:** asigna pesos según capacidad.
- **IP Hash:** mantiene afinidad por cliente; útil para sesiones, pero puede desbalancear.
- **Least Response Time:** considera latencia además de carga.

Otros conceptos: health checks, connection draining, timeouts, reintentos controlados y
evitar "retry storms".

##### 6.3 Estrategias de caché

La caché reduce latencia y carga, pero introduce el problema de la **consistencia** y la
**invalidación**.

| Estrategia | Funcionamiento | Ventaja | Riesgo |
|---|---|---|---|
| Cache-aside (lazy) | La app consulta caché; si falla, lee la BD y llena la caché | Simple; solo cachea lo usado | Datos obsoletos; primer acceso lento |
| Write-through | Cada escritura actualiza caché y BD de forma síncrona | Caché siempre actualizada | Mayor latencia de escritura |
| Write-behind | Escribe en caché y luego en BD de forma asíncrona | Escrituras rápidas | Pérdida de datos si falla la caché |
| Refresh-ahead | Refresca entradas antes de que expiren | Evita misses predecibles | Complejidad y carga proactiva |

Conceptos complementarios: TTL, invalidación por evento, claves versionadas, cache stampede
o thundering herd, negative caching y caché en CDN.

##### En la entrevista

- Pregunta por el ratio lectura/escritura y la tolerancia a datos obsoletos.
- Explica Round Robin vs Least Connections con un ejemplo de carga variable.
- Para caché, menciona invalidación y fallos, no solo "es más rápido".
- Recuerda que la caché no es una fuente de verdad.

##### Aplicación al caso Pólizas

El ejercicio incluye Redis para catálogos (artículos, empleados, centros), que cambian poco
y se leen mucho: buen caso de cache-aside con TTL. No conviene cachear el stock o los cargos
sin una estrategia de invalidación, porque son datos transaccionales. El balanceador
reparte tráfico entre servidores web; si los servicios son stateless, no se necesitan
sticky sessions.

##### Práctica de recuperación activa

1. Explica cuándo escalar verticalmente y cuándo horizontalmente.
2. Compara Round Robin y Least Connections.
3. Describe cache-aside y write-through con un ejemplo.
4. ¿Qué es un cache stampede y cómo lo mitigarías?

- [ ] Sé diferenciar escalado vertical y horizontal.
- [ ] Puedo elegir un algoritmo de balanceo según la carga.
- [ ] Puedo diseñar una caché con invalidación y TTL.

---

### Módulo II — Arquitecturas modernas, datos y resiliencia

#### Lección 7 — Comunicación, mensajería y arquitectura orientada a eventos

**Objetivo:** elegir entre comunicación síncrona y asíncrona, y entre colas y pub/sub.

**Preguntas del banco:** 21, 31, 34.

##### 7.1 Comunicación síncrona vs asíncrona

| Criterio | Síncrona | Asíncrona |
|---|---|---|
| Ejemplo | HTTP/REST, gRPC | Colas, brokers de eventos |
| Comportamiento | El emisor espera respuesta | El emisor publica y continúa |
| Acoplamiento temporal | Alto | Bajo |
| Fallos | Se propagan si no hay timeout/circuit breaker | Se amortiguan con buffer y reintentos |
| Complejidad | Baja | Mayor: orden, idempotencia, consistencia |
| Uso típico | Consultas de usuario, operaciones que necesitan respuesta inmediata | Efectos secundarios, notificaciones, procesos largos |

La comunicación síncrona es simple y fácil de razonar, pero un servicio lento puede agotar
hilos y conexiones del llamador. La asíncrona desacopla y mejora la resiliencia, a cambio de
consistencia eventual y más complejidad operativa.

##### 7.2 Event-Driven Architecture (EDA)

Los componentes producen y consumen **eventos**: hechos ocurridos en el sistema, por ejemplo
`PolizaCreada`, `InventarioAfectado` o `CargoRegistrado`. El productor no conoce a los
consumidores; un broker (Kafka, RabbitMQ, SNS/SQS) entrega los eventos.

- **Ventajas:** desacoplamiento, escalabilidad, resiliencia, extensibilidad (nuevos
  consumidores sin tocar al productor).
- **Desventajas:** trazabilidad más difícil, consistencia eventual, orden de eventos,
  duplicados, evolución de esquemas y depuración distribuida.

Topologías habituales: notificación de eventos, transferencia de estado en el evento y
Event Sourcing (L9). En la práctica se combina con coreografía u orquestación (L10).

##### 7.3 Cola de mensajes vs pub/sub

| Criterio | Cola (point-to-point) | Pub/sub |
|---|---|---|
| Consumidores | Un mensaje lo consume un consumidor | Todos los suscriptores reciben una copia |
| Objetivo | Repartir trabajo | Difundir eventos |
| Ejemplo | Workers que procesan pólizas | Notificar a auditoría, facturación y analítica |
| Escalado | Varios workers compiten por mensajes | Cada suscriptor tiene su propio consumo |

Kafka combina ambos según los **consumer groups**: dentro de un grupo, cada mensaje va a un
consumidor (cola); varios grupos reciben el mismo evento (pub/sub).

##### 7.4 Semánticas de entrega

- **At-most-once:** puede perderse; no se reintenta.
- **At-least-once:** no se pierde, pero puede duplicarse; requiere consumidores idempotentes.
- **Exactly-once:** deseable, pero costoso; suele lograrse como "efectivamente una vez" con
  idempotencia y transacciones.

Diseña consumidores idempotentes, usa DLQ (dead-letter queue), reintentos con backoff y
claves de deduplicación. La semántica de entrega es una decisión arquitectónica, no un
detalle.

##### En la entrevista

- Explica el acoplamiento temporal de lo síncrono y cómo lo asíncrono lo reduce.
- Diferencia cola de pub/sub con un ejemplo de trabajo vs notificación.
- Menciona el precio del asíncrono: consistencia eventual, orden, duplicados y debugging.

##### Aplicación al caso Pólizas

La creación de una póliza necesita una respuesta inmediata (folio), así que el núcleo puede
ser síncrono. La auditoría, las notificaciones y la analítica son candidatas a eventos
asíncronos. Si se separan servicios, `PolizaCreada` puede disparar el cargo y la auditoría
sin que `PolizaService` conozca a todos los consumidores.

##### Práctica de recuperación activa

1. Da un caso donde lo síncrono es mejor y otro donde lo asíncrono es mejor.
2. Explica la diferencia entre cola y pub/sub.
3. ¿Qué implica at-least-once para el consumidor?
4. Dibuja un flujo de eventos para Pólizas.

- [ ] Sé comparar síncrono y asíncrono.
- [ ] Puedo explicar EDA y sus trade-offs.
- [ ] Distingo cola de pub/sub y conozco las semánticas de entrega.

---

#### Lección 8 — Arquitectura hexagonal y Domain-Driven Design

**Objetivo:** aislar el dominio de la infraestructura y modelar límites y agregados.

**Preguntas del banco:** 22, 25, 26.

##### 8.1 Arquitectura hexagonal (Ports & Adapters)

Coloca la lógica de negocio en el centro y la aísla de los detalles externos mediante:

- **Puertos:** interfaces que definen cómo el dominio interactúa con el exterior.
- **Adaptadores:** implementaciones concretas de esos puertos.

Hay adaptadores **primarios o de entrada** (REST, UI, CLI, consumidores de mensajes) y
**secundarios o de salida** (base de datos, broker, APIs externas). El dominio no depende de
la infraestructura; la infraestructura depende del dominio (inversión de dependencias).

Beneficios: testabilidad del núcleo sin base de datos, reemplazo de infraestructura,
decisión tardía de tecnología y límites claros. No significa "seis módulos" ni una
estructura de carpetas rígida; es una forma de pensar dependencias. Comparte objetivo con
Clean Architecture y Onion Architecture.

##### 8.2 DDD estratégico

- **Lenguaje ubicuo:** vocabulario compartido por negocio y desarrollo dentro de un contexto.
- **Bounded Context:** límite dentro del cual un modelo de dominio es válido y consistente.
  Un mismo término ("Cliente", "Póliza") puede significar cosas distintas en contextos
  distintos.
- **Context Map:** mapa de relaciones entre contextos: partnership, shared kernel,
  customer-supplier, conformist, anti-corruption layer (ACL), separate ways.

Un Bounded Context no es sinónimo de microservicio, pero suele alinearse con él porque
delimita un modelo y un equipo.

##### 8.3 DDD táctico

| Concepto | Definición |
|---|---|
| Entidad | Objeto con identidad propia que persiste en el tiempo |
| Value Object | Objeto inmutable sin identidad; se compara por valor |
| Aggregate | Clúster de entidades y value objects con una frontera de consistencia |
| Aggregate Root | Único punto de entrada al agregado; garantiza invariantes |
| Repository | Abstracción para persistir/recuperar agregados |
| Domain Service | Lógica de dominio que no encaja en una entidad |
| Domain Event | Hecho relevante del dominio |

Reglas de diseño de agregados: mantenerlos pequeños, una transacción por agregado,
referenciar otros agregados por ID y usar consistencia eventual entre agregados. Un agregado
demasiado grande genera contención y transacciones lentas; uno demasiado pequeño no protege
invariantes.

##### En la entrevista

- Explica hexagonal como aislamiento del dominio, no como "hexágono mágico".
- Diferencia Bounded Context de microservicio.
- Explica Aggregate con un ejemplo de invariante (total del pedido/póliza).
- Menciona que DDD es más útil en dominios complejos; no lo apliques a CRUD simple.

##### Aplicación al caso Pólizas

`Poliza` con `PolizaDetalle` es un agregado natural: el total y las reglas del tipo de
póliza se protegen a través de la raíz. `Inventario` puede ser otro agregado; `CargoEmpleado`
podría pertenecer a otro contexto (nómina/cobranza). La integración con el sistema legado de
empleados se puede aislar con una **ACL**.

##### Práctica de recuperación activa

1. Dibuja puertos y adaptadores para Pólizas.
2. Da un ejemplo de término con significado distinto en dos contextos.
3. Explica qué invariante protege el Aggregate Root de una póliza.
4. ¿Cuándo no usarías DDD?

- [ ] Puedo explicar puertos y adaptadores.
- [ ] Sé definir Bounded Context y dar un ejemplo.
- [ ] Puedo modelar un Aggregate y justificar sus límites.

---

#### Lección 9 — CQRS y Event Sourcing

**Objetivo:** separar lecturas de escrituras y persistir el historial de eventos cuando el
dominio lo justifique.

**Preguntas del banco:** 23, 24.

##### 9.1 CQRS

CQRS (Command Query Responsibility Segregation) separa los modelos de escritura (comandos)
de los de lectura (consultas):

- **Comando:** modifica estado; valida invariantes; no devuelve datos de negocio (o solo un
  identificador).
- **Consulta:** solo lee; puede usar un modelo desnormalizado optimizado para la vista.

Se pueden separar modelos lógicos, almacenes o servicios. Ventajas: optimización
independiente, escalado separado, modelos de lectura adaptados a la UI. Costes: consistencia
eventual entre escritura y lectura, duplicación, complejidad operativa.

No es para todo el sistema: un CRUD simple no necesita CQRS. Es útil cuando hay asimetría
fuerte entre lecturas y escrituras, consultas complejas o requisitos de escalado distintos.

##### 9.2 Event Sourcing

En lugar de guardar solo el estado actual, se guarda la **secuencia de eventos** que lo
produjeron. El estado se reconstruye reproduciendo los eventos; se pueden usar snapshots
para no reproducir desde el inicio.

- **Ventajas:** auditoría completa, consultas temporales, depuración, reconstrucción de
  vistas, capacidad de replicar el historial.
- **Retos:** versionado de eventos, tamaño del log, snapshots, concurrencia optimista,
  idempotencia, evolución de esquemas, privacidad/derecho al olvido y consistencia eventual
  con las proyecciones.

Event Sourcing se combina a menudo con CQRS: el lado de escritura guarda eventos y el lado
de lectura construye proyecciones. No es un requisito: se puede usar CQRS sin Event Sourcing
y Event Sourcing sin CQRS.

##### En la entrevista

- Explica CQRS como separación de responsabilidades, no como "dos bases de datos siempre".
- Menciona la consistencia eventual y cómo la maneja la UI.
- Explica Event Sourcing con un ejemplo de cuenta o póliza y menciona snapshots.
- Reconoce cuándo **no** usarlos: dominios simples, equipos sin experiencia, requisitos
  transaccionales sencillos.

##### Aplicación al caso Pólizas

El historial de una póliza (creada, actualizada, eliminada, movimiento aplicado, cargo
registrado) es un candidato natural a Event Sourcing si la auditoría es un requisito fuerte.
El listado de pólizas puede ser una proyección de lectura (CQRS). La creación sigue
necesitando validar reglas e invariantes en el lado de escritura.

##### Práctica de recuperación activa

1. Diferencia comando de consulta.
2. Explica CQRS con y sin bases separadas.
3. Describe cómo reconstruir el estado de una póliza desde eventos.
4. ¿Qué problema resuelven los snapshots?

- [ ] Puedo explicar CQRS y sus costes.
- [ ] Sé definir Event Sourcing y sus retos.
- [ ] Puedo decidir cuándo no aplicarlos.

---

#### Lección 10 — Resiliencia: Circuit Breaker, Saga y Bulkhead

**Objetivo:** evitar fallos en cascada, mantener consistencia entre servicios y aislar
recursos.

**Preguntas del banco:** 27, 28, 55.

##### 10.1 Circuit Breaker

Protege al llamador de un servicio que falla. Tiene tres estados:

- **Cerrado:** las llamadas pasan normalmente; se cuentan fallos.
- **Abierto:** se deja de llamar durante un periodo; se responde rápido con error o fallback.
- **Semi-abierto:** se permiten llamadas de prueba; si funcionan, se cierra; si no, se
  vuelve a abrir.

Se configura por dependencia, con umbrales de fallo/lentitud y tiempo de enfriamiento. Evita
agotar hilos y conexiones esperando timeouts, y previene fallos en cascada. Se combina con
timeouts, reintentos con backoff y fallbacks.

##### 10.2 Saga

Una Saga gestiona una transacción de negocio que abarca varios servicios, cada uno con su
propia base de datos. Se compone de transacciones locales y **acciones compensatorias** para
deshacer los pasos si algo falla.

- **Coreografía:** cada servicio reacciona a eventos; no hay coordinador central. Simple al
  principio, difícil de seguir cuando crece.
- **Orquestación:** un coordinador dirige la secuencia y decide compensaciones. Más explícito,
  pero añade un componente que debe diseñarse bien.

No hay aislamiento global ni atomicidad estricta: hay consistencia eventual. Las
compensaciones deben ser idempotentes y diseñadas como lógica de negocio. Ejemplo: crear
póliza, reservar inventario, registrar cargo; si el cargo falla, revertir inventario y
cancelar la póliza.

##### 10.3 Bulkhead

Inspirado en los compartimentos estancos de un barco: aísla recursos (hilos, conexiones,
instancias, colas) por dependencia o funcionalidad. Si un servicio lento consume todos los
hilos de un pool compartido, puede tumbar las llamadas a otros servicios; con pools
separados, el daño queda contenido.

Coste: menor utilización de recursos y necesidad de dimensionar cada compartimento. Se
complementa con rate limiting y load shedding.

##### 10.4 Patrones complementarios

- **Timeout:** no esperar indefinidamente.
- **Retry con backoff exponencial y jitter:** reintentar sin sincronizar reintentos.
- **Fallback:** respuesta degradada o cacheada.
- **Rate limiting:** proteger al servicio y a sus dependencias.
- **Health checks:** detectar y sacar de rotación instancias enfermas.

##### En la entrevista

- Dibuja los estados del Circuit Breaker.
- Explica Saga con un ejemplo y diferencia coreografía vs orquestación.
- Explica Bulkhead como aislamiento de recursos, no como "otro circuit breaker".
- Menciona que estos patrones se combinan; ninguno basta por sí solo.

##### Aplicación al caso Pólizas

Circuit Breaker alrededor de `EmployeeService` y del servicio de inventario; Bulkhead para
separar las llamadas a cargos de las consultas de catálogo; Saga si la creación de póliza
atraviesa servicios con bases separadas. Si la transacción sigue en una sola base, una
transacción local es preferible.

##### Práctica de recuperación activa

1. Explica los tres estados del Circuit Breaker.
2. Diseña una Saga para crear una póliza y cancelarla si falla el cargo.
3. ¿Qué recurso aislarías con Bulkhead y por qué?
4. ¿Por qué los reintentos necesitan backoff y jitter?

- [ ] Puedo explicar Circuit Breaker y sus estados.
- [ ] Sé cuándo usar Saga y cómo compensar.
- [ ] Entiendo Bulkhead y su coste.

---

#### Lección 11 — Plataforma: API Gateway, Service Mesh, contenedores, Kubernetes y serverless

**Objetivo:** conocer los componentes de infraestructura de una arquitectura moderna y sus
trade-offs.

**Preguntas del banco:** 29, 30, 38, 39, 40, 43, 49.

##### 11.1 API Gateway

Punto de entrada único para clientes externos. Enruta solicitudes, centraliza autenticación
y autorización, rate limiting, agregación de respuestas, traducción de protocolos y
observabilidad. Puede implementar el patrón BFF (Backend for Frontend).

Ventajas: evita duplicar preocupaciones transversales en cada servicio y oculta la topología
interna. Riesgos: cuello de botella y SPOF si no se replica; no debe contener lógica de
negocio. En arquitecturas grandes puede haber varios gateways por dominio o canal.

##### 11.2 Service Mesh

Capa de infraestructura para la comunicación servicio a servicio. Despliega un proxy
**sidecar** junto a cada instancia (por ejemplo, Envoy) y separa el **data plane** (proxies)
del **control plane** (configuración y políticas).

Funciones: mTLS, descubrimiento, balanceo, retries, timeouts, circuit breaking, traffic
shifting, telemetría y políticas de acceso. Ventaja: seguridad y observabilidad
consistentes sin tocar el código. Coste: complejidad operativa, latencia adicional y curva
de aprendizaje. Suele justificarse con muchos servicios y equipos.

##### 11.3 Patrón Sidecar

Proceso o contenedor auxiliar que acompaña al servicio principal en el mismo host o Pod.
Comparte red y ciclo de vida y provee capacidades transversales: proxy, logging, métricas,
TLS, sincronización de configuración. No debe contener lógica de negocio. Es la base de los
service meshes.

##### 11.4 Contenedores vs máquinas virtuales

| Criterio | Contenedor | Máquina virtual |
|---|---|---|
| Virtualización | A nivel de SO; comparte kernel | Hardware completo con hipervisor |
| Peso | Ligero | Pesado |
| Arranque | Segundos o menos | Minutos |
| Densidad | Alta | Menor |
| Aislamiento | Procesos, namespaces, cgroups | Más fuerte; kernel separado |
| SO invitado | No; usa el del host | Sí, completo |
| Uso típico | Microservicios, CI/CD, despliegue denso | Aislamiento fuerte, multi-OS, cargas tradicionales |

Los contenedores no son "VMs pequeñas": comparten kernel y por eso son ligeros, pero también
por eso el aislamiento y la compatibilidad dependen del host.

##### 11.5 Kubernetes

- **Pod:** unidad mínima de despliegue; uno o más contenedores que comparten red y
  almacenamiento; efímero.
- **Deployment:** garantiza réplicas, actualizaciones rolling y self-healing.
- **Service:** acceso estable a un conjunto de Pods.
- **Ingress:** enrutamiento HTTP externo.
- **ConfigMap/Secret:** configuración y secretos.
- **HPA:** escalado automático por métricas.

No se gestionan Pods directamente en producción; se usan controladores de nivel superior.

##### 11.6 Serverless / FaaS

El proveedor gestiona servidores, aprovisionamiento y escalado; el código se ejecuta por
eventos y se cobra por uso. Escala a cero cuando no hay tráfico.

**Cold start:** latencia adicional cuando no hay una instancia caliente y el proveedor debe
inicializar runtime y código. Se mitiga con warm-up, paquetes pequeños, runtimes rápidos y
concurrencia aprovisionada. Limitaciones: tiempo máximo de ejecución, memoria, estado local,
límites del proveedor y vendor lock-in. Ideal para cargas esporádicas, eventos y picos
variables; menos adecuado para procesos largos o latencia ultraestable.

##### En la entrevista

- Diferencia API Gateway de Service Mesh: entrada externa vs comunicación interna.
- Explica Sidecar como patrón base del mesh.
- Compara contenedores y VMs por aislamiento, peso y densidad.
- Define Pod y no confundirlo con nodo.
- Explica cold start y cuándo serverless no es buena opción.

##### Aplicación al caso Pólizas

El API Gateway enruta `/polizas`, `/inventory` y `/charges`; los servicios pueden correr en
contenedores sobre Kubernetes; un sidecar puede encargarse de logging o mTLS; una función
serverless puede procesar notificaciones o reportes esporádicos. La creación de póliza, por
ser transaccional y sensible a latencia, probablemente no sea el mejor candidato a FaaS.

##### Práctica de recuperación activa

1. Enumera cinco responsabilidades de un API Gateway.
2. Explica qué aporta un service mesh y qué cuesta.
3. Compara contenedores y VMs en cuatro criterios.
4. Define Pod, Deployment y Service.
5. Explica cold start y dos mitigaciones.

- [ ] Puedo diferenciar Gateway, Mesh y Sidecar.
- [ ] Sé comparar contenedores y VMs.
- [ ] Entiendo Pod, Kubernetes y serverless con sus límites.

---

#### Lección 12 — Sistemas distribuidos: CAP, consistencia, hashing, CRDTs y Kafka

**Objetivo:** razonar sobre consistencia, particiones y distribución de datos.

**Preguntas del banco:** 35, 36, 41, 42, 46, 50.

##### 12.1 Teorema CAP

En un sistema distribuido no se pueden garantizar simultáneamente:

- **Consistencia (C):** todos los nodos ven los mismos datos (linealizabilidad).
- **Disponibilidad (A):** toda solicitud recibe una respuesta, aunque no sea la más reciente.
- **Tolerancia a particiones (P):** el sistema sigue funcionando si se pierden mensajes
  entre nodos.

Como las particiones de red son inevitables, durante una partición hay que elegir:

- **CP:** sacrificar disponibilidad para preservar consistencia; se rechazan o bloquean
  solicitudes que no pueden garantizarla.
- **AP:** sacrificar consistencia inmediata para seguir disponible; se aceptan lecturas
  posiblemente obsoletas y se converge después.

CAP no significa "elige dos para siempre"; se aplica cuando ocurre una partición. **PACELC**
extiende la idea: si hay partición, eliges A o C; si no la hay, eliges latencia (L) o
consistencia (C).

##### 12.2 Consistencia eventual

Bajo consistencia eventual, tras una escritura las réplicas pueden divergir temporalmente,
pero si no hay nuevas actualizaciones, convergen al mismo estado. Es común en sistemas AP y
en modelos BASE (Basically Available, Soft state, Eventually consistent).

Ejemplos aceptables: contadores de "me gusta", recomendaciones, feeds. Ejemplos donde no es
aceptable: saldos bancarios, stock crítico, cargos de dinero, a menos que el negocio lo
tolere con reglas claras. Los conflictos se resuelven con last-write-wins, versiones,
vectores o CRDTs.

##### 12.3 Consistent hashing

Con hashing por módulo (`hash(clave) % N`), añadir o quitar un nodo cambia la mayoría de las
asignaciones y obliga a mover muchos datos. El **consistent hashing** mapea nodos y claves a
un anillo; cada clave se asigna al primer nodo en sentido horario. Al añadir o quitar un
nodo, solo se mueven las claves adyacentes.

Los **nodos virtuales** mejoran el balance. Se usa en cachés distribuidas, Cassandra,
DynamoDB y sistemas de particionado. Considera replicación, hotspots y rebalanceo.

##### 12.4 CRDTs

Los Conflict-free Replicated Data Types son estructuras diseñadas para que réplicas
independientes se actualicen sin coordinación y se fusionen de forma determinista,
convergiendo al mismo estado. El merge debe ser conmutativo, asociativo e idempotente.

Ejemplos: G-Counter (solo incrementos), PN-Counter (incrementos/decrementos), OR-Set
(conjunto observado-remove), LWW-Register (última escritura gana). Se usan en edición
colaborativa, offline-first y sistemas multi-región AP. Limitaciones: metadata, semántica
limitada y complejidad; no sirven para cualquier regla de negocio.

##### 12.5 Apache Kafka

- **Topic:** categoría de eventos.
- **Partition:** unidad de paralelismo y orden.
- **Offset:** posición de un consumidor en la partición.
- **Consumer group:** consumidores que reparten particiones.
- **Replicación:** copias de cada partición para tolerancia a fallos.

Kafka garantiza orden **dentro de una partición**, no en todo el topic. Los mensajes con la
misma clave van a la misma partición (hash de la clave), lo que permite ordenar por entidad
(por ejemplo, todos los eventos de una póliza). Diseñar la clave y el número de particiones
es una decisión arquitectónica.

##### En la entrevista

- Explica CAP con la partición como condición, no como "elige dos".
- Diferencia CP y AP con ejemplos de negocio.
- Explica consistencia eventual y cuándo no usarla.
- Describe consistent hashing y el problema que resuelve.
- Explica CRDTs sin exagerar: convergencia sin coordinación, con límites.
- Para Kafka, destaca orden por partición y elección de clave.

##### Aplicación al caso Pólizas

El stock y los cargos son datos sensibles: conviene CP o consistencia fuerte en la escritura.
Los reportes y catálogos pueden ser AP/eventuales. Si se publican eventos de póliza en Kafka,
usa `id_poliza` como clave para preservar el orden por póliza. Los CRDTs no son adecuados
para saldos, pero sí para contadores o listas colaborativas.

##### Práctica de recuperación activa

1. Define C, A y P y explica por qué P es inevitable.
2. Da un ejemplo CP y otro AP.
3. Explica consistent hashing con un anillo de cuatro nodos.
4. ¿Qué garantiza Kafka y qué no?
5. ¿Cuándo usarías un CRDT y cuándo no?

- [ ] Puedo explicar CAP y PACELC.
- [ ] Entiendo consistencia eventual y sus riesgos.
- [ ] Sé explicar consistent hashing, CRDTs y orden en Kafka.

---

#### Lección 13 — Transacciones distribuidas y streaming: 2PC, Saga, backpressure, Lambda y Kappa

**Objetivo:** comparar mecanismos de consistencia distribuida y arquitecturas de
procesamiento de datos.

**Preguntas del banco:** 44, 45, 56.

##### 13.1 Two-phase commit (2PC)

Protocolo con un coordinador y participantes:

1. **Prepare:** cada participante confirma que puede comprometerse y bloquea recursos.
2. **Commit/abort:** si todos están listos, el coordinador ordena commit; si alguno falla,
   abort.

Garantiza atomicidad fuerte, pero bloquea recursos durante el proceso, depende del
coordinador y reduce disponibilidad. No escala bien para transacciones largas o muchos
participantes. Se usa en escenarios acotados donde la consistencia fuerte es imprescindible.

##### 13.2 2PC vs Saga

| Criterio | 2PC | Saga |
|---|---|---|
| Atomicidad | Fuerte | Eventual; compensaciones |
| Bloqueo | Recursos bloqueados | Sin bloqueo global |
| Disponibilidad | Menor | Mayor |
| Escalabilidad | Limitada | Mejor |
| Complejidad | Protocolo coordinado | Lógica de compensación y estados |
| Uso típico | Transacciones cortas, pocos participantes | Microservicios, procesos largos |

Una Saga no "deshace" físicamente; aplica acciones compensatorias. Requiere idempotencia,
estados intermedios y tolerancia a fallos durante la compensación.

##### 13.3 Backpressure

Mecanismo de control de flujo: un consumidor más lento comunica al productor que reduzca la
tasa, o el sistema aplica buffering acotado, bloqueo, descarte o throttling. Sin
backpressure, una cola ilimitada puede agotar memoria y colapsar.

Se implementa en Reactive Streams, RxJava, Akka Streams y sistemas de streaming. Monitorea
lag, profundidad de cola y latencia; el backpressure debe propagarse por toda la cadena.

##### 13.4 Lambda vs Kappa

| Criterio | Lambda | Kappa |
|---|---|---|
| Rutas | Batch + speed + serving | Solo streaming |
| Datos históricos | Capa batch | Reprocesando el log |
| Latencia | Mixta | Baja y uniforme |
| Complejidad | Dos sistemas y lógica duplicada | Un solo sistema; requiere motor y retención |
| Reprocesamiento | Batch dedicado | Replay del log |
| Uso típico | Analítica con históricos y tiempo real | Streaming continuo con reprocesamiento |

Lambda es robusta pero costosa de mantener; Kappa simplifica si el motor de streaming puede
reprocesar grandes volúmenes y el log se conserva lo suficiente.

##### En la entrevista

- Explica 2PC y su problema de bloqueo/coordinador.
- Compara 2PC y Saga por atomicidad, disponibilidad y complejidad.
- Define backpressure como control de flujo, no como "más buffer".
- Diferencia Lambda y Kappa por rutas y reprocesamiento.

##### Aplicación al caso Pólizas

Si la creación de póliza se mantiene en una base relacional, una transacción local evita 2PC
y Saga. Si se separan inventario y cargos, usa Saga con compensaciones. Para analítica de
pólizas, un pipeline streaming con retención y replay puede simplificar frente a Lambda.

##### Práctica de recuperación activa

1. Describe las dos fases de 2PC y su principal debilidad.
2. Compara 2PC y Saga en cuatro criterios.
3. Explica qué ocurre sin backpressure en una cola.
4. ¿Cuándo elegirías Kappa sobre Lambda?

- [ ] Puedo explicar 2PC y Saga con sus trade-offs.
- [ ] Entiendo backpressure y sus estrategias.
- [ ] Sé comparar Lambda y Kappa.

---

### Módulo III — Entrega, operación y organización

#### Lección 14 — Modernización, despliegues, operación y arquitectura evolutiva

**Objetivo:** migrar sistemas legacy, desplegar con bajo riesgo, operar con observabilidad y
proteger la arquitectura con automatización.

**Preguntas del banco:** 37, 47, 48, 54, 57, 59, 60.

##### 14.1 Strangler Fig

Patrón para modernizar un sistema legado de forma incremental. Se coloca una fachada o proxy
delante del legado y se enruta el tráfico gradualmente hacia nuevos servicios, a medida que
se implementan funcionalidades equivalentes. Al final, el legado se retira.

Ventajas: reduce el riesgo de una reescritura "big bang", permite validar por partes y
revertir. Requisitos: estrategia de enrutamiento, paridad funcional, migración de datos y
criterios de retirada. Se complementa con branch by abstraction y feature flags.

##### 14.2 Blue-green, canary y feature flags

| Estrategia | Funcionamiento | Ventaja | Coste/riesgo |
|---|---|---|---|
| Blue-green | Dos entornos completos; se cambia todo el tráfico de golpe | Rollback instantáneo | Doble infraestructura |
| Canary | Se libera a un porcentaje pequeño y se amplía según métricas | Detecta problemas con impacto limitado | Enrutamiento y observabilidad |
| Feature flags | Activan/desactivan funcionalidades en runtime | Despliegue separado de liberación; rollback inmediato | Deuda de flags y complejidad |

Las **feature flags** permiten desplegar código sin liberarlo, hacer A/B testing, activar por
segmento y desactivar una función problemática sin revertir el despliegue. Requieren
disciplina para eliminar flags obsoletos.

##### 14.3 Chaos Engineering

Consiste en inyectar fallos **controlados** (latencia, caída de instancias, saturación de
CPU, errores de red) con una hipótesis sobre el comportamiento esperado, para verificar que
la resiliencia funciona en condiciones adversas. Se empieza en entornos de prueba y se
avanza a producción con un **blast radius** limitado.

No es sabotaje aleatorio: es experimentación con hipótesis, métricas y reversión. Complementa
las pruebas tradicionales y descubre "unknown unknowns".

##### 14.4 Observabilidad

Tres pilares:

- **Logs:** eventos discretos y detallados; útiles para depuración.
- **Métricas:** valores agregados en el tiempo; útiles para tendencias y alertas.
- **Trazas distribuidas:** recorrido de una solicitud por varios servicios.

Se complementan con SLI (indicador), SLO (objetivo) y SLA (acuerdo). Alerta sobre síntomas
que afectan al usuario, no sobre cada métrica. Controla la cardinalidad de etiquetas.

##### 14.5 Distributed tracing

Asigna un **trace ID** a una solicitud y propaga el contexto entre servicios. Cada unidad de
trabajo es un **span** con duración y metadatos. Permite ver dónde se va el tiempo y dónde
falla una solicitud en un sistema con muchos servicios. OpenTelemetry estandariza la
instrumentación de trazas, métricas y logs. Considera muestreo para controlar coste.

##### 14.6 Fitness functions

En arquitectura evolutiva, una fitness function es una prueba automatizada y objetiva que
verifica si la arquitectura mantiene un atributo de calidad o una restricción. Ejemplos:
prohibir dependencias del dominio hacia infraestructura, validar latencia de una API,
detectar ciclos entre módulos, verificar compatibilidad de contratos o escanear seguridad.

Se ejecutan en CI/CD y actúan como guardrails: la arquitectura evoluciona sin degradarse
silenciosamente. No sustituyen las revisiones humanas; las hacen más baratas y continuas.

##### En la entrevista

- Explica Strangler Fig como migración incremental, no big bang.
- Compara blue-green y canary por tráfico, rollback y coste.
- Diferencia desplegar de liberar con feature flags.
- Define chaos engineering con hipótesis y blast radius.
- Enumera los tres pilares de observabilidad y el valor del tracing.
- Explica una fitness function con un ejemplo concreto.

##### Aplicación al caso Pólizas

Usa Strangler Fig para migrar el módulo legacy de inventario; canary y feature flags para el
nuevo módulo de pólizas; SLOs para la creación de pólizas; tracing desde el gateway hasta la
base de datos; una fitness function que impida que el dominio de pólizas dependa del cliente
legacy.

##### Práctica de recuperación activa

1. Diseña una migración Strangler para un módulo legado.
2. Compara blue-green y canary en tres criterios.
3. Explica qué medirías en un experimento de caos.
4. Define SLI, SLO y SLA.
5. Propón dos fitness functions para Pólizas.

- [ ] Puedo explicar Strangler Fig y sus requisitos.
- [ ] Sé comparar blue-green, canary y feature flags.
- [ ] Entiendo observabilidad, tracing y fitness functions.

---

#### Lección 15 — Seguridad, multi-tenancy, datos y arquitectura empresarial

**Objetivo:** aplicar Zero Trust, diseñar multi-tenancy, entender Data Mesh y ubicar TOGAF
ADM.

**Preguntas del banco:** 51, 52, 53, 58.

##### 15.1 Zero Trust

El modelo perimetral tradicional asume que todo lo que está dentro de la red es confiable.
Zero Trust invierte la premisa: **ninguna solicitud es confiable por defecto**, sin importar
si viene de dentro o de fuera.

Principios:

- **Verificar explícitamente:** identidad, dispositivo, contexto y permisos en cada acceso.
- **Mínimo privilegio:** solo los permisos necesarios, por el tiempo necesario.
- **Asumir compromiso:** diseñar para detectar y limitar el daño, no solo para prevenirlo.

Mecanismos: autenticación fuerte/MFA, autorización por solicitud, microsegmentación, mTLS
entre servicios, políticas centralizadas, monitoreo continuo y rotación de credenciales. Es
una estrategia, no un producto. Añade latencia y complejidad, así que se aplica con riesgo
proporcional.

##### 15.2 Multi-tenancy

Una arquitectura multi-tenant permite que varios clientes (tenants) compartan la misma
aplicación e infraestructura, reduciendo costes. El reto es aislar:

- **Datos:** que un tenant no acceda a los de otro.
- **Rendimiento:** evitar el "noisy neighbor" (un tenant con carga alta degrada a los demás).
- **Configuración:** personalización por tenant sin duplicar el código.

Modelos de aislamiento:

| Modelo | Aislamiento | Coste | Complejidad |
|---|---|---|---|
| Base de datos por tenant | Alto | Alto | Media |
| Esquema por tenant | Medio | Medio | Media |
| Tabla compartida con `tenant_id` | Bajo | Bajo | Baja, pero exige disciplina |
| Híbrido | Ajustable | Variable | Alta |

Considera propagación del contexto de tenant, cifrado, límites de tasa por tenant,
onboarding/offboarding, cumplimiento y pruebas de fuga entre tenants.

##### 15.3 Data Mesh

Enfoque organizacional y arquitectónico para escalar la gestión de datos en organizaciones
grandes. En lugar de centralizar todo en un data lake/warehouse y un equipo central, propone:

1. **Propiedad por dominio:** los equipos que producen los datos los poseen.
2. **Datos como producto:** calidad, documentación, SLA y contrato de datos.
3. **Plataforma de autoservicio:** infraestructura común para publicar y consumir datos.
4. **Gobernanza federada y computacional:** políticas comunes aplicadas automáticamente.

No es solo tecnología: requiere cambio organizacional. Resuelve el cuello de botella del
equipo central, a costa de coordinación, estándares y gobernanza.

##### 15.4 TOGAF ADM

TOGAF es un marco de arquitectura empresarial. Su núcleo es el **ADM** (Architecture
Development Method), un ciclo iterativo de fases:

- **Preliminary:** preparación y principios.
- **A — Visión de la arquitectura.**
- **B — Arquitectura de negocio.**
- **C — Arquitecturas de sistemas de información** (datos y aplicaciones).
- **D — Arquitectura tecnológica.**
- **E — Oportunidades y soluciones.**
- **F — Planificación de la migración.**
- **G — Gobernanza de la implementación.**
- **H — Gestión del cambio arquitectónico.**
- **Requirements Management** en el centro, alimentando todas las fases.

El ADM opera a nivel de toda la organización, no de un solo sistema, y busca alinear negocio
y tecnología. Es iterativo; no obliga a un waterfall. Se complementa con marcos ágiles y de
gobierno.

##### En la entrevista

- Explica Zero Trust con "nunca confíes, siempre verifica" y los tres principios.
- Diferencia los modelos de multi-tenancy por aislamiento, coste y complejidad.
- Explica Data Mesh con sus cuatro principios y advierte que es organizacional.
- Describe el ADM como ciclo iterativo y menciona que es enterprise, no solo solución.

##### Aplicación al caso Pólizas

Si la solución se ofrece a varias cadenas de tiendas, multi-tenant con `tenant_id` o esquema
por tenant según el aislamiento requerido. Zero Trust entre gateway, servicios y base de
datos con mTLS y autorización por servicio. Data Mesh aplica si la organización quiere que
cada dominio (pólizas, inventario, finanzas) publique sus datos analíticos. TOGAF ADM sirve
para planificar el rollout empresarial por fases.

##### Práctica de recuperación activa

1. Enumera los tres principios de Zero Trust y dos mecanismos.
2. Compara tres modelos de multi-tenancy.
3. Explica los cuatro principios de Data Mesh.
4. Nombra las fases A–D del ADM y di qué produce cada una.

- [ ] Puedo explicar Zero Trust y diferenciarlo del perímetro.
- [ ] Sé elegir un modelo multi-tenant con trade-offs.
- [ ] Entiendo Data Mesh y TOGAF ADM a alto nivel.

---

## 6. Chuleta de comparaciones

| Par | Diferencia esencial |
|---|---|
| Arquitectura vs diseño | Decisiones globales costosas de cambiar vs decisiones locales reversibles |
| Acoplamiento vs cohesión | Dependencia entre módulos vs relación interna dentro de un módulo |
| Capas vs tres capas | Organización lógica vs despliegue físico separado |
| Monolito vs microservicios | Un artefacto vs servicios independientes; simplicidad vs autonomía y complejidad |
| MVC vs capas | Patrón de presentación vs estilo de organización del sistema |
| Relacional vs NoSQL | Esquema/ACID/joins vs flexibilidad/escalado horizontal/consistencia relajada |
| Vertical vs horizontal | Más potencia en un nodo vs más nodos |
| Round Robin vs Least Connections | Turnos fijos vs menor carga actual |
| Cache-aside vs write-through | La app llena la caché bajo demanda vs escritura sincrónica en caché y BD |
| Síncrono vs asíncrono | Espera respuesta vs publica y continúa |
| Cola vs pub/sub | Un consumidor por mensaje vs copia a todos los suscriptores |
| CAP CP vs AP | Rechazar para conservar consistencia vs responder con datos posiblemente stale |
| Consistencia fuerte vs eventual | Todos ven lo mismo de inmediato vs convergencia posterior |
| CQRS vs Event Sourcing | Separar lectura/escritura vs persistir eventos |
| 2PC vs Saga | Atomicidad fuerte con bloqueo vs transacciones locales con compensación |
| Circuit Breaker vs Bulkhead | Cortar llamadas a dependencia fallida vs aislar recursos |
| API Gateway vs Service Mesh | Entrada externa vs comunicación interna entre servicios |
| VM vs contenedor | SO completo y kernel propio vs comparte kernel y es más ligero |
| Blue-green vs canary | Cambio total de tráfico vs liberación gradual |
| Lambda vs Kappa | Batch + streaming vs solo streaming con replay |
| Zero Trust vs perímetro | Verificar siempre vs confiar en la red interna |
| Data Mesh vs data lake central | Propiedad por dominio vs centralización |

---

## 7. Cómo responder en una entrevista

### 7.1 Marco de respuesta en 60–90 segundos

1. **Aclara el contexto:** "Depende de los requisitos de consistencia, escala y equipo".
2. **Define el concepto** en una frase.
3. **Estructura** en dos o tres puntos.
4. **Compara trade-offs:** qué ganas y qué pierdes.
5. **Da un ejemplo** concreto, preferiblemente del caso Pólizas.
6. **Cierra con cómo lo validarías:** métricas, pruebas, SLOs.

Plantilla:

> "La decisión depende de X. La opción A ofrece ... a cambio de ...; la opción B ofrece ...
> pero ... . En un sistema como Pólizas elegiría ... porque ... . Lo validaría midiendo ... y
> revisando ... ."

### 7.2 Frases útiles

- "Eso depende del atributo de calidad que prioricemos".
- "El trade-off principal es consistencia vs disponibilidad".
- "No lo llevaría a microservicios sin madurez operativa y límites de dominio claros".
- "La caché mejora latencia, pero introduce el problema de invalidación".
- "La decisión es reversible a bajo coste, así que podemos empezar simple".
- "Mediría el p99, la tasa de errores y el lag de la cola".

### 7.3 Errores comunes

- Responder con absolutos: "siempre microservicios", "NoSQL es mejor".
- Nombrar tecnologías sin explicar el problema.
- Ignorar costes operativos y de equipo.
- No mencionar trade-offs ni alternativas.
- Confundir conceptos parecidos: CQRS vs Event Sourcing, API Gateway vs Service Mesh,
  HA vs tolerancia a fallos, cola vs pub/sub.
- No dar ejemplos.
- Sobrearquitecturar un problema simple.

### 7.4 Si no sabes algo

No inventes. Razona desde primeros principios:

> "No tengo experiencia directa con esa tecnología, pero el problema que resuelve es ...
> y lo abordaría considerando ... . ¿Es correcto que ...?"

Demuestra criterio, no memoria.

### 7.5 Preguntas abiertas para practicar

1. Diseña la arquitectura de una plataforma de pólizas para 500 tiendas.
2. ¿Cómo migrarías el módulo legacy de inventario sin detener el negocio?
3. ¿Cómo garantizarías que no se dupliquen cargos si el cliente reintenta?
4. ¿Qué cambiarías si el sistema debe operar en dos regiones?
5. ¿Cómo detectarías y contenerías un fallo en cascada?
6. ¿Qué métricas usarías para saber si la arquitectura cumple?
7. ¿Cómo aislarías a los tenants en una versión SaaS?
8. ¿Cuándo justificarías Event Sourcing?
9. ¿Cómo diseñarías el despliegue de una nueva versión sin downtime?
10. ¿Qué decisiones documentarías con ADRs y por qué?

---

## 8. Simulacros y registro de errores

### 8.1 Calendario de simulacros

| Momento | Alcance | Meta |
|---|---|---|
| Fin de semana 2 | Preguntas 1–20 (Básico) | ≥ 16/20 |
| Fin de semana 4 | Preguntas 21–50 | ≥ 80 % |
| Fin de semana 5 | Preguntas 41–60 (Avanzado) | ≥ 75 % |
| Semana 6 | Quiz completo (60) | ≥ 80 % (umbral de `config.yml`) |
| Semana 6 | Segundo quiz completo | ≥ 90 % y cero errores repetidos |

Usa la app de consola para el simulacro completo y la GUI para filtrar por nivel o
categoría. El modo estudio de la GUI sirve para revisar explicaciones, no para medirte.

### 8.2 Cómo revisar un simulacro

1. Anota todas las falladas y las dudosas acertadas.
2. Para cada una, escribe por qué la correcta es correcta y por qué cada distractor es falso.
3. Clasifica el error (concepto, confusión, lectura, descarte).
4. Crea una tarjeta y prográmala a 1, 3, 7 y 14 días.
5. Vuelve a explicar el concepto en voz alta sin mirar.
6. Repite solo las preguntas falladas antes del siguiente simulacro.

### 8.3 Plantilla de registro

| Fecha | Pregunta | Concepto | Tipo de error | Corrección | Repaso 1 | Repaso 2 | Repaso 3 |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

### 8.4 Entrevista simulada

Pide a otra persona (o hazlo en voz alta) que te haga 5 preguntas abiertas de la sección 7.5.
Grabar la respuesta ayuda a detectar muletillas, falta de estructura y exceso de detalle.
Evalúa:

- ¿Aclaraste el contexto?
- ¿Diste una definición clara?
- ¿Mencionaste trade-offs?
- ¿Usaste un ejemplo?
- ¿Cerraste con validación o siguiente paso?
- ¿Respondiste en 90 segundos o divagaste?

---

## 9. Checklist de cobertura

Marca cada pregunta cuando puedas explicar su concepto **sin mirar la respuesta** y dar un
ejemplo propio.

### Fundamentos (L1–L6)

- [ ] 1. Definición de arquitectura de software — L1
- [ ] 2. Arquitectura vs diseño — L1
- [ ] 3. Atributos de calidad — L2
- [ ] 4. Stakeholders — L1
- [ ] 5. Arquitectura en capas — L4
- [ ] 6. Cliente-servidor — L4
- [ ] 7. Monolito vs microservicios — L4
- [ ] 8. SRP — L3
- [ ] 9. OCP — L3
- [ ] 10. Acoplamiento — L3
- [ ] 11. Cohesión — L3
- [ ] 12. Separation of Concerns — L3
- [ ] 13. Idempotencia en REST — L5
- [ ] 14. Relacional vs NoSQL — L5
- [ ] 15. MVC — L4
- [ ] 16. Escalabilidad vertical vs horizontal — L6
- [ ] 17. Alta disponibilidad — L2
- [ ] 18. Diagramas de arquitectura y C4 — L1
- [ ] 19. Punto único de falla (SPOF) — L2
- [ ] 20. Arquitectura de tres capas — L4

### Estilos, patrones y distribuidos (L7–L13)

- [ ] 21. Event-Driven Architecture — L7
- [ ] 22. Arquitectura hexagonal — L8
- [ ] 23. CQRS — L9
- [ ] 24. Event Sourcing — L9
- [ ] 25. Bounded Context — L8
- [ ] 26. Aggregate — L8
- [ ] 27. Circuit Breaker — L10
- [ ] 28. Saga — L10
- [ ] 29. API Gateway — L11
- [ ] 30. Service Mesh — L11
- [ ] 31. Comunicación síncrona vs asíncrona — L7
- [ ] 32. Round Robin vs Least Connections — L6
- [ ] 33. Cache-aside vs write-through — L6
- [ ] 34. Cola de mensajes vs pub/sub — L7
- [ ] 35. Teorema CAP — L12
- [ ] 36. Consistencia eventual — L12
- [ ] 37. Strangler Fig — L14
- [ ] 38. Contenedores vs máquinas virtuales — L11
- [ ] 39. Pod de Kubernetes — L11
- [ ] 40. Serverless / FaaS — L11
- [ ] 41. CAP: AP vs CP — L12
- [ ] 42. Consistent hashing — L12
- [ ] 43. Patrón Sidecar — L11
- [ ] 44. Backpressure — L13
- [ ] 45. 2PC vs Saga — L13
- [ ] 46. Particionamiento y orden en Kafka — L12
- [ ] 47. Blue-green vs canary — L14
- [ ] 48. Chaos Engineering — L14
- [ ] 49. Cold start — L11
- [ ] 50. CRDTs — L12
- [ ] 51. Zero Trust — L15
- [ ] 52. Multi-tenant — L15
- [ ] 53. Data Mesh — L15
- [ ] 54. Pilares de observabilidad — L14
- [ ] 55. Bulkhead — L10
- [ ] 56. Lambda vs Kappa — L13
- [ ] 57. Distributed tracing — L14
- [ ] 58. TOGAF ADM — L15
- [ ] 59. Feature flags — L14
- [ ] 60. Fitness functions — L14

---

## 10. Glosario de siglas

| Sigla | Significado |
|---|---|
| ACL | Anti-Corruption Layer |
| ACID | Atomicity, Consistency, Isolation, Durability |
| ADM | Architecture Development Method (TOGAF) |
| ADR | Architecture Decision Record |
| API | Application Programming Interface |
| BFF | Backend for Frontend |
| CAP | Consistency, Availability, Partition tolerance |
| CQRS | Command Query Responsibility Segregation |
| CRDT | Conflict-free Replicated Data Type |
| DDD | Domain-Driven Design |
| DLQ | Dead Letter Queue |
| EDA | Event-Driven Architecture |
| FaaS | Function as a Service |
| HA | High Availability |
| K8s | Kubernetes |
| L4/L7 | Capas del modelo OSI (transporte/aplicación) |
| MVC | Model-View-Controller |
| PACELC | Partition, Availability, Consistency, Else Latency, Consistency |
| REST | Representational State Transfer |
| RTO/RPO | Recovery Time Objective / Recovery Point Objective |
| SLA/SLI/SLO | Service Level Agreement / Indicator / Objective |
| SPOF | Single Point of Failure |
| SRP/OCP/LSP/ISP/DIP | Principios SOLID |
| TOGAF | The Open Group Architecture Framework |
| 2PC | Two-Phase Commit |

---

## 11. Recursos del repositorio

| Archivo | Uso recomendado |
|---|---|
| [`README.md`](README.md) | Leer la explicación completa de cada pregunta |
| [`architectural-interview-questions.json`](architectural-interview-questions.json) | Practicar con la app y filtrar por nivel/categoría |
| [`self-test-app/architecture_quiz_console.py`](self-test-app/architecture_quiz_console.py) | Simulacros completos y gráfico de resultados |
| [`self-test-app/architecture_quiz_gui.py`](self-test-app/architecture_quiz_gui.py) | Quiz rápido, personalizado, por nivel/categoría y modo estudio |
| [`self-test-app/config.yml`](self-test-app/config.yml) | Ajustar umbral de aprobación y número de preguntas |
| [`ejercicio-arquitectura-polizas/01-listado-impacto.md`](ejercicio-arquitectura-polizas/01-listado-impacto.md) | Caso de negocio y componentes afectados |
| [`ejercicio-arquitectura-polizas/02-arquitectura-general.puml`](ejercicio-arquitectura-polizas/02-arquitectura-general.puml) | Vista general para aplicar C4 y capas |
| [`ejercicio-arquitectura-polizas/03-arquitectura-tecnologica.puml`](ejercicio-arquitectura-polizas/03-arquitectura-tecnologica.puml) | Despliegue, HA, balanceo y SPOF |
| [`ejercicio-arquitectura-polizas/04-diagrama-secuencia.puml`](ejercicio-arquitectura-polizas/04-diagrama-secuencia.puml) | Transacciones, idempotencia y Saga |
| [`ejercicio-arquitectura-polizas/05-diagrama-datos.puml`](ejercicio-arquitectura-polizas/05-diagrama-datos.puml) | Agregados, modelo relacional y datos |

### Flujo sugerido con la app

1. Diagnóstico: quiz completo en consola.
2. Estudio: lección + preguntas del banco + modo estudio de la GUI.
3. Práctica: quiz personalizado por lección o nivel.
4. Simulacro: quiz completo sin ayudas.
5. Repaso: solo preguntas falladas y tarjetas de error.

### Regla de oro

Si no puedes explicar un concepto en **90 segundos, con un ejemplo y un trade-off**, todavía
no lo dominas. Vuelve a la lección, dibújalo y explícalo en voz alta.
