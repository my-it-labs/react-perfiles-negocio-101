# No todas las pantallas son la misma pantalla

[← Página anterior](01-una-frase.md) · [Siguiente página →](03-la-entrega.md)

En el mismo pliego suelen viajar dos encargos que parecen uno:

**La pantalla que mira el público.** Nadie se identifica delante de ella. Nadie la busca en un buscador. No se comparte su dirección. Está encendida siempre y nadie la vuelve a abrir.

**La herramienta con la que el personal programa lo que sale en esa pantalla.** Aquí hay usuarios, contraseñas, permisos por perfil, datos que no deben salir del edificio y, a veces, conexiones a sistemas internos.

Son dos oficios distintos. Pedirlos con la misma frase es el error más caro del pliego, porque el proveedor cotizará el fácil y descubrirá el difícil a mitad del proyecto.

## Lo que llega del proveedor, y lo que de verdad decide

La discusión suele llegar en forma de nombres de herramientas. Conviene tener la traducción a mano, en una línea cada una:

- **React** es la forma de construir la pantalla por piezas: una pieza por cada cosa que se ve, y la pieza se vuelve a dibujar cuando cambia su dato.
- **Vite** es el taller que convierte esas piezas en los archivos que el navegador abre. No queda nada suyo funcionando después.
- **Next.js** es lo mismo más un servidor propio, que se queda encendido y puede preparar la página antes de enviarla y guardar contraseñas donde el navegador no las ve.

Y ahora la parte que importa: **esa decisión no se toma comparando las tres.** Se toma con dos preguntas.

1. ¿Hay alguien que se identifique para entrar?
2. ¿Hay algo que no puede viajar al navegador? Una contraseña, la clave de un servicio de pago, un dato personal.

Si las dos respuestas son no —el caso de la pantalla del público— ese servidor propio no aporta nada y sí cuesta: es una pieza más que hay que instalar, vigilar, actualizar y certificar durante toda la vida del sistema.

Si alguna respuesta es sí —el caso de la herramienta del personal— ese servidor es el sitio natural de lo que no puede verse, y pedirlo es razonable.

## Cómo se escribe eso en el pliego

No por el nombre de la herramienta. Por la condición:

> La aplicación de las pantallas se entregará como archivos que el navegador del equipo abre directamente, sin ningún servicio propio del proveedor que deba permanecer en ejecución para que la pantalla funcione.

> La herramienta de gestión de contenidos tendrá acceso por usuario y perfil. Ninguna credencial de acceso a sistemas de terceros estará presente en el navegador del operador.

Dos frases, y el proveedor ya no puede meter un servidor en el tren ni dejar una contraseña a la vista.

**Tip.** Si el pliego fija una herramienta por nombre, que sea por el motivo real y escrito: porque el equipo que va a heredar el mantenimiento ya trabaja con ella. Eso se defiende. «Porque es lo más moderno» no.
