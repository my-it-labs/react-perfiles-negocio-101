# Ejemplo: los mínimos

[← Página anterior](04-garantia.md) · [Siguiente página →](../../modulos/M01-ecosistema-react/README.md)

Un supuesto. **AVISOS** no existe: son pantallas en dependencias que muestran los avisos internos vigentes y el estado del servicio. Las mira quien pasa, nadie se identifica, y las alimenta una herramienta con usuario. Los datos salen de dos servicios internos. Corre en el navegador de una CPU por dependencia, encendida en continuo. Son 60 unidades, dos medidas, una en vertical.

Las filas marcadas **React** son el mínimo de esta tecnología, y no hay una segunda lista de recomendados. El resto se escribiría igual en cualquier proyecto: está aquí para que el caso se pueda leer entero. La columna Ámbito dice de qué bloque sale cada fila: Entorno, Pruebas, Anexo o Pantalla. La numeración se ajusta al expediente.

No hay nada clausular: ni precio, ni solvencia, ni plazos, ni penalizaciones.

## Alcance

| ID | Ámbito | Concepto | Descripción |
| --- | --- | --- | --- |
| ALC.1 | Anexo | Anexo de pantallas | Forma parte del alcance el anexo con la relación de pantallas: medida, resolución, orientación, ubicación, número de unidades de cada combinación, y el dibujo funcional de cada pantalla. |
| ALC.2 **React** | Entorno | Entorno de construcción | El suministro incluye un entorno de construcción en instalaciones del órgano de contratación: una máquina, que puede ser virtual, capaz de fabricar el paquete, con la copia de las librerías de terceros. Esa máquina fabrica el paquete. No sustituye a los entornos de preproducción o de producción, que son donde el paquete se instala. |
| ALC.3 **React** | Pruebas | Pruebas automáticas | El suministro incluye las pruebas automáticas de la aplicación, unitarias y de extremo a extremo, y el documento para lanzarlas en un equipo sin preparación previa. |
| ALC.4 | | Herramienta de gestión | El suministro incluye la herramienta con la que el personal propio programa los contenidos, con su propia formación y su propia aceptación. |

## Requerimientos de la aplicación

| ID | Ámbito | Concepto | Descripción |
| --- | --- | --- | --- |
| RFUN.1 **React** | Anexo | Aplicación | El contenido de la pantalla será una aplicación web progresiva (React) responsive, que se adaptará a todas las combinaciones del anexo ALC.1. Una medida, resolución u orientación que no figure en el anexo es un cambio de alcance. |
| RFUN.2 | Anexo | Adaptación comprobable | El adjudicatario entregará una imagen de la aplicación en funcionamiento por cada combinación del anexo, para aprobación previa a las pruebas de aceptación. |
| RFUN.3 | | Sin datos | Cuando el servicio de avisos responda sin avisos vigentes, la pantalla mostrará el texto aprobado en el diseño previo, y no una zona vacía. |
| RFUN.4 | | Con error | Cuando el servicio de avisos no responda, responda con error o responda algo inesperado, se reintentará dos veces con intervalos de cinco segundos. Si ninguna tiene éxito, se mantendrá el último contenido válido descargado. |
| RFUN.5 | | Dato mal formado | Si un aviso concreto llega con estructura o contenido inesperado, se ignorará ese aviso y se mostrarán los correctos. |
| RFUN.6 **React** | Pantalla | Recuperación | Al restablecerse la comunicación, la aplicación volverá a solicitar toda la información que esté mostrando, sin esperar al siguiente ciclo de refresco. |
| RFUN.7 | | Arranque | Mientras el equipo arranca, y en caso de que la aplicación no llegue a arrancar, la pantalla mostrará el contenido de reserva almacenado localmente. |
| RFUN.8 **React** | Pantalla | Fichero de configuración | Textos, colores, medidas, posiciones, duraciones y direcciones de origen de datos estarán en un fichero de configuración, separado del paquete instalable, modificable y desplegable sin volver a fabricar el paquete. No cumple dejarlos en el código ni en el fichero de aspecto generado con el paquete. |
| RFUN.9 | | Accesibilidad | Contrastes, tamaños de letra y tiempos de permanencia cumplirán las pautas aplicables a contenido de lectura a distancia, verificados sobre el anexo ALC.1. |
| RARQ.1 **React** | Pantalla | Sin programas residentes | La pantalla funcionará abriendo los ficheros en el navegador del equipo. No quedará ningún programa del adjudicatario en ejecución para que se vea. |
| RARQ.2 | | Herramienta de gestión | La herramienta de gestión tendrá acceso por usuario y perfil, y registro de quién modificó cada contenido. Ninguna credencial de acceso a sistemas de terceros estará presente en el navegador del operador. |

## Entregables

