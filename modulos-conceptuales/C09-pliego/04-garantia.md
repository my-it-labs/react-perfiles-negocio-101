# Qué queda en garantía

[← Página anterior](03-aceptacion.md) · [Siguiente página →](05-ejemplo.md)

Garantía es lo que aparece en producción después de firmar la recepción. Lo que se puede prever —semanas sin reinicio, el reloj del equipo, volver a pedir los datos, los fallos en los registros— son requerimientos, y se comprueban en la aceptación. No se vuelven a escribir aquí.

Quedan dos cosas.

**Los registros.** Un fallo de la aplicación que salga en producción tiene que acabar en los registros que el sistema ya recoge y envía a los sistemas centrales, con los mismos niveles que el resto. Si solo se ve enchufando un teclado al equipo, nadie se entera.

**La bolsa de horas.** Cada evolutivo vuelve a lanzar las mismas pruebas automáticas, en el entorno del órgano de contratación. Así se ve en una tarde si lo nuevo rompió lo que ya funcionaba. Sin esas pruebas, cada evolutivo repite la recepción entera y la bolsa se gasta en comprobar.
