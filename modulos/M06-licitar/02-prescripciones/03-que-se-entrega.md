# Qué se entrega

[← Página anterior](02-dato-y-desenlaces.md) · [Siguiente página →](../03-cierre/01-obligatorio-y-puntuable.md)

«Aplicación terminada» no se puede señalar. La entrega se define como cosas que una tercera persona arranca y lee, en una máquina que no es la del proveedor.

## El producto que se abre

- El repositorio, con las dependencias declaradas. En una máquina limpia, con el Node que el propio proyecto pide, la instalación y el arranque son los comandos escritos en el proyecto. Si solo arranca en el portátil de quien lo desarrolló, no está entregado.
- Los entornos separados: prueba contra el sistema de datos de prueba, y el procedimiento para construir lo que se publica. La demo del curso sirve Next ya construido y la SPA en caliente. El pliego dice cuál de las dos cosas es la entrega de producción y cuál es solo la forma de trabajar.
- Una página corta, en el repositorio, que diga dónde nace el HTML de cada ruta pública, dónde vive el estado del panel y qué fichero habla con el sistema del dato. No es un diagrama de venta. Es el mapa para el checklist de arquitectura.

## El cambio que demuestra que hay piezas

Se pide una prueba de mantenimiento, hecha en la aceptación o descrita con el fichero exacto: cambiar el texto de un estado de servicio («retraso leve» pasa a «demora») y verlo en el listado y en la ficha. Si el cambio está en un solo sitio, las piezas existen. Si hay que perseguir el texto en varias pantallas, el pliego de «componentes» no se cumplió, aunque el marco sea React.

## Lo que acompaña y lo que no sustituye

Acompaña el acceso al entorno de prueba y la lista de cuentas con las que se comprueba la sesión. Acompaña la tabla de desenlaces rellena con las frases definitivas. No sustituye a nada de eso una presentación, una captura a pantalla completa ni un vídeo. La aceptación recorre las mismas filas que el checklist del módulo de calidad: arquitectura, rendimiento de la primera vista, interfaz, acceso y la superficie correcta. Una fila que no se puede señalar en la entrega se anota como no cumplida.

La propiedad del código, el depósito en el repositorio de la casa y la garantía son cláusulas. El pliego técnico se limita a decir que, el día de la entrega, la casa puede construir y arrancar el producto sin el proveedor delante. Si eso no ocurre, la cláusula de propiedad todavía no se ha materializado.
