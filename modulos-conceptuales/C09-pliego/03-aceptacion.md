# Cómo se acepta

[← Página anterior](02-entregables.md) · [Siguiente página →](04-garantia.md)

El marco no cambia: un plan de pruebas que redacta el adjudicatario y aprueba el órgano de contratación, pruebas en origen, pruebas en destino, y un acta con la lista, el resultado y las deficiencias. Esta página dice qué entra en esa lista por la parte de la aplicación. Las filas están en el [ejemplo](05-ejemplo.md), en el ámbito Pruebas.

## Una frase en el pliego, cuatro situaciones

El diseño funcional muchas veces no está cerrado cuando se escribe el pliego. No se pegan cuatro pantallas. Se escribe una frase: para cada dato que la aplicación muestre, el plan cubre con dato, sin dato, con error y con un dato mal formado, y dice qué tiene que verse en cada caso.

![Las cuatro situaciones de la misma pantalla: con datos, sin datos, con error y con un dato mal formado, que se ignora.](../img/pruebas-cuatro-casos.svg)

Si al licitar ya existe una tabla de averías, el plan la recorre entera. Si no existe, el diseño se cierra y se aprueba antes de construir, y las pruebas cubren ese diseño.

## Qué más se comprueba el día de la recepción

- **Una imagen por cada combinación del anexo**, aprobada antes de las pruebas.
- **Una semana encendida**, como mínimo, sin reiniciar. Se mira que la memoria no crezca y que no haya un fallo visible: un contador parado o una pantalla en negro. El requerimiento pide 30 días; la semana es la prueba que cabe en el calendario de recepción.
- **Un cambio en el fichero de configuración**, sin fabricar otro paquete, y la pantalla muestra el valor nuevo.
- **Las pruebas automáticas, en un entorno del órgano de contratación** y delante de su personal. Unitarias y de extremo a extremo. Tienen que superarse todas. Si solo se pueden lanzar en el ordenador de una persona del proveedor, no es una entrega.

## Señales de alerta en el plan

- No hay ninguna prueba en la que el dato no llegue.
- Todas las capturas son de la misma pantalla y del mismo tamaño.
- Dice «se verificará manualmente» y no hay lista de qué se verifica.
- Las pruebas automáticas solo corren en un equipo del proveedor.

Se corrigen antes de aprobar el plan.
