# Clean Architecture a nivel doctoral

Oct 29, 2026 · @Isidro Leos Viscencio

## Primeros principios

La arquitectura de software es la disciplina de decidir qué cambios serán baratos y cuáles caros. Clean Architecture es una respuesta concreta: hacer que las reglas de negocio no dependan de la tecnología, controlando la dirección de las dependencias del código fuente.

La tesis se construye con cinco proposiciones, cada una apoyada en la anterior:

1. El software vale por dos cosas: lo que hace hoy (comportamiento) y lo fácil que es cambiarlo mañana (estructura). El nombre "soft"ware promete lo segundo. Martin sostiene que la estructura es la más valiosa de las dos, porque un sistema que funciona y no se puede cambiar queda obsoleto, mientras que uno que se puede cambiar se corrige y se adapta.
2. El cambio es la condición normal, no la excepción. Las leyes de Lehman (1980) formalizan que un sistema en uso debe evolucionar continuamente y que su complejidad crece si nadie la contiene.
3. La complejidad se divide en esencial, la del problema, y accidental, la que introducen nuestras herramientas (Brooks, 1986). Ousterhout (2018) la reduce a dos síntomas medibles: dependencias y opacidad.
4. Un módulo A depende de B cuando un cambio en B puede obligar a cambiar A. Lo que importa es el radio de impacto, el número de módulos alcanzables hacia atrás por esas dependencias:

```latex
B(m) = \left| \{\, x \in M \;:\; x \rightarrow^{*} m \,\} \right|
```

Una buena arquitectura intenta minimizar el radio de impacto esperado de los cambios más probables. Es una heurística, no un teorema: depende de qué cambios se consideran probables.

Quinta proposición: no todo cambia al mismo ritmo ni por las mismas razones. Las políticas (reglas de negocio) cambian por razones de negocio; los detalles (base de datos, framework, protocolo) cambian por razones técnicas y de mercado. Si ambos viven mezclados, cualquier cambio técnico toca el negocio y al revés.

De ahí sale la idea central. Si las políticas son lo estable y valioso, y los detalles lo volátil y reemplazable, las dependencias del código deben apuntar de lo volátil hacia lo estable. Eso es la regla de dependencia. Todo lo demás en Clean Architecture es el andamiaje para lograrlo.

## Fundamentos teóricos

Clean Architecture no inventa ideas nuevas: sintetiza seis líneas de pensamiento que llevan décadas madurando. Entenderlas por separado permite saber qué parte de la arquitectura viene de cuál y dónde se puede flexibilizar.

| Línea teórica | Idea central | Qué aporta a Clean Architecture |
| --- | --- | --- |
| Ocultamiento de información (Parnas, 1972) | Se descompone un sistema en módulos por las decisiones de diseño que es probable que cambien, y cada módulo esconde una de ellas | El criterio de descomposición: separar por razones de cambio, no por pasos del proceso. Es el origen de la separación entre política y detalle |
| Separación de responsabilidades (Dijkstra, 1974; sistema THE, 1968) | Estudiar un aspecto a la vez; organizar el sistema en niveles donde cada uno solo conoce los inferiores | La idea de capas, y su límite: las capas clásicas hacen que el negocio dependa de la persistencia |
| Acoplamiento y cohesión (Stevens, Myers y Constantine, 1974) | Un buen módulo tiene alta cohesión interna y bajo acoplamiento con los demás | El vocabulario para juzgar cualquier frontera: qué va junto y qué se separa |
| Principios SOLID (Meyer, 1988; Liskov, 1987; Martin, 2000 en adelante) | Abierto/cerrado, sustitución de Liskov, segregación de interfaces, inversión de dependencias, responsabilidad única | La inversión de dependencias (DIP) es el mecanismo técnico que permite que el código apunte hacia adentro aunque el flujo de ejecución salga hacia afuera |
| Principios de componentes (Martin) | Cohesión: REP, CCP, CRP. Acoplamiento: ADP, SDP, SAP, con las métricas de inestabilidad y abstracción | Los criterios para agrupar clases en componentes desplegables y la dirección en que deben depender: hacia lo estable y abstracto |
| Ley de Conway (1968) y DDD (Evans, 2003) | La estructura del sistema refleja la de la organización que lo construye. El modelo del dominio debe ser el centro del diseño, con contextos delimitados | Por qué las entidades y los casos de uso están en el centro, y por qué las fronteras técnicas deben alinearse con las fronteras de equipo y de negocio |

