# Pliego de ejemplo

[← Página anterior](05-garantia.md) · [Siguiente página →](../../modulos/M01-ecosistema-react/README.md)

Un supuesto teórico: una aplicación ficticia, pequeña, y el extracto de pliego que le correspondería. Mismo formato de tabla de tres columnas y mismas familias de identificadores de siempre; la numeración se ajusta al expediente real.

Sirve para dos cosas: recorrerlo entero sobre un caso que cabe en una página, y tenerlo delante el día de redactar uno de verdad.

No hay nada clausular aquí: ni precio, ni solvencia, ni plazos, ni penalizaciones.

Los requerimientos marcados **React** son los que en otro tipo de proyecto no se escriben, o se dan por cubiertos con otra cláusula. El resto es trabajo de siempre: estados sin dato, accesibilidad, diseño previo, registro de quién hizo qué.

## El supuesto

**AVISOS.** Pantallas instaladas en dependencias que muestran los avisos internos vigentes y el estado del servicio. No existe: está inventada para este ejercicio.

- **Quién la mira.** Personal de la dependencia, de paso. Nadie se identifica y nadie toca nada.
- **Quién la alimenta.** Comunicación interna, desde una herramienta con usuario y perfil.
- **De dónde salen los datos.** Dos servicios internos: uno de avisos y otro de estado del servicio.
- **Dónde corre.** En el navegador de una CPU por dependencia, encendida en continuo.
- **Cuántas pantallas.** 60 unidades, dos medidas, una de ellas en vertical.

Con eso ya se puede escribir todo lo que sigue.

## Alcance

| ID | Concepto | Descripción |
| --- | --- | --- |
| ALC.1 | Anexo de pantallas | Forma parte del alcance el anexo con la relación de pantallas: medida, resolución, orientación y número de unidades de cada combinación. |
| ALC.2 **React** | Entorno de construcción | El suministro incluye el entorno para fabricar el paquete instalable y una copia de todas las librerías de terceros utilizadas. |
| ALC.3 **React** | Pruebas automáticas | El suministro incluye las pruebas automáticas de la aplicación y el documento para lanzarlas en un equipo sin preparación previa. |
| ALC.4 | Herramienta de gestión | El suministro incluye la herramienta con la que el personal propio programa los contenidos, con su propia formación y su propia aceptación. |

**Por qué ALC.2 y ALC.3.** En un desarrollo tradicional el código fuente y el compilador bastan para volver a fabricar. En React el paquete se monta sobre librerías de terceros que no viajan en el código, y las pruebas automáticas de pantalla son el único medio de comprobar en una tarde que un evolutivo no rompió lo anterior. Si no están en el listado, no se entregan.

## Requerimientos funcionales

| ID | Concepto | Descripción |
| --- | --- | --- |
| RFUN.1 | Aplicación | El contenido de la pantalla será una aplicación web progresiva (React) responsive, que se adaptará a todas las combinaciones del anexo ALC.1. |
| RFUN.2 | Adaptación comprobable | El adjudicatario entregará una imagen de la aplicación en funcionamiento por cada combinación del anexo, para aprobación previa a las pruebas de aceptación. |
| RFUN.3 | Sin datos | Cuando el servicio de avisos responda sin avisos vigentes, la pantalla mostrará el texto aprobado en el diseño previo, y no una zona vacía. |
| RFUN.4 | Con error | Cuando el servicio de avisos no responda, responda con error o responda algo inesperado, se reintentará dos veces con intervalos de cinco segundos. Si ninguna tiene éxito, se mantendrá el último contenido válido descargado. |
| RFUN.5 | Dato mal formado | Si un aviso concreto llega con estructura o contenido inesperado, se ignorará ese aviso y se mostrarán los correctos. |
| RFUN.6 **React** | Recuperación | Al restablecerse la comunicación, la aplicación volverá a solicitar toda la información que esté mostrando, sin esperar al siguiente ciclo de refresco. |
| RFUN.7 | Arranque | Mientras el equipo arranca, y en caso de que la aplicación no llegue a arrancar, la pantalla mostrará el contenido de reserva almacenado localmente. |
| RFUN.8 **React** | Sin valores fijos | Textos, colores, medidas, posiciones, duraciones y direcciones de origen de datos serán configurables sin volver a fabricar el paquete. |
| RFUN.9 | Accesibilidad | Contrastes, tamaños de letra y tiempos de permanencia cumplirán las pautas aplicables a contenido de lectura a distancia, verificados sobre el anexo ALC.1. |

