# Cómo se comprueba que está bien

[← Página anterior](04-dias-seguidos.md) · [Siguiente página →](06-requisitos.md)

El marco ya lo tienen los pliegos: un plan de pruebas que redacta el adjudicatario y aprueba la casa, unas pruebas en las instalaciones del proveedor, otras en destino, y un acta con la lista de pruebas, el resultado de cada una y el cuadro de deficiencias a corregir.

Lo que no suele estar es qué entra en esa lista por la parte de la aplicación. Son cuatro familias, y las cuatro se escriben sin saber programar.

## Las cuatro familias

**1. Lo que se ve con el dato normal.** Una imagen de referencia por cada medida y orientación del inventario de pantallas. Aprobadas por la casa antes de las pruebas, no durante.

**2. Lo que se ve sin el dato.** Aquí hay un atajo enorme: tu tabla de averías ya tiene las situaciones escritas una por una. Si la tabla cruza diez averías con cinco tipos de contenido, la lista de pruebas sale de ahí directamente, casilla por casilla. No hay que inventar nada; hay que exigir que el plan de pruebas recorra la tabla entera y que ninguna casilla se quede sin probar.

**3. Lo que aguanta.** La prueba de los días seguidos de la página anterior.

**4. Lo que se puede volver a pasar.** Esta es la importante, y es la que casi nunca se pide.

## Qué significa automatizar, en claro

Un programa aparte abre la aplicación, le entrega datos preparados —la lista normal, la lista vacía, una respuesta con error, un elemento mal formado— y comprueba que en la pantalla aparece exactamente lo que el pliego dijo que tenía que aparecer en cada caso.

Tarda segundos. No necesita el equipo real, ni el tren, ni la estación, ni esperar a que una avería ocurra de verdad. Y se puede lanzar mil veces.

Por eso no es un asunto del proveedor: es tuyo. Cuando llegue la fase siguiente del sistema —los cambios, las mejoras, la ampliación, o un proveedor distinto al que hizo el original— esas pruebas son lo único que te dice en una tarde si lo nuevo rompió lo que ya funcionaba. Sin ellas, cada fase vuelve a pagar la recepción entera y cada fase vuelve a descubrir los mismos fallos.

Se pide con las mismas palabras que el código fuente, porque es lo mismo:

> Se entregarán las pruebas automáticas de la aplicación, en el mismo repositorio que el código fuente, junto con el documento que permita lanzarlas en un ordenador limpio. Como condición de recepción, se lanzarán en presencia de la casa y deberán superarse todas.

> El resultado de las pruebas se entregará como un informe legible sin herramientas adicionales, indicando cada prueba, su resultado y la fecha de ejecución.

Ese informe es el mismo tipo de documento que el parte diario de estado del sistema. Pídelo con ese formato y lo entenderá todo el mundo.

## Señales de alerta en un plan de pruebas

Cuatro cosas que se ven a simple vista, antes de aprobarlo:

- No hay ninguna prueba en la que el dato no llegue. Solo se prueba el día bueno.
- Todas las capturas son de la misma pantalla, del mismo tamaño y con el mismo contenido.
- Pone «se verificará manualmente» y no hay lista de qué se verifica.
- Las pruebas automáticas existen, pero solo se pueden lanzar en el ordenador de una persona del proveedor.

Las cuatro se corrigen antes de firmar, y ninguna se corrige después.
