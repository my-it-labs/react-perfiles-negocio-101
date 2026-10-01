# Lectura

[← Página anterior](05-lento.md) · [Siguiente página →](../../../../modulos/M06-licitar/README.md)

## Lo que la guía ha fijado

| Gesto | Red | Pantalla al terminar |
|-------|-----|----------------------|
| Ninguno | — | «Elige un caso.» |
| Con datos | 200 y dos incidencias | INC-14 en L2, INC-15 en L1 |
| Vacío | 200 y lista vacía | «No hay incidencias abiertas.» |
| Error | 500 | «No se han podido cargar las incidencias.» |
| Lento | 200, ~1,2 s, dos incidencias | Primero la carga, luego los mismos artículos |

Cuatro frases de negocio, ninguna repetida para dos desenlaces. La carga es la quinta frase, y es transitoria.

## Cómo se reutiliza en una entrega

Se cambia el botón de la demo por la acción real y se mantiene la tabla: qué se ve antes de pedir, qué se ve mientras, qué se ve con datos, qué se ve con cero, qué se ve si el código no es correcto. Si la entrega no puede rellenar esas celdas con frases literales, el flujo no está definido, aunque la petición «funcione» en el caso feliz.

## Cierre del recorrido

Las tres demos quedan leídas: el documento que se sustituye, la SPA que conserva la memoria y pierde la URL, y Next.js con HTML de servidor, hora de cliente y esta API. El módulo siguiente escribe el pliego que habría encargado esas superficies. El índice del repositorio sigue siendo la forma de volver a una página concreta, sin recorrer otra vez toda la cadena.
