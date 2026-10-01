# Los requerimientos funcionales

[← Página anterior](01-alcance.md) · [Siguiente página →](03-fuentes.md)

![Hoja de prescripciones con doce requerimientos para el equipo, las comunicaciones y la instalación, y un solo requerimiento, resaltado, para la aplicación que se ve.](../img/pliego-el-hueco.svg)

- **La asimetría.** Los requerimientos de la CPU pueden pasar de setenta. Los de las pantallas, de veinte. La aplicación que el viajero mira suele tener uno: «será una aplicación web progresiva (React) y responsive».

- **Eso no es un requerimiento, es una etiqueta.** No se puede medir, ni probar en el FAT, ni rechazar en el acta.

- **Lo que tiene que decir ese bloque.** Cuatro cosas, y ninguna es técnica:
  - Qué se ve cuando el dato no llega, llega tarde o llega mal.
  - Qué hace la aplicación cuando se recupera una comunicación interrumpida.
  - Qué es configurable sin volver a fabricar el paquete: textos, colores, tamaños, posiciones, duraciones y orígenes de datos.
  - Qué se ve mientras el equipo arranca, y qué se ve si la aplicación no llega a arrancar.

- **Y un requerimiento de arquitectura, uno solo.** Que no quede ningún servicio del proveedor funcionando para que la aplicación pinte. Todo lo que se queda encendido hay que inventariarlo, mantenerlo, actualizarlo y certificarlo durante la vida del contrato, y eso se valora en la oferta o se paga después.

- **Se escribe en el formato de siempre.** Tabla de tres columnas, identificador, concepto y descripción, dentro de la familia de funcionales que ya usáis.

**Tip.** La prueba de que un requerimiento está bien escrito es que alguien pueda ponerse delante de la pantalla y decir «esto cumple» o «esto no cumple» sin llamar a nadie. Si hace falta interpretar, todavía es una etiqueta.
