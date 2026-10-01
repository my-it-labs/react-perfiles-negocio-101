# Una frase no es un requisito

[← Página anterior](README.md) · [Siguiente página →](02-dos-encargos.md)

En los pliegos de sistemas con pantallas aparece casi siempre una frase parecida a esta:

> El contenido que se mostrará en la pantalla será una aplicación web progresiva (React) diseñada de forma responsive para que se auto-adapte a diferentes tamaños de pantalla.

Está bien escrita y es correcta. El problema es lo que tiene al lado.

En el mismo documento, el equipo sobre el que corre esa aplicación lleva decenas de requisitos: el arranque por debajo de un tiempo dado, aguantar un corte de alimentación sin quedar inservible, recuperarse sin que vaya nadie, registros con sus niveles, dónde se guarda el código, un informe diario del estado. Todo eso es comprobable. Alguien puede ir, cortar la corriente y mirar el reloj.

La aplicación —lo único que el viajero ve— cabe en una frase.

## Qué queda sin decidir ahí dentro

- Quién dibuja las pantallas, y cuándo se aprueban.
- Qué se ve cuando el dato no llega, llega tarde o llega mal.
- Qué se recibe al terminar, y si con eso se puede reconstruir la aplicación sin el proveedor.
- Cómo se comprueba que está bien antes de firmar la recepción.
- Qué pasa en la licitación siguiente del mismo sistema.

Ninguna de esas cinco preguntas es técnica. Las cinco son funcionales, y las cinco se contestan escribiendo tres o cuatro líneas más.

## Un detalle que conviene no dar por hecho

«Responsive» significa que la misma aplicación se adapta a pantallas de distinto tamaño. En una web eso se entiende: el teléfono y el ordenador. En un sistema de pantallas instaladas, los tamaños son los que hay en el inventario, y son finitos.

Así que ese requisito no se puede comprobar hasta que exista la lista: qué medidas, qué orientaciones y cuántas unidades de cada una. Con la lista, «responsive» es una prueba. Sin la lista, es una palabra, y el proveedor entregará lo que haya probado en su monitor.

**Tip.** Pide el inventario de pantallas como anexo del pliego, aunque sea aproximado, y exige una imagen de la aplicación por cada combinación de medida y orientación. Es el requisito más barato de escribir y el que más discusiones ahorra en la recepción.
