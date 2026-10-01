# Requisitos para pegar en un pliego

[← Página anterior](05-la-recepcion.md) · [Siguiente página →](../../modulos/M01-ecosistema-react/README.md)

Veintidós requisitos para la parte de aplicación de un pliego de sistema. No sustituyen a nada de lo que ya tienes: se colocan al lado de los requisitos de plataforma, de comunicaciones y de instalación, y cubren el hueco que deja la frase de la página 1.

Los identificadores van en neutro (`REQ.n`) para que los renumeres con la familia que uses en cada expediente. Nada de lo que hay aquí es clausular: ni precio, ni solvencia, ni plazos, ni penalizaciones.

## La aplicación

| ID | Concepto | Descripción |
| --- | --- | --- |
| REQ.1 | Inventario de pantallas | El pliego incorporará como anexo la relación de pantallas sobre las que funcionará la aplicación, indicando medida, resolución, orientación y número de unidades de cada combinación. |
| REQ.2 | Adaptación | La aplicación se adaptará a todas las combinaciones del anexo. El adjudicatario entregará una imagen de la aplicación en funcionamiento por cada combinación, para su aprobación previa a las pruebas de aceptación. |
| REQ.3 | Diseño de pantallas | El diseño de cada pantalla se aprobará por la casa antes de su construcción. La aprobación incluirá el estado normal y los estados sin datos previstos en el apartado de averías. |
| REQ.4 | Sin valores fijos | Ningún texto, color, medida, posición, duración ni dirección de origen de datos estará fijado en el código. Todo será configurable sin reconstruir la aplicación. |
| REQ.5 | Sin servicio propio | La aplicación de las pantallas se entregará como archivos que el navegador del equipo abre directamente, sin ningún servicio del proveedor que deba permanecer en ejecución para que la pantalla funcione. |
| REQ.6 | Herramienta de gestión | La herramienta de gestión de contenidos tendrá acceso por usuario y perfil. Ninguna credencial de acceso a sistemas de terceros estará presente en el navegador del operador. |
| REQ.7 | Accesibilidad | Contrastes, tamaños de letra y tiempos de permanencia de cada pantalla cumplirán las pautas de accesibilidad aplicables a contenido de lectura a distancia, y se verificarán sobre el inventario del anexo. |

## Entrega y continuidad

| ID | Concepto | Descripción |
| --- | --- | --- |
| REQ.8 | Código fuente | Se entregará el código fuente completo de la aplicación, con la propiedad intelectual de la casa, en el repositorio que la casa indique. |
| REQ.9 | Versiones de terceros | Se entregará el archivo que fija la versión exacta de cada componente de terceros utilizado. Una relación aproximada de componentes no cumple este requisito. |
| REQ.10 | Copia de los componentes | Se entregará una copia de todos los componentes de terceros necesarios para construir la aplicación, de forma que el proceso pueda completarse sin acceso a internet. |
| REQ.11 | Licencias | Se entregará la relación de licencias de los componentes de terceros, con declaración expresa de que ninguna impone obligaciones sobre los desarrollos propios de la casa. |
| REQ.12 | Pasos de construcción | Se entregará el documento que permita obtener, partiendo del código fuente, el paquete instalable, en un ordenador sin preparación previa. |
| REQ.13 | Reconstrucción verificada | Antes de la recepción, personal de la casa construirá el paquete instalable siguiendo únicamente el documento anterior y sin asistencia del adjudicatario. El paquete obtenido deberá coincidir con el instalado. |
| REQ.14 | Inventario de piezas visuales | Se entregará la relación de todas las piezas visuales de la aplicación indicando, para cada una: qué muestra, dentro de qué otra pieza aparece, qué datos recibe y de qué sistema o servicio procede cada dato. |

## Funcionamiento continuado

| ID | Concepto | Descripción |
| --- | --- | --- |
| REQ.15 | Días seguidos | La aplicación funcionará de forma continuada durante al menos 30 días sin reinicio, manteniendo estable la memoria ocupada. Se medirá en las pruebas de aceptación y el resultado constará en el acta. |
| REQ.16 | Información temporal | Toda información con validez temporal se recalculará con el reloj del equipo, y no a partir del momento en que la aplicación se inició. |
| REQ.17 | Recuperación del dato | Al restablecerse una comunicación interrumpida, la aplicación volverá a solicitar toda la información que esté mostrando, sin esperar al siguiente ciclo de refresco. |
| REQ.18 | Reinicio autónomo | Si la aplicación deja de responder, el equipo la reiniciará por sí mismo y mostrará el contenido de reserva mientras lo hace. |
| REQ.19 | Registro de fallos | Los fallos de la aplicación se incorporarán a los registros del equipo, con los mismos niveles y el mismo mecanismo de recogida que el resto del sistema. No se considerará cumplido si solo quedan accesibles desde el propio navegador. |

## Pruebas y recepción

| ID | Concepto | Descripción |
| --- | --- | --- |
| REQ.20 | Cobertura del plan de pruebas | El plan de pruebas recorrerá la totalidad de la tabla de averías del pliego, con una prueba por cada situación y tipo de contenido, indicando el resultado esperado en pantalla. |
| REQ.21 | Pruebas automáticas | Se entregarán las pruebas automáticas de la aplicación, en el mismo repositorio que el código fuente, junto con el documento que permita lanzarlas en un ordenador sin preparación previa. Se lanzarán en presencia de la casa como condición de recepción y deberán superarse todas. |
| REQ.22 | Informe de resultados | El resultado de las pruebas se entregará como informe legible sin herramientas adicionales, indicando cada prueba, su resultado y la fecha de ejecución. Se repetirá en cada entrega posterior sobre el mismo sistema. |

## Cómo cierra esto la licitación siguiente

La vida de un sistema no es un contrato. Es el contrato nuevo, la fase de cambios, la fase de mejoras, la ampliación, y a veces un proveedor distinto del que lo construyó.

De los veintidós requisitos, seis son los que hacen posible esa segunda licitación sin empezar de cero: el inventario de pantallas, el archivo de versiones, la copia de los componentes, la reconstrucción verificada, el inventario de piezas visuales y las pruebas automáticas.

Si en el pliego de hoy solo entran seis, que sean esos.