**Por qué RFUN.6 y RFUN.8.** En un programa de equipo, al volver la red el dato suele pedirse solo. En React, si nadie lo pide otra vez, la pantalla sigue mostrando lo viejo. Y los textos, colores y posiciones se suelen dejar escritos en el código: cambiar uno obliga a volver a fabricar el paquete e instalarlo en las sesenta pantallas. Sin este requerimiento, cada cambio de color es un evolutivo.

## Requerimientos de arquitectura

| ID | Concepto | Descripción |
| --- | --- | --- |
| RARQ.1 **React** | Sin servicios residentes | La aplicación de las pantallas se entregará como archivos que el navegador del equipo abre directamente. No quedará ningún servicio del adjudicatario en ejecución para que la pantalla funcione. |
| RARQ.2 | Herramienta de gestión | La herramienta de gestión tendrá acceso por usuario y perfil y registro de quién modificó cada contenido. Ninguna credencial de acceso a sistemas de terceros estará presente en el navegador del operador. |

**Por qué RARQ.1.** En otras tecnologías el servidor forma parte del suministro y se inventaría. En React es fácil que el proveedor deje uno encendido «porque así se desarrolla», y esa pieza entra en el inventario, el mantenimiento y las certificaciones de los veinte años siguientes sin haber sido valorada.

## Mantenimiento y gestión tecnológica

| ID | Concepto | Descripción |
| --- | --- | --- |
| RMOGT.1 | Fuentes | Se entregará el código fuente completo, con la propiedad intelectual del órgano de contratación, en el repositorio que este indique. |
| RMOGT.2 **React** | Versiones exactas | Se entregará el fichero que fija la versión exacta de cada librería de terceros. Una relación aproximada no cumple este requerimiento. |
| RMOGT.3 **React** | Copia de las librerías | Se entregará copia de todas las librerías de terceros, de forma que el paquete pueda fabricarse sin acceso a internet. |
| RMOGT.4 | Licencias | Se entregará la relación de licencias de las librerías, con declaración de que ninguna impone obligaciones sobre los desarrollos propios. |
| RMOGT.5 **React** | Reconstrucción verificada | Antes de la recepción, personal del órgano de contratación fabricará el paquete siguiendo únicamente el documento de pasos y sin asistencia del adjudicatario. El resultado deberá coincidir con el instalado. |
| RMOGT.6 **React** | Funcionamiento continuado | La aplicación funcionará en continuo durante al menos 30 días sin reinicio, con la memoria ocupada estable. Se medirá en las pruebas de aceptación y constará en el acta. |
| RMOGT.7 **React** | Información temporal | Toda información con validez temporal se recalculará con el reloj del equipo, y no a partir del momento en que la aplicación se inició. |
| RMOGT.8 | Reinicio autónomo | Si la aplicación deja de responder, el equipo la reiniciará por sí mismo y mostrará el contenido de reserva mientras lo hace. |
| RMOGT.9 **React** | Registros | Los fallos de la aplicación se incorporarán a los registros del equipo, con los mismos niveles y el mismo mecanismo de recogida que el resto del sistema. No se considerará cumplido si solo son accesibles desde el propio navegador. |