Dos conceptos de esa tabla merecen precisión porque son los que más se confunden en entrevista.

La inversión de dependencias no es lo mismo que la inyección de dependencias. La primera es un principio de diseño: los módulos de alto nivel no deben depender de los de bajo nivel, ambos dependen de abstracciones, y las abstracciones pertenecen al lado de la política. La segunda es una técnica para entregar en tiempo de ejecución la implementación concreta. Se puede inyectar sin invertir (un servicio que recibe por constructor una clase concreta de infraestructura) y se puede invertir sin un contenedor de inyección.

La inestabilidad de un componente se mide como I = Ce / (Ca + Ce), donde Ce son sus dependencias salientes y Ca las entrantes. Un componente con muchas dependencias entrantes y pocas salientes es estable: cambiarlo es caro porque muchos dependen de él. El principio de dependencias estables dice que se debe depender en la dirección de la estabilidad, y por eso las reglas de negocio, que queremos que cambien poco, ocupan el centro.

## Evolución histórica

Clean Architecture (2012) es el último eslabón visible de una cadena de seis décadas de intentos por separar lo que cambia de lo que no. Cada hito resolvió un problema del anterior.

| Año | Hito | Qué problema atacó | Qué dejó sin resolver |
| --- | --- | --- | --- |
| 1968 | Sistema THE (Dijkstra) y ley de Conway | Dominar la complejidad con niveles de abstracción; el diseño refleja a la organización | Las capas permiten que lo alto dependa de lo bajo, incluida la persistencia |
| 1972 | Ocultamiento de información (Parnas) | Descomponer por decisiones que cambiarán, no por pasos del flujo | Es un criterio, no una estructura de paquetes ni una regla de dependencia |
| 1974 | Acoplamiento y cohesión (Stevens, Myers, Constantine); separación de responsabilidades (Dijkstra) | Un vocabulario para medir la calidad de las fronteras | Sin criterio sobre la dirección de las dependencias |
| 1979 | Model-View-Controller (Reenskaug) | Separar el modelo de dominio de la presentación | Cubre la UI, no la persistencia ni la integración con sistemas externos |
| 1988 | Principio abierto/cerrado (Meyer); sustitución de Liskov en 1987 | Extender sin modificar; subtipos intercambiables | Operan dentro de un módulo, no definen una arquitectura |
| 1990s | Arquitectura en capas y n-tier (presentación, lógica, datos) | Estandarizar la separación por responsabilidad técnica | La lógica de negocio depende de la capa de datos; cambiar la base de datos obliga a tocar el negocio |
| 2000 | Principios SOLID (Martin), incluida la inversión de dependencias | Una herramienta técnica para invertir esa dependencia | Faltaba un modelo que los combinara en una estructura de sistema |
| 2003 | Domain-Driven Design (Evans) | Poner el modelo del dominio en el centro y delimitar contextos | No prescribe la estructura de dependencias de la infraestructura |
| Ene. 2005 | Arquitectura hexagonal, o puertos y adaptadores (Cockburn) | Que la aplicación sea indiferente a si la conduce un usuario, un test o un lote, y a qué base de datos usa | Define puertos y adaptadores, pero no subdivide el interior |
| 2008 | Arquitectura de cebolla (Palermo, partes 1 a 3) | El modelo de dominio al centro y las dependencias hacia adentro, con anillos | Las capas internas quedan menos prescritas que en Clean Architecture |
| 12 ago. 2012 | The Clean Architecture (Martin, blog) | Sintetiza hexagonal, cebolla, DCI y BCE bajo una regla de dependencia | Es una guía, con costos propios (ver críticas) |
| 2017 | Libro Clean Architecture (Martin) | Desarrolla los principios de componentes y la arquitectura como política y detalle | Sus costos de aplicación están en la sección de críticas |
| 2010s en adelante | Microservicios, vertical slices, monolito modular, arquitectura evolutiva | Escalar por equipos y despliegues; organizar por capacidad de negocio | Se combinan con las ideas anteriores en vez de reemplazarlas |

