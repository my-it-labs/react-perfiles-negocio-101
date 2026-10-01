# Cómo se comprueba que está bien

[← Página anterior](05-dias-seguidos.md) · [Siguiente página →](07-requisitos.md)

![La misma pantalla en cuatro casos de prueba: con datos muestra tres avisos, sin datos muestra «No hay avisos», con error muestra «No se ha podido cargar», y con un dato mal formado muestra los dos correctos y descarta el tercero.](../img/pruebas-cuatro-casos.svg)

- **El marco ya lo tenéis.** Un plan de pruebas que redacta el adjudicatario y aprueba la casa, pruebas en sus instalaciones, pruebas en destino, y un acta con la lista, el resultado de cada prueba y el cuadro de deficiencias.

- **Lo que falta es qué entra en esa lista por la parte de la pantalla.** Son cuatro familias, y las cuatro se escriben sin saber programar.

- **Uno: con el dato normal.** Una imagen de referencia por cada medida y orientación del inventario, aprobada por la casa antes de las pruebas, no durante.

- **Dos: sin el dato.** Aquí hay un atajo enorme. Vuestra tabla de averías ya tiene las situaciones escritas una por una: la lista de pruebas sale de ahí, casilla por casilla. No hay que inventar nada; hay que exigir que el plan recorra la tabla entera.

- **Tres: lo que aguanta.** La prueba de los días seguidos de la página anterior.

- **Cuatro: lo que se puede volver a pasar.** Esta es la que casi nunca se pide, y es la que más vale.

- **Automatizar, en claro.** Un programa aparte abre la aplicación, le entrega datos preparados —la lista normal, la lista vacía, una respuesta con error, un elemento mal formado— y comprueba que en la pantalla sale lo que el pliego dijo. Tarda segundos. No necesita el equipo real, ni el tren, ni esperar a que la avería ocurra.

- **Por qué te interesa a ti más que al proveedor.** Cuando llegue la fase de cambios, la de mejoras, la ampliación, o un proveedor distinto del que lo construyó, esas pruebas son lo único que te dice en una tarde si lo nuevo rompió lo que ya funcionaba. Sin ellas, cada fase vuelve a pagar la recepción entera.

Se pide con las mismas palabras que el código fuente, porque es lo mismo:

> Se entregarán las pruebas automáticas de la aplicación, en el mismo repositorio que el código fuente, junto con el documento que permita lanzarlas en un ordenador sin preparación previa. Se lanzarán en presencia de la casa como condición de recepción y deberán superarse todas.

## Señales de alerta en un plan de pruebas

- No hay ninguna prueba en la que el dato no llegue. Solo se prueba el día bueno.
- Todas las capturas son de la misma pantalla, del mismo tamaño y con el mismo contenido.
- Pone «se verificará manualmente» y no hay lista de qué se verifica.
- Las pruebas automáticas existen, pero solo se pueden lanzar en el ordenador de una persona del proveedor.

**Tip.** Las cuatro se corrigen antes de firmar. Ninguna se corrige después.
