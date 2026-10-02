# Qué tienen que entregar

[← Página anterior](01-el-pliego.md) · [Siguiente página →](03-aceptacion.md)

El pliego pide el código fuente, el entorno y un documento de pasos. Con React eso se puede cumplir al pie de la letra y no bastar. Esta página dice qué tiene que haber dentro de cada cosa. Las filas están en el [ejemplo](05-ejemplo.md), en el ámbito Entorno.

![Lo que se entrega es el código fuente y una lista de nombres de librerías. Las librerías están en internet y se bajan cada vez que se fabrica el paquete.](../img/la-entrega.svg)

## Entorno de construcción

Una máquina del órgano de contratación, que puede ser virtual, limpia, y capaz de fabricar el paquete sin acceso a internet.

Lleva las herramientas para fabricar, la copia de las librerías y el código. No replica la arquitectura de preproducción ni la de producción. Esas son los sitios donde el paquete se instala, y ya las cubre el pliego de implantación. Pedir tres máquinas de construcción es pedir tres veces la misma.

## Documento de pasos

Indica tres cosas, y con eso se puede seguir sin el proveedor:

- de qué se parte,
- en qué orden,
- cuál es el resultado, que es el paquete instalable.

## Código y librerías

- El código fuente, en el repositorio que indique el órgano de contratación.
- El fichero con el nombre y la versión exacta de cada librería de terceros. Una relación aproximada no vale.
- Una copia de esas librerías. En una aplicación React son muchas, hechas por otros, y no viajan dentro del código: se bajan de internet cada vez que se fabrica. A los dos años una puede no estar, o estar en otra versión, y lo que sale deja de ser lo que se recibió.
- La licencia de cada una, y la declaración de que ninguna obliga a publicar lo que se construye encima.

## Piezas de pantalla

Donde el pliego pide un diagrama de clases, en React no hay clases que dibujar y el documento llega vacío. Lo que ocupa ese sitio es la relación de piezas de pantalla: qué muestra cada una, dentro de cuál aparece, qué datos recibe y de qué sistema sale cada dato.

## El paquete y el fichero de aspecto

Del paquete instalable bastan dos cosas.

El **fichero de aspecto** es el que dice cómo se ve cada pieza: colores, tamaños y posiciones. Viaja dentro del paquete. Cambiarlo obliga a fabricar otra vez.

Lo que se quiere poder cambiar sin fabricar —un texto, un color, una duración, la dirección de un dato— va en un **fichero de configuración**, al lado de la aplicación, que se modifica y se despliega solo. Si eso está escrito dentro del fichero de aspecto generado, cada cambio es un evolutivo.

## Para poder fabricarlo dentro de tres años

Hace falta todo lo anterior, y una comprobación: antes de firmar la recepción, personal propio fabrica el paquete en esa máquina, con el documento de pasos delante y sin el proveedor. El resultado tiene que coincidir con el instalado. Es una tarde, y es la única prueba de que la entrega sirve.