Las fechas de la arquitectura hexagonal (enero de 2005), la cebolla (2008 con una cuarta parte en 2013) y el artículo de Martin (13 de agosto de 2012) las verifiqué en las fuentes citadas en la bibliografía. El resto son fechas de las publicaciones originales conocidas, y la sección de bibliografía indica cuáles no pude verificar en esta sesión.

## Clean Architecture a fondo

La regla es una sola: las dependencias del código fuente solo pueden apuntar hacia adentro. Nada en un círculo interior puede nombrar algo declarado en uno exterior, ni una clase, ni una función, ni una variable. El resto de la arquitectura es consecuencia de esa regla.

Los cuatro círculos del diagrama de Martin son un esquema, no un límite: él mismo dice que puede haber más o menos de cuatro, siempre que la regla se cumpla.

&#91;embedded content: círculos de Clean Architecture y cruce de una frontera · 4 círculos, 4 cajas\]

A la izquierda, los cuatro círculos con la flecha de dependencia hacia el centro. A la derecha, cómo un caso de uso llega a la base de datos sin conocerla.

| Círculo | Contiene | Cambia por | Ejemplo en Java |
| --- | --- | --- | --- |
| Entidades | Reglas de negocio de toda la empresa, independientes de cualquier aplicación | Cambios del negocio mismo; es lo más estable | Una clase Pedido con sus invariantes, un objeto de valor Dinero |
| Casos de uso | Reglas de una aplicación concreta; orquestan las entidades y definen los puertos | Cambios en lo que hace la aplicación | CrearPedido, ReservarInventario, y las interfaces que necesitan |
| Adaptadores de interfaz | Convierten datos entre el formato del caso de uso y el del exterior | Cambios en formatos y protocolos | Controlador REST, mapeadores, repositorio que implementa el puerto |
| Frameworks y drivers | El pegamento con lo concreto: base de datos, web, mensajería | Cambios de herramienta o de proveedor; es lo más volátil | Quarkus o Spring Boot, JDBC, el cliente de Kafka |

### El problema de cruzar fronteras

Hay una tensión aparente. En ejecución, el flujo de control sale hacia afuera: un caso de uso necesita guardar un pedido, así que llama a la base de datos. Pero la regla prohibe que el caso de uso conozca la base de datos. Se resuelve con la inversión de dependencias: el caso de uso declara una interfaz (el puerto) en su propio círculo, y un adaptador exterior la implementa. La llamada va hacia afuera; la dependencia del código va hacia adentro.

Tres corolarios prácticos salen de ahí:

1. **Los datos que cruzan una frontera son estructuras simples.** No se pasa una entidad ni una fila de base de datos hacia adentro o afuera; se pasan objetos de transferencia que el círculo receptor puede entender sin arrastrar el del emisor.
2. **El presentador es un objeto humilde.** La lógica de qué mostrar vive en el caso de uso o en el presentador; la vista solo pinta. Así lo difícil de probar queda reducido a lo mínimo.
3. **Las fronteras pueden ser parciales.** Martin describe en su libro alternativas más baratas que la separación completa, como omitir el último paso de la separación o usar una fachada, para cuando todavía no sabes si la frontera hará falta. Es una decisión que se documenta y se revisa.

### Las métricas de componentes

Para decidir qué tan sana es una frontera entre componentes, Martin usa dos medidas. La inestabilidad I va de 0 (estable, muchos dependen de él) a 1 (inestable, depende de muchos). La abstracción A es la proporción de clases abstractas e interfaces del componente. La distancia a la secuencia principal D indica cuánto se aleja un componente del equilibrio ideal entre ambas:

```latex
I = \frac{C_e}{C_a + C_e} \qquad A = \frac{N_a}{N_c} \qquad D = \left| A + I - 1 \right|
```

Un componente estable y concreto (I cerca de 0, A cerca de 0) cae en la "zona de dolor": muchos dependen de él y es difícil de cambiar. Uno inestable y abstracto (I cerca de 1, A cerca de 1) cae en la "zona de inutilidad": nadie lo usa. El objetivo es quedar cerca de la secuencia principal, con lo estable siendo abstracto y lo concreto siendo inestable.

