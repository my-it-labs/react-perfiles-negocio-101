# Qué se encarga

[← Página anterior](../README.md) · [Siguiente página →](02-dos-documentos.md)

Una licitación compra un uso. El proveedor —en el procedimiento, el licitador— contesta lo que el pliego pregunta. Si el pliego dice «aplicación React moderna», la oferta repetirá esa frase y el producto seguirá sin estar decidido. El mismo desmontaje que sirve para leer una propuesta sirve para escribirla al revés: cada frase del pliego tiene que poder señalarse después en una pantalla.

## El objeto, en una frase

El objeto nombra quién usa qué, y para qué decisión. No nombra el marco.

| Objeto que se puede encargar | Objeto que no cierra nada |
|------------------------------|---------------------------|
| Consulta pública del estado de las líneas, con URL propia | Portal moderno de la red |
| Panel de sala para abrir y cerrar incidencias durante el turno | Herramienta React de operaciones |
| Las dos cosas, en dos superficies, con el mismo dato de líneas | Una app única para viajeros y sala |

«React» entra en el pliego cuando es una restricción de la casa: el equipo que mantendrá el producto ya trabaja en React, o hay un sistema de piezas que la nueva pantalla tiene que reutilizar. Entra como restricción de mantenimiento, escrita como tal. No entra como sinónimo de calidad. Si la casa no tiene esa restricción, el pliego fija el uso y la superficie, y deja el marco como respuesta de la oferta, con la obligación de justificarlo.

## Qué queda del lado de quien encarga

Quien escribe las prescripciones técnicas tiene que poder rellenar, antes de publicar, esta lista. Si una fila está vacía, el proveedor la va a rellenar a su favor.

- Quién usa cada pantalla, y en qué momento del servicio.
- Si la primera vista tiene que leerse al llegar —buscador, aviso, enlace compartido— o si es una herramienta con sesión.
- De qué sistema sale el dato, y quién es dueño de ese sistema.
- Qué frases tiene que ver la persona en carga, con datos, con cero resultados y con fallo.
- Qué queda fuera de este contrato, dicho en voz alta.

La demostración de los módulos anteriores ya separó esas filas en la red de transporte: el documento que se recarga, la SPA que conserva la memoria, la portada cuyo HTML nace en el servidor, y el flujo con cuatro desenlaces. Un pliego de ese producto no pide «lo de las demos». Pide, para cada superficie, el comportamiento que la demo sirvió para reconocer.
