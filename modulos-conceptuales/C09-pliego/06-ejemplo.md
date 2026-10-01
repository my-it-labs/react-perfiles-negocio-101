# Pliego de ejemplo

[← Página anterior](05-garantia.md) · [Siguiente página →](../../modulos/M01-ecosistema-react/README.md)

Un supuesto teórico: una aplicación ficticia, pequeña, y el extracto de pliego que le correspondería. Mismo formato de tabla de tres columnas y mismas familias de identificadores de siempre; la numeración se ajusta al expediente real.

Sirve para dos cosas: recorrerlo entero sobre un caso que cabe en una página, y tenerlo delante el día de redactar uno de verdad.

No hay nada clausular aquí: ni precio, ni solvencia, ni plazos, ni penalizaciones.

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
| ALC.2 | Entorno de construcción | El suministro incluye el entorno para fabricar el paquete instalable y una copia de todos los componentes de terceros utilizados. |
| ALC.3 | Pruebas automáticas | El suministro incluye las pruebas automáticas de la aplicación y el documento para lanzarlas en un equipo sin preparación previa. |
| ALC.4 | Herramienta de gestión | El suministro incluye la herramienta con la que el personal propio programa los contenidos, con su propia formación y su propia aceptación. |

## Requerimientos funcionales

| ID | Concepto | Descripción |
| --- | --- | --- |
| RFUN.1 | Aplicación | El contenido de la pantalla será una aplicación web progresiva (React) responsive, que se adaptará a todas las combinaciones del anexo ALC.1. |
| RFUN.2 | Adaptación comprobable | El adjudicatario entregará una imagen de la aplicación en funcionamiento por cada combinación del anexo, para aprobación previa a las pruebas de aceptación. |
| RFUN.3 | Sin datos | Cuando el servicio de avisos responda sin avisos vigentes, la pantalla mostrará el texto aprobado en el diseño previo, y no una zona vacía. |
| RFUN.4 | Con error | Cuando el servicio de avisos no responda, responda con error o responda algo inesperado, se reintentará dos veces con intervalos de cinco segundos. Si ninguna tiene éxito, se mantendrá el último contenido válido descargado. |
| RFUN.5 | Dato mal formado | Si un aviso concreto llega con estructura o contenido inesperado, se ignorará ese aviso y se mostrarán los correctos. |
| RFUN.6 | Recuperación | Al restablecerse la comunicación, la aplicación volverá a solicitar toda la información que esté mostrando, sin esperar al siguiente ciclo de refresco. |
| RFUN.7 | Arranque | Mientras el equipo arranca, y en caso de que la aplicación no llegue a arrancar, la pantalla mostrará el contenido de reserva almacenado localmente. |
| RFUN.8 | Sin valores fijos | Textos, colores, medidas, posiciones, duraciones y direcciones de origen de datos serán configurables sin volver a fabricar el paquete. |
| RFUN.9 | Accesibilidad | Contrastes, tamaños de letra y tiempos de permanencia cumplirán las pautas aplicables a contenido de lectura a distancia, verificados sobre el anexo ALC.1. |

## Requerimientos de arquitectura

| ID | Concepto | Descripción |
| --- | --- | --- |
| RARQ.1 | Sin servicios residentes | La aplicación de las pantallas se entregará como archivos que el navegador del equipo abre directamente. No quedará ningún servicio del adjudicatario en ejecución para que la pantalla funcione. |
| RARQ.2 | Herramienta de gestión | La herramienta de gestión tendrá acceso por usuario y perfil y registro de quién modificó cada contenido. Ninguna credencial de acceso a sistemas de terceros estará presente en el navegador del operador. |

## Mantenimiento y gestión tecnológica

| ID | Concepto | Descripción |
| --- | --- | --- |
| RMOGT.1 | Fuentes | Se entregará el código fuente completo, con la propiedad intelectual del órgano de contratación, en el repositorio que este indique. |
| RMOGT.2 | Versiones exactas | Se entregará el fichero que fija la versión exacta de cada componente de terceros. Una relación aproximada no cumple este requerimiento. |
| RMOGT.3 | Copia de componentes | Se entregará copia de todos los componentes de terceros, de forma que el paquete pueda fabricarse sin acceso a internet. |
| RMOGT.4 | Licencias | Se entregará la relación de licencias de los componentes, con declaración de que ninguna impone obligaciones sobre los desarrollos propios. |
| RMOGT.5 | Reconstrucción verificada | Antes de la recepción, personal del órgano de contratación fabricará el paquete siguiendo únicamente el documento de pasos y sin asistencia del adjudicatario. El resultado deberá coincidir con el instalado. |
| RMOGT.6 | Funcionamiento continuado | La aplicación funcionará en continuo durante al menos 30 días sin reinicio, con la memoria ocupada estable. Se medirá en las pruebas de aceptación y constará en el acta. |
| RMOGT.7 | Información temporal | Toda información con validez temporal se recalculará con el reloj del equipo, y no a partir del momento en que la aplicación se inició. |
| RMOGT.8 | Reinicio autónomo | Si la aplicación deja de responder, el equipo la reiniciará por sí mismo y mostrará el contenido de reserva mientras lo hace. |
| RMOGT.9 | Registros | Los fallos de la aplicación se incorporarán a los registros del equipo, con los mismos niveles y el mismo mecanismo de recogida que el resto del sistema. No se considerará cumplido si solo son accesibles desde el propio navegador. |

## Gestión del proyecto y documentación

| ID | Concepto | Descripción |
| --- | --- | --- |
| RGP.1 | Inventario de componentes | Se entregará la relación de todos los componentes visuales de la aplicación, indicando para cada uno qué muestra, dentro de cuál aparece, qué datos recibe y de qué sistema o servicio sale cada dato. Sustituye al diagrama de clases para esta parte del suministro. |
| RGP.2 | Diseño previo | El diseño de cada pantalla se aprobará por el órgano de contratación antes de su construcción, incluyendo los estados de los requerimientos RFUN.3 a RFUN.7. |
| RGP.3 | Cobertura del plan de pruebas | El plan de pruebas recorrerá la totalidad de la tabla de averías, con una prueba por cada situación y tipo de contenido, indicando el resultado esperado en pantalla. |
| RGP.4 | Pruebas como condición | Las pruebas automáticas de ALC.3 se lanzarán en presencia del órgano de contratación como condición de recepción y deberán superarse todas. |
| RGP.5 | Informe de resultados | El resultado de las pruebas se entregará como informe legible sin herramientas adicionales, con cada prueba, su resultado y la fecha de ejecución. Se repetirá en cada entrega posterior sobre el mismo sistema. |

## Si solo entran cinco

De los veintisiete, estos cinco son los que hacen posible la licitación siguiente sin empezar de cero: `ALC.1` el anexo de pantallas, `ALC.2` el entorno de construcción, `RMOGT.2` las versiones exactas, `RMOGT.5` la reconstrucción verificada y `RGP.1` el inventario de componentes.