## Críticas y límites

Un nivel doctoral exige poder argumentar en contra. Clean Architecture compra independencia de los detalles a cambio de indirección, y esa compra no siempre conviene. Estas son las objeciones serias.

1. **Ceremonia de mapeo.** Cada frontera suele traer sus propios modelos de datos (entidad de dominio, modelo de persistencia, DTO de entrada y de salida) y el código que los traduce. En una aplicación que en esencia es CRUD, ese código es costo sin beneficio.
2. **Dominio anémico.** Si los casos de uso concentran toda la lógica y las entidades son bolsas de datos, se cae en el anti-patrón que Fowler describió en 2003. La estructura es limpia y el dominio sigue sin modelarse.
3. **La independencia del framework es parcial.** Anotaciones de JPA en las entidades o de Spring en los casos de uso filtran detalles al centro. Existen dos posturas válidas: separar estrictamente con modelos duplicados, o aceptar un número pequeño de anotaciones y vigilar la regla de dependencia con pruebas arquitectónicas (ArchUnit).
4. **Capas frente a rebanadas.** Organizar por capas técnicas dispersa un cambio de negocio en muchos paquetes. Las rebanadas verticales (Bogard) y el empaquetado por componente (Brown) agrupan por funcionalidad, y Clean Architecture se puede aplicar dentro de cada rebanada.
5. **Profundidad de los módulos.** Ousterhout (2018) defiende módulos profundos, con interfaz pequeña y mucha funcionalidad detrás, y advierte que fragmentar en muchas clases diminutas aumenta la complejidad. Aplicada de forma mecánica, la arquitectura limpia puede producir justo eso.
6. **Evidencia empírica limitada.** No conozco estudios controlados sólidos que demuestren que Clean Architecture mejore resultados medibles frente a alternativas. Se apoya en argumentos de diseño y en experiencia profesional, y conviene decirlo así.
7. **No resuelve lo distribuido.** La regla de dependencia ordena dependencias de código dentro de un proceso. En microservicios aparecen acoplamientos de ejecución (latencia, disponibilidad, consistencia, dueño de los datos) que requieren otras herramientas: contratos, eventos, idempotencia, sagas.

Con esas objeciones, la decisión de usarla se vuelve contextual:

| Contexto | Recomendación |
| --- | --- |
| Dominio rico que vivirá años, con muchas reglas que cambian | Aplicar completa en el núcleo: entidades, casos de uso y puertos |
| Muchas integraciones con sistemas externos que cambian de proveedor o de contrato | Puertos y adaptadores en cada integración, con capa anticorrupción |
| CRUD con poca lógica | Estructura simple por rebanada; sin capas de ceremonia |
| Servicio pequeño de un solo propósito | Un módulo profundo con pruebas; basta la regla de dependencia a nivel de paquetes |
| Migración de un monolito heredado | Estrangular por contexto delimitado y aplicar la arquitectura en lo nuevo, no reescribir todo |

## Bibliografía clave en orden de lectura

La lista sigue el orden en que conviene leer, de los fundamentos a la práctica. En la última columna distingo lo que pude comprobar en esta sesión (la página existe y coincide con el título y la fecha) de lo que cito de memoria: verifica edición y páginas antes de usar cualquiera en un documento formal.

