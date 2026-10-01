# El alcance y el listado de suministros

[← Página anterior](README.md) · [Siguiente página →](02-requerimientos.md)

![Listado resumen de suministros y servicios con las líneas habituales en gris y tres líneas añadidas en verde: entorno de construcción, pruebas automáticas y anexo de pantallas.](../img/alcance-listado.svg)

- **El listado manda.** Lo que no aparece en el resumen de suministros y servicios no se entrega, y después no hay dónde reclamarlo.

- **Con React, el software no es lo único que hay que listar.** El paquete que se instala se fabrica, y para volver a fabricarlo hacen falta cosas que no son el código.

- **Tres líneas que conviene añadir.** El entorno de construcción con los componentes de terceros. Las pruebas automáticas y el documento para lanzarlas. Y el anexo de pantallas.

- **El anexo de pantallas es alcance, no detalle.** «Responsive» significa que se adapta a tamaños distintos, y los tamaños de un sistema instalado son los que hay: medidas, resoluciones, orientaciones y unidades. Sin esa lista no se puede comprobar, y cada parte entiende una cosa distinta hasta el día de la recepción.

- **Las condiciones técnicas mínimas también se escriben.** Si el apartado existe y la aplicación no tiene las suyas, se dan por cumplidas todas.

**Tip.** Antes de publicar, leer el listado y hacerse una sola pregunta: con esto en la mano, ¿puede TMB volver a fabricar la aplicación dentro de tres años sin este proveedor? Si la respuesta no es un sí claro, falta una línea.