**Por qué RMOGT.2, RMOGT.3 y RMOGT.5.** Las fuentes ya se piden en cualquier desarrollo. En React no bastan: el paquete se fabrica bajando de internet las librerías de terceros, que no están en el código. A los dos años una librería ya no está, o está en otra versión, y lo que sale deja de ser lo que se recibió. La reconstrucción hecha por personal propio, antes de firmar, es la única prueba de que eso no va a pasar.

**Por qué RMOGT.6, RMOGT.7 y RMOGT.9.** Un programa de equipo se reinicia con el equipo. Una aplicación React puede llevar once días sin volver a empezar, porque nadie la cierra: se come la memoria hasta el negro, el contador se queda en el minuto en que se abrió, y los fallos se escriben en un sitio al que solo se llega enchufando un teclado. Nada de eso se cubre con los requerimientos de la CPU.

## Gestión del proyecto y documentación

| ID | Concepto | Descripción |
| --- | --- | --- |
| RGP.1 **React** | Inventario de componentes | Se entregará la relación de todos los componentes visuales de la aplicación, indicando para cada uno qué muestra, dentro de cuál aparece, qué datos recibe y de qué sistema o servicio sale cada dato. Sustituye al diagrama de clases para esta parte del suministro. |
| RGP.2 | Diseño previo | El diseño de cada pantalla se aprobará por el órgano de contratación antes de su construcción, incluyendo los estados de los requerimientos RFUN.3 a RFUN.7. |
| RGP.3 | Cobertura del plan de pruebas | El plan de pruebas recorrerá la totalidad de la tabla de averías, con una prueba por cada situación y tipo de contenido, indicando el resultado esperado en pantalla. |
| RGP.4 **React** | Pruebas como condición | Las pruebas automáticas de ALC.3 se lanzarán en presencia del órgano de contratación como condición de recepción y deberán superarse todas. |
| RGP.5 | Informe de resultados | El resultado de las pruebas se entregará como informe legible sin herramientas adicionales, con cada prueba, su resultado y la fecha de ejecución. Se repetirá en cada entrega posterior sobre el mismo sistema. |

**Por qué RGP.1.** El pliego pide diagrama de clases porque en otras tecnologías las hay. En React no: pedirlas es recibir un documento de trámite. El inventario de componentes visuales es lo que ocupa ese sitio y es lo que necesita quien herede el mantenimiento.

**Por qué RGP.4.** En un desarrollo tradicional las pruebas se pasan una vez, sobre el equipo. En React se pueden pasar mil veces en un ordenador, sin el equipo, y son lo que permite que cada evolutivo no vuelva a ser una recepción entera.

## Lo que es de React, de un vistazo

Once requerimientos. El resto se escribiría igual para cualquier tecnología.

- **Se fabrica, no se instala.** `ALC.2`, `RMOGT.2`, `RMOGT.3`, `RMOGT.5`: el código fuente no basta porque las librerías de terceros se bajan de internet cada vez que se fabrica el paquete.
- **Nadie la cierra nunca.** `RFUN.6`, `RMOGT.6`, `RMOGT.7`, `RMOGT.9`: vive semanas en un navegador y se degrada sola.
- **No hay clases que dibujar.** `RGP.1`: el diagrama de siempre no existe; hay que pedir otra cosa.
- **No deja un servidor encendido.** `RARQ.1`: si se queda uno, entra en el inventario de veinte años.
- **Los valores no se recompilan.** `RFUN.8`: un color escrito en el código es un evolutivo por cada cambio.
- **Las pruebas se pueden repetir.** `ALC.3`, `RGP.4`: sin ellas, cada fase siguiente vuelve a pagar la recepción.

## Si solo entran cinco

De los once, estos cinco son los que hacen posible la licitación siguiente sin empezar de cero: `ALC.2` el entorno de construcción, `RMOGT.2` las versiones exactas, `RMOGT.5` la reconstrucción verificada, `RGP.1` el inventario de componentes y `RGP.4` las pruebas como condición de recepción.