| ID | Ámbito | Concepto | Descripción |
| --- | --- | --- | --- |
| RMOGT.1 | Entorno | Fuentes | Se entregará el código fuente completo, con la propiedad intelectual del órgano de contratación, en el repositorio que este indique. |
| RMOGT.2 **React** | Entorno | Versiones exactas | Se entregará el fichero que fija la versión exacta de cada librería de terceros. Una relación aproximada no cumple este requerimiento. |
| RMOGT.3 **React** | Entorno | Copia de las librerías | Se entregará copia de todas las librerías de terceros, de forma que el paquete pueda fabricarse sin acceso a internet. |
| RMOGT.4 | Entorno | Licencias | Se entregará la relación de licencias de las librerías, con declaración de que ninguna impone obligaciones sobre los desarrollos propios. |
| RMOGT.5 **React** | Entorno | Reconstrucción verificada | Antes de la recepción, personal del órgano de contratación fabricará el paquete en el entorno de ALC.2, siguiendo únicamente el documento de pasos y sin asistencia del adjudicatario. El resultado deberá coincidir con el instalado. |
| RMOGT.6 **React** | Pantalla | Funcionamiento continuado | La aplicación funcionará en continuo durante al menos 30 días sin reinicio, con la memoria ocupada estable y sin degradación visible del contenido. Se medirá en las pruebas de aceptación y constará en el acta. |
| RMOGT.7 **React** | Pantalla | Información temporal | Toda información con validez temporal se recalculará con el reloj del equipo, y no a partir del momento en que la aplicación se inició. |
| RMOGT.8 | | Reinicio autónomo | Si la aplicación deja de responder, el equipo la reiniciará por sí mismo y mostrará el contenido de reserva mientras lo hace. |
| RMOGT.9 **React** | Pantalla | Registros | Los fallos de la aplicación se incorporarán a los registros del equipo, con los mismos niveles y el mismo mecanismo de recogida y envío a los sistemas centrales que el resto del sistema. No se considerará cumplido si solo son accesibles desde el propio navegador. |
| RMOGT.10 **React** | Entorno | Documento de pasos | El documento para fabricar el paquete indicará de qué se parte, el orden de los pasos y el resultado esperado. |
| RGP.1 **React** | Entorno | Inventario de piezas | Se entregará la relación de las piezas de pantalla, indicando para cada una qué muestra, dentro de cuál aparece, qué datos recibe y de qué sistema sale cada dato. Sustituye al diagrama de clases para esta parte del suministro. |

## Aceptación

| ID | Ámbito | Concepto | Descripción |
| --- | --- | --- | --- |
| RGP.2 | | Diseño previo | Si el diseño funcional no está cerrado al publicar el pliego, el adjudicatario lo cerrará y el órgano de contratación lo aprobará antes de construir. Las pruebas cubrirán el diseño aprobado, incluidos los estados de RFUN.3 a RFUN.7. |
| RGP.3 **React** | Pruebas | Cuatro situaciones | Para cada dato que la aplicación muestre, el plan de pruebas cubrirá cuatro situaciones: con dato, sin dato, con error y con un dato mal formado, indicando el resultado esperado en pantalla. Si el pliego incluye una tabla de averías, el plan la recorrerá entera. |
| RGP.4 **React** | Pruebas | Pruebas como condición | Las pruebas automáticas de ALC.3 se lanzarán en un entorno del órgano de contratación y en su presencia, como condición de recepción, y deberán superarse todas. |
| RGP.5 | Pruebas | Informe de resultados | El resultado se entregará como informe legible sin herramientas adicionales, con cada prueba, su resultado y la fecha. Se repetirá en cada entrega posterior sobre el mismo sistema. |
| RGP.6 **React** | Pruebas | Configuración sin fabricar | Como condición de recepción se modificará un valor del fichero de configuración de RFUN.8, sin fabricar de nuevo el paquete, y la pantalla mostrará el valor modificado. |

## Por qué estas y no otras

- **Entorno.** El código fuente no trae las librerías. Sin la máquina, la copia, las versiones, el documento de pasos y una fabricación hecha en casa, dentro de dos años no se puede reconstruir.
- **Pruebas.** Las cuatro situaciones cubren el día bueno y el día malo sin necesidad de tener el funcional cerrado. Unitarias y de extremo a extremo, lanzadas en entorno propio. No se pide una metodología de desarrollo: se pide que las pruebas existan y se superen.
- **Anexo.** «Responsive» solo se puede comprobar contra una lista. Fuera de la lista, es otro alcance.
- **Fichero de configuración.** El fichero de aspecto viaja dentro del paquete. Lo que se quiere cambiar sin fabricar tiene que vivir fuera.
- **Sin programas residentes.** Si queda uno encendido, entra en el mantenimiento de toda la vida del contrato sin estar en la oferta.
- **Semanas encendida, reloj y registros.** Nadie cierra la aplicación. La memoria crece, el contador se para, y el fallo no llega a los registros que ya se envían a central si no se pide.
