# Lo que hay que llevarse

[← Página anterior](02-dos-encargos.md) · [Siguiente página →](04-dias-seguidos.md)

Esta parte los pliegos la suelen traer ya escrita, y bien escrita:

> El adjudicatario entregará el código fuente de todos los desarrollos, así como los entornos para programar y compilar, y un documento que explique los pasos para obtener, partiendo del código fuente, el paquete de distribución.

El proveedor puede cumplir esas tres cosas al pie de la letra y dejarte sin poder reconstruir nada. No por mala fe: por cómo se construyen estas aplicaciones.

## Por qué el código fuente no es suficiente

Una aplicación de este tipo no se escribe entera. Se monta encima de cientos de piezas hechas por otros —un calendario, un reproductor, una forma de dibujar gráficos— que no viven en el proyecto. Viven en internet, y se descargan en el momento de construir el paquete.

El código fuente que recibes no las lleva dentro. Lleva una lista con sus nombres.

Dentro de dos años, cuando haya que tocar una pantalla, esa lista se vuelve a descargar. Si alguna pieza ya no está en su sitio, o está en una versión distinta, lo que sale del taller no es lo que te entregaron. Puede fallar, puede verse distinto, o puede dejar de arrancar. Y nadie podrá decirte por qué, porque el proveedor original entregó exactamente lo que el pliego pedía.

## Lo que hay que añadir al requisito

- **El archivo donde queda anotada la versión exacta de cada pieza de terceros**, no la lista aproximada. Es un archivo que el taller genera solo; el proveedor únicamente tiene que no borrarlo al entregar.
- **Una copia de esas piezas guardada en casa.** No la dirección de internet de donde se bajan: las piezas.
- **La licencia de cada pieza**, y la declaración de que ninguna obliga a publicar lo que se construye encima.
- **La prueba de que se puede reconstruir.** Alguien de la casa, en un ordenador limpio, siguiendo solo el documento de pasos, sin llamar al proveedor, obtiene el mismo paquete que está instalado. Esto se hace **antes** de firmar la recepción, no cuando hace falta.

Ese último punto es el único que de verdad cierra el riesgo, y es una tarde de trabajo.

## El documento que te van a entregar vacío

Los pliegos piden, en el apartado de documentación, los diagramas de siempre: protocolos, secuencia, estados, clases y casos de uso.

En estas aplicaciones no hay clases. Si lo pides así, recibirás un documento inventado para cumplir el trámite, o no lo recibirás.

Lo que ocupa ese sitio, y es lo que necesitas para mantener, es el inventario de las piezas de pantalla. Pídelo con estas palabras:

> Relación de todas las piezas visuales de la aplicación, indicando para cada una: qué muestra, dentro de qué otra pieza aparece, qué datos recibe y de qué sistema o servicio sale cada uno de esos datos.

Eso se puede leer sin programar, se puede comparar con el dibujo de la pantalla, y es exactamente la información que necesita el equipo que coja el relevo.

**Tip de reunión.** Una pregunta que ordena la conversación en treinta segundos: «¿podemos construir el paquete nosotros, hoy, aquí, con vuestro documento delante?». Si la respuesta es que hace falta alguien del equipo del proveedor, la entrega no está completa, aunque esté firmada.
