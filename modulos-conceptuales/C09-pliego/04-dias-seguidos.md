# La pantalla que no se apaga

[← Página anterior](03-la-entrega.md) · [Siguiente página →](05-la-recepcion.md)

Los pliegos de estos sistemas cubren muy bien dos cosas.

**El equipo.** Arranca por debajo de un tiempo dado, aguanta un corte de alimentación, sobrevive a un reinicio no controlado, se vigila a sí mismo y se recupera sin que vaya nadie.

**El contenido.** Hay tablas que cruzan cada avería con cada tipo de contenido y dicen qué se ve en cada casilla: reintentar dos veces con cinco segundos de espera, mantener la última lista válida, ignorar el elemento que llega mal formado y mostrar los correctos, pasar al siguiente vídeo, y un vídeo de reserva guardado en el propio equipo para cuando no haya ninguno.

Esas tablas son mejores que lo que pide la mayoría de los pliegos. No hay nada que enseñar ahí.

Lo que falta es la casilla de la aplicación.

## Lo que pasa entre dos reinicios

El equipo puede estar arrancado. El contenido puede estar llegando. Y la aplicación puede llevar once días sin volver a empezar, porque nadie la cierra nunca. Eso tiene tres consecuencias concretas, y las tres se han visto en instalaciones reales.

**Va ocupando cada vez más memoria.** Cada vez que entra un dato nuevo, la aplicación dibuja; si no limpia detrás de sí, lo viejo se queda. Al cabo de unos días el navegador la descarta y la pantalla se queda en negro. Visto desde fuera parece una avería de red, y no lo es: la red funciona.

**La hora se queda quieta.** Un contador que debería ir bajando se queda en el minuto en que la aplicación se abrió. La pantalla sigue mostrando información, y es falsa. Esto es peor que una pantalla apagada, porque nadie lo reporta.

**Al recuperar el enlace, se sigue viendo lo viejo.** El dato volvió, pero nadie lo pidió otra vez. Si tus tablas de contenido ya resuelven esto —forzando que al reconectar todo se vuelva a descargar—, la aplicación necesita exactamente la misma regla, y suele no tenerla.

## Los requisitos que lo cubren

Cuatro frases, en el formato del resto del pliego:

> La aplicación funcionará de forma continuada durante al menos **30 días** sin reinicio, manteniendo estable la memoria ocupada. Se medirá en las pruebas de aceptación y el resultado constará en el acta.

> Toda información con validez temporal se recalculará con el reloj del equipo, no con el momento en que la aplicación se abrió.

> Al recuperarse una comunicación interrumpida, la aplicación volverá a solicitar toda la información que esté mostrando, sin esperar al siguiente ciclo.

> Si la aplicación deja de responder, el equipo la reiniciará por sí mismo y mostrará la imagen de reserva mientras lo hace. El incidente quedará registrado en los registros del equipo.

Esa última línea tiene truco, y es un truco que conviene conocer: los fallos de una aplicación de este tipo se escriben, por defecto, en un sitio que solo se ve conectando un teclado y una pantalla al equipo. En un túnel o en un andén, eso no existe. Si el pliego no dice que esos fallos tienen que acabar en los registros del equipo —los que ya se recogen y se envían—, nadie se enterará nunca de nada.

**Tip.** La prueba que destapa casi todo esto no cuesta dinero: dejarla encendida un puente y mirarla el martes. Pide que esa prueba figure en el plan de pruebas con esas palabras, y con la obligación de adjuntar una fotografía de la pantalla al final.
