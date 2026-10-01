# Dato y desenlaces

[← Página anterior](01-uso-y-superficie.md) · [Siguiente página →](03-que-se-entrega.md)

La pantalla es una lectura del dato. El pliego nombra el dato con el mismo cuidado que la pantalla. Si no lo nombra, el proveedor enseñará un array escrito en el proyecto, como `datos.js` en la demo, y la aceptación no podrá distinguir la maqueta del servicio.

## De dónde sale

Para cada dato que la persona ve, el pliego responde tres cosas: qué sistema lo guarda, qué operación lo lee o lo escribe, y quién autoriza un entorno de prueba. «Una API REST» no basta. Hace falta el nombre del sistema y, si ya existe el contrato, el recurso (`GET` de incidencias abiertas, alta de incidencia, cierre). Si el sistema todavía no existe, el pliego lo dice y encarga también definir esa operación, no solo la pantalla. Encargar la pantalla contra un sistema sin nombre deja la integración para el final, cuando ya no hay plazo.

Lo que la pantalla no debe recibir se lista. Notas internas en la ficha pública, teléfonos personales, identificadores que no hacen falta para la tarea. El checklist de acceso del módulo anterior es, aquí, una prescripción: el JSON de prueba no trae campos de más, y el panel no es una ruta abierta.

## Las frases, literales

Cada lectura que el usuario dispara tiene cinco celdas. Se rellenan con la frase que verá la persona, no con el código HTTP.

| Momento | Ejemplo de frase que el pliego puede fijar |
|---------|--------------------------------------------|
| Antes de pedir | «Elige una línea.» |
| Mientras la red no contesta | «Cargando incidencias.» |
| Con datos | La lista, con el identificador y la línea |
| Con cero | «No hay incidencias abiertas.» |
| Si la petición falla | «No se han podido cargar las incidencias.» |

Cero y fallo no comparten frase. La espera no es un puesto congelado. Si hay escritura, se añaden dos frases más: guardado y no guardado. El pliego puede fijar el texto o exigir que la oferta lo proponga y la aceptación lo congele. Lo que no puede hacer es dejar la celda en blanco y dar por bueno que «sale un listado».

## Lo que se excluye para que no vuelva

Si este contrato no incluye canal en vivo, cola sin cobertura ni mapa, se escribe. Una exclusión es una prescripción. Sin ella, la oferta añadirá WebSockets o una app de campo como mejora, y el objeto habrá cambiado sin otro pliego.
