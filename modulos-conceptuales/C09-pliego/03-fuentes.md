# Las fuentes y los entregables

[← Página anterior](02-requerimientos.md) · [Siguiente página →](04-aceptacion.md)

![La caja que entrega el proveedor contiene la receta y la lista de la compra. Una flecha sale hacia una despensa que está en internet. Debajo, en rojo, lo que pasa a los dos años; en verde, lo que hay que pedir.](../img/la-entrega.svg)

- **Esto ya lo pedís, y bien.** Las herramientas necesarias con el código fuente, por ejemplo en una máquina virtual, con el entorno de desarrollo configurado, y el documento con los pasos para obtener el paquete de distribución.

- **Con React se puede cumplir al pie de la letra y no bastar.** Lo que recibes es la receta y la lista de la compra. La despensa está en internet: componentes hechos por otros que se bajan cada vez que se fabrica el paquete. En una aplicación React son cientos, y eso es lo normal.

- **Lo que pasa a los dos años.** Un componente ya no está donde estaba, o está en otra versión. Lo que sale deja de ser lo que te entregaron, y nadie puede explicar por qué, porque el proveedor cumplió el pliego.

- **Tres líneas que lo cierran.** El fichero donde queda anotada la versión exacta de cada componente. Una copia de los componentes guardada en TMB, para poder fabricar sin internet. Y la reconstrucción hecha por personal de TMB, en un equipo limpio, antes de firmar la recepción.

- **La última es la única que cierra el riesgo de verdad.** Y es una tarde.

- **Y la documentación.** Donde el pliego pide diagrama de clases y casos de uso, en React no hay clases que dibujar: recibirás un documento de trámite. Lo que ocupa ese sitio es el inventario de componentes: qué muestra cada uno, dentro de cuál aparece, qué datos recibe y de qué sistema sale cada dato.

**Tip de reunión.** «¿Podemos fabricar el paquete nosotros, hoy, aquí, con vuestro documento delante?» Si hace falta alguien del proveedor, la entrega no está completa, esté firmada o no.
