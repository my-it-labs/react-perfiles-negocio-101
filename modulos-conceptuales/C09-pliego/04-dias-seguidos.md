# La pantalla que no se apaga

[← Página anterior](03-la-entrega.md) · [Siguiente página →](05-la-recepcion.md)

![La misma pantalla en cuatro momentos: el día 1 marca 3 min, el día 4 marca 6 min, el día 8 sigue marcando 6 min en ámbar y el día 11 está en negro. Debajo, una barra de memoria ocupada que sube en cada paso.](../img/dias-seguidos.svg)

- **Lo que vuestros pliegos ya cubren bien.** El equipo: arranque por debajo de un tiempo dado, aguantar un corte de alimentación, sobrevivir a un reinicio no controlado, vigilarse y recuperarse sin que vaya nadie.

- **Y el contenido, mejor todavía.** Las tablas que cruzan cada avería con cada tipo de contenido y dicen qué se ve en cada casilla: reintentar dos veces, mantener la última lista válida, ignorar el elemento mal formado, pasar al siguiente vídeo, y un contenido de reserva guardado en el propio equipo. Eso está por encima de lo que pide la mayoría de pliegos.

- **La casilla que falta es la de la aplicación.** El equipo arrancado, el contenido llegando, y la aplicación once días sin volver a empezar porque nadie la cierra nunca.

- **Se va comiendo la memoria.** Cada dato nuevo la hace dibujar otra vez; si no limpia detrás de sí, al cabo de unos días el navegador la descarta y la pantalla se queda en negro. Visto desde fuera parece una avería de red, y la red funciona.

- **La hora se queda quieta.** El contador que debería ir bajando se queda en el minuto en que la aplicación se abrió. La pantalla sigue informando, y lo que informa es falso. Esto es peor que una pantalla apagada, porque nadie lo reporta.

- **Al volver el enlace se sigue viendo lo viejo.** El dato volvió, pero nadie lo pidió otra vez. Vuestras tablas de contenido ya resuelven esto; la aplicación necesita la misma regla y suele no tenerla.

- **Y los fallos no quedan en ninguna parte.** Por defecto se escriben en un sitio al que solo se llega enchufando un teclado y una pantalla al equipo. En un túnel o en un andén, eso no existe.

Cuatro frases lo cubren:

> La aplicación funcionará de forma continuada durante al menos 30 días sin reinicio, manteniendo estable la memoria ocupada. Se medirá en las pruebas de aceptación y constará en el acta.

> Toda información con validez temporal se recalculará con el reloj del equipo, no a partir del momento en que la aplicación se inició.

> Al restablecerse una comunicación interrumpida, la aplicación volverá a solicitar toda la información que esté mostrando.

> Los fallos de la aplicación se incorporarán a los registros del equipo, con el mismo mecanismo de recogida que el resto del sistema.

**Tip.** La prueba que destapa casi todo esto no cuesta dinero: dejarla encendida un puente y mirarla el martes. Pide que figure en el plan de pruebas, con una fotografía de la pantalla al final.