| # | Obra | Por qué leerla | Estado |
| --- | --- | --- | --- |
| 1 | Parnas, [On the Criteria to Be Used in Decomposing Systems into Modules](https://asw.inf.uniroma3.it/altrui/parnas-1972.pdf), Communications of the ACM, 1972 | El origen del criterio "separa por decisiones que cambiarán" | Comprobada |
| 2 | Brooks, No Silver Bullet: Essence and Accident in Software Engineering, 1986 | Complejidad esencial frente a accidental | De memoria |
| 3 | Lehman, [Programs, Life Cycles, and Laws of Software Evolution](https://ieeexplore.ieee.org/document/1456074), Proceedings of the IEEE, 1980 | Por qué los sistemas en uso deben cambiar y se degradan | Comprobada |
| 4 | Stevens, Myers y Constantine, Structured Design, IBM Systems Journal, 1974 | Origen de acoplamiento y cohesión | De memoria |
| 5 | Dijkstra, The Structure of the THE Multiprogramming System (1968) y On the Role of Scientific Thought (1974) | Niveles de abstracción y separación de responsabilidades | De memoria |
| 6 | Conway, How Do Committees Invent?, Datamation, 1968 | La estructura del sistema copia a la de la organización | De memoria |
| 7 | Perry y Wolf, Foundations for the Study of Software Architecture, 1992 | Definición académica de arquitectura de software | De memoria |
| 8 | Cockburn, [Hexagonal Architecture](https://alistaircockburn.com/Articles/Hexagonal-Architecture), enero de 2005 | Puertos y adaptadores, la base conceptual de Clean Architecture | Comprobada |
| 9 | Palermo, The Onion Architecture, partes 1 a 3 (2008) y parte 4 (2013); [resumen y comentario de Graca](https://herbertograca.com/2017/09/21/onion-architecture/) | Dominio al centro con dependencias hacia adentro | Comprobada a través del resumen; busca el original |
| 10 | Martin, [The Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html), 13 de agosto de 2012 | El texto fundacional, corto; léelo antes que el libro | Comprobada a través de un resumen; abre el original |
| 11 | Martin, [Clean Architecture: A Craftsman's Guide to Software Structure and Design](https://www.pearson.com/us/higher-education/program/Bob-Clean-Code-A-Handbook-of-Agile-Software-Craftsmanship/PGM333762.html), 2017 | Principios SOLID y de componentes, política frente a detalle, fronteras | Comprobada |
| 12 | Evans, [Domain-Driven Design: Tackling Complexity in the Heart of Software](https://www.pearson.com/en-gb/subject-catalog/p/domain-driven-design-tackling-complexity-in-the-heart-of-software/P200000009375), 2003 | Modelo del dominio, contextos delimitados, capa anticorrupción | Comprobada |
| 13 | Vernon, Implementing Domain-Driven Design, 2013 | DDD con arquitectura hexagonal en código concreto | De memoria |
| 14 | Ousterhout, [A Philosophy of Software Design](https://web.stanford.edu/~ouster/cgi-bin/aposd.php), 2018 (2.ª ed. 2021) | La contraparte crítica: módulos profundos y complejidad | Comprobada |
| 15 | Ford, Parsons y Kua, [Building Evolutionary Architectures](https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/ch01.html), 2.ª ed. 2022 | Funciones de aptitud: verificar la arquitectura de forma automatizada | Comprobada |
| 16 | Richards y Ford, Fundamentals of Software Architecture, 2020 | Estilos arquitectónicos y trade-offs; muy útil para entrevista | De memoria |
| 17 | Fowler, Patterns of Enterprise Application Architecture (2002) y su artículo Anemic Domain Model (2003) | Patrones de persistencia y la crítica al dominio anémico | De memoria |
| 18 | Hohpe y Woolf, Enterprise Integration Patterns, 2003 | Vocabulario de mensajería e integración, central para tu rol | De memoria |
| 19 | Richardson, Microservices Patterns, 2018 | Outbox, sagas y consistencia entre servicios | De memoria |
| 20 | Newman, Building Microservices, 2.ª ed. 2021 | Fronteras de servicio y migración desde un monolito | De memoria |
| 21 | Kleppmann, Designing Data-Intensive Applications, 2017 | Fundamentos de datos y mensajería en sistemas distribuidos | De memoria |

Si solo tienes tiempo para cinco: 1, 8, 10, 12 y 14. Cubren el criterio de descomposición, la idea de puertos, el texto fundacional, el dominio y la crítica.

## Aplicación a tu oportunidad como Arquitecto de Soluciones

El puesto, según la descripción que te pasaron, pide diseñar y programar integraciones para un ecosistema de e-commerce y omnicanalidad: plataformas digitales, apps móviles, marketplace, sistemas internos y servicios de última milla, sobre Java 17 o 21 con Quarkus o Spring Boot, microservicios, APIs REST y OpenShift. Es un perfil donde Clean Architecture rinde más que en un CRUD, porque el dolor típico es que cada tercero cambia de contrato y el negocio no debe enterarse. No conozco los sistemas internos del cliente; lo siguiente es el marco que aplicarías una vez que los veas.

### De la necesidad al patrón

| Necesidad del rol | Patrón | Cómo se ve en el código |
| --- | --- | --- |
| Integrar marketplace y última milla, que son APIs de terceros que cambian | Puerto de salida por capacidad (por ejemplo, calcular envío o publicar producto) más un adaptador por proveedor y una capa anticorrupción que traduce el modelo ajeno al tuyo | Una interfaz en la capa de aplicación y un adaptador por proveedor con su propio cliente REST y mapeo. Cambiar de proveedor es agregar un adaptador |
| Un mismo pedido llega por web, app o tienda | Un caso de uso por intención de negocio (crear pedido, reservar inventario, cancelar) con varios adaptadores de entrada | El mismo caso de uso lo invocan un controlador REST, un consumidor de eventos y una prueba. Los canales no duplican reglas |
| Reglas que cambian seguido (promociones, precios, elegibilidad) | Entidades y servicios de dominio sin dependencias de framework | Pruebas unitarias en milisegundos, sin contenedor ni base de datos |
| Comunicar contextos de forma confiable | Puerto de publicación de eventos, outbox transaccional y consumidores idempotentes | Lo que repasas para Kafka encaja aquí: el adaptador de salida escribe en la tabla outbox y otro proceso publica |
| Resiliencia ante terceros lentos o caídos | Tiempos de espera, reintentos acotados, interruptor de circuito y degradación elegante, todo en el adaptador | SmallRye Fault Tolerance en Quarkus o Resilience4j en Spring Boot, nunca en el dominio |
| Correr en OpenShift | Configuración externa, sondas de salud y observabilidad como detalle de infraestructura | Los adaptadores leen la configuración; el dominio la recibe ya resuelta. Puedes probar el núcleo sin clúster |
| Si el cliente usa Magento o Adobe Commerce (la descripción lo menciona como plus) | Tratarlo como un sistema externo detrás de un puerto, con anticorrupción | Su modelo de producto y de orden no se filtra a tus entidades; hablas con él por su API |

### Estructura de módulos sugerida

Un proyecto Maven multimódulo hace que la regla de dependencia sea verificable por el compilador y no solo por disciplina:

```text
pedidos/
  dominio/            entidades, objetos de valor, servicios de dominio. Sin dependencias externas
  aplicacion/         casos de uso y puertos (interfaces). Depende solo de dominio
  adaptador-entrada/  REST, consumidores de eventos. Depende de aplicacion
  adaptador-salida/   persistencia, clientes de terceros, publicación de eventos. Depende de aplicacion
  arranque/           Quarkus o Spring Boot: ensambla todo e inyecta los adaptadores
```

La práctica más útil para entrevista es hacer cumplir la regla con una prueba arquitectónica, como en la idea de funciones de aptitud de la arquitectura evolutiva:

```java
@AnalyzeClasses(packages = "com.empresa.pedidos")
class ArquitecturaTest {

  @ArchTest
  static final ArchRule dominio_sin_dependencias_externas =
      noClasses().that().resideInAPackage("..dominio..")
          .should().dependOnClassesThat().resideInAnyPackage(
              "..aplicacion..", "..adaptador..",
              "jakarta.persistence..", "org.springframework..", "io.quarkus..");
}
```

Si quieres permitir algunas anotaciones de JPA en el dominio por pragmatismo, quita esa línea de la regla y escribe explícitamente la excepción en una decisión documentada.

### Decisiones que debes poder defender

1. **Separar o no el modelo de persistencia del de dominio.** Con un dominio rico y reglas cambiantes, sepáralos y mapea en el adaptador. Con poca lógica, comparte el modelo y acepta el acoplamiento a cambio de menos código.
2. **Un servicio por capacidad de negocio, no por capa técnica.** Las fronteras de microservicio siguen contextos delimitados (catálogo, pedidos, inventario, envíos), y Clean Architecture se aplica dentro de cada uno.
3. **Anticorrupción en cada tercero.** El costo es un mapeo por proveedor; el beneficio es poder cambiar de marketplace o transportista sin tocar el negocio.
4. **Verificación automatizada de la arquitectura.** La regla de dependencia vive en una prueba que falla en el pipeline, no en un documento que se olvida.
5. **Cada decisión con su registro.** Un ADR corto por decisión: contexto, alternativas, costo aceptado y cuándo se revisa.

Como el puesto es "hands-on", llévate un ejemplo mínimo en tu propio repositorio: un caso de uso, un puerto, dos adaptadores (uno real y uno falso para pruebas) y la prueba arquitectónica. Mostrarlo en pantalla pesa más que describirlo.

## Ruta de estudio y defensa en entrevista

Cuatro semanas a unas cinco horas por semana bastan para pasar de conocer el vocabulario a defender la arquitectura con ejemplos propios. Si tu calendario de entrevistas aprieta, comprime las semanas 1 y 2 y conserva la 3, que es la que te distingue.

| Semana | Lectura | Ejercicio | Entregable |
| --- | --- | --- | --- |
| 1. Fundamentos | Parnas (1), artículo de Cockburn (8), artículo de Martin de 2012 (10) | Explicar la regla de dependencia sin mirar y dibujarla de memoria | Un párrafo de dos minutos, en español y en inglés |
| 2. El libro | Clean Architecture de Martin: partes sobre principios de diseño, de componentes y de arquitectura; capítulos de Evans sobre contextos delimitados | Refactorizar un caso de uso real tuyo a puertos y adaptadores en Java | Un repositorio pequeño con un caso de uso, un puerto y dos adaptadores |
| 3. Crítica y verificación | Ousterhout (14), Ford, Parsons y Kua (15), artículo de Fowler sobre dominio anémico | Añadir la prueba con ArchUnit y escribir dos ADR: uno a favor y otro en contra de separar el modelo de persistencia | Dos ADR de una página |
| 4. Integración y distribuido | Hohpe y Woolf (18), Richardson (19), Newman (20) | Agregar al repositorio un adaptador a un tercero simulado con anticorrupción y un outbox que publique a Kafka | Un caso de "pedido omnicanal" que puedas mostrar en pantalla |

### Preguntas que te pueden hacer

| Pregunta | Estructura de una buena respuesta |
| --- | --- |
| Explícame Clean Architecture en dos minutos | Problema (cambio caro), idea (las dependencias del código apuntan hacia el negocio), mecanismo (inversión de dependencias, puertos), costo (mapeos e indirección) y cuándo la usas |
| ¿En qué se diferencia de la hexagonal y de la cebolla? | Comparten el principio: dominio al centro y dependencias hacia adentro. Hexagonal define puertos y adaptadores; cebolla añade anillos de dominio; Clean concreta cuatro círculos y la regla de cruce de fronteras |
| ¿Cuándo no la usarías? | CRUD con poca lógica, scripts y servicios de un solo propósito. Di el criterio: la usas donde el dominio vive años y hay integraciones que cambian |
| ¿Cómo haces que un equipo la respete? | Módulos Maven que impiden la dependencia, prueba ArchUnit en el pipeline, ADR y revisión de código centrada en las fronteras |
| ¿Cómo se relaciona con microservicios? | La regla de dependencia ordena el código dentro de un servicio; las fronteras entre servicios siguen contextos delimitados y se comunican por contratos y eventos |
| ¿Inversión de dependencias frente a inyección de dependencias? | Principio de diseño frente a técnica de entrega de la implementación. Se puede inyectar sin invertir |
| Cuéntame una vez que fue un error aplicarla | Una historia tuya con el costo real, qué aprendiste y qué harías distinto. Admitir el límite te da más credibilidad que defenderla siempre |

### Frase de apertura en inglés

Por si la entrevista es en inglés, prepara una versión corta que puedas decir sin guion:

```text
Clean Architecture is about making business rules independent of technology details.
The source code dependencies point inward, toward the domain, so I can swap a database,
a framework or a third-party API without touching the core. The cost is extra mapping
and indirection, so I apply it where the domain is rich and the integrations change often.
```
