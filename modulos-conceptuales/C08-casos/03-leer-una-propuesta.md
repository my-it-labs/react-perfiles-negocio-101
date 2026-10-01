# Leer una frase de propuesta

[← Página anterior](02-alarma-en-vivo.md) · [Siguiente página →](../../modulos/M01-ecosistema-react/README.md)

La frase, inventada y reconocible:

> Panel de operaciones en React, con Next.js por el SEO, app móvil en Ionic nativa y de paso el puesto de sala en Electron. Tiempo real con WebSockets. Lo publicamos en el servidor web.

Se puede desmontar con lo que ya tienes, sin escribir una línea.

## Qué dice de verdad, y qué se pisa

**React.** Habrá piezas y datos. Pide el boceto del panel y el árbol. Si no existe, la frase no ha empezado.

**Next.js por el SEO.** El SEO importa en lo que un buscador debe leer. Un panel de operaciones suele estar tras una sesión. Ahí el HTML fabricado para Google no es el argumento. Puede haber una portada pública que sí lo necesite: esa ruta, en Next, puede nacer en el servidor o al publicar. El panel puede nacer en el navegador. «Next en todo el producto por el SEO» mezcla las dos rutas. La pregunta es qué direcciones tienen que llegar ya escritas.

**Ionic nativa.** Ionic empaqueta la web. La promesa justa es una interfaz, un icono, algunas capacidades del teléfono. La palabra «nativa» pertenece a React Native, y ni siquiera allí significa «la misma pantalla de la web». Hay que elegir. Si quien está en vía consulta y poco más, Ionic puede bastar. Si el móvil es la herramienta principal, toca hablar de React Native y de un oficio de interfaz distinto.

**Electron en la sala.** Entra si el puesto necesita disco, varias ventanas o salir del navegador corporativo. Si la sala puede abrir una dirección, Electron es un instalable de más. Pregunta qué capacidad del ordenador está en el requisito.

**WebSockets.** Encaja con la alarma que llega sola. Pide el cuarto final traducido: silencio sano contra vía caída, y la visita que cierra la escucha.

**Publicarlo en el servidor web.** Solo es cierto para el resultado que el navegador abre. Next puede necesitar un servidor que fabrique páginas, no solo archivos quietos. Ionic y Electron se publican por otros canales: tiendas, instaladores. Un solo «despliegue web» no cubre las tres superficies.

## La lectura que ya puedes devolver

React para las piezas del panel. Next solo en las rutas que de verdad se comparten o se indexan; el panel interno puede ser navegador. Una superficie móvil, con el nombre correcto. Electron solo con un requisito de puesto. Una vía en vivo con vacío y con sordera diseñados. Y un taller distinto para cada cosa que se entrega.

El otro recorrido del curso abre las demos y enseña estas ideas con aplicaciones pequeñas. Si quieres ver el documento tradicional, la SPA y un Next uno al lado del otro, sigue por ahí. Escribir el encargo, en vez de desmontar la frase del proveedor, está en [Licitar una aplicación](../../modulos/M06-licitar/README.md).

## Qué preguntar al cerrar la reunión

- ¿Qué rutas necesitan HTML ya hecho, y cuáles son una herramienta con sesión?
- ¿El móvil es la web empaquetada o una app con controles propios?
- ¿Qué se instala, qué se sirve, y quién repite el taller la próxima semana?
