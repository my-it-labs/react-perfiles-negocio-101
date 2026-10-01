# El plano sale del dato

[← Demos](../../README.md)

## Arranque

El planner se arranca con `npm run demo:cocina` y se abre en `http://localhost:5174`. Vite y React están declarados en `demos/cocina/package.json`. Si el puerto no responde, el fallo es de entorno, no del plano.

El HTML de `index.html` trae un `<div id="root">` vacío. `src/main.jsx` mete `App` ahí. A partir de ese momento, lo que se ve lo produce React: una lista de módulos y una sala. El SVG no guarda el dibujo. Lo calcula.

## Ficheros que importan en la guía

| Fichero | Qué mirar |
|---------|-----------|
| `src/datos.js` | El catálogo, la sala inicial y la lista de módulos. También el precio, el solape y la zona de la puerta |
| `src/App.jsx` | `sala`, `modulos` y `seleccionado`. El resumen y la lista leen ese estado |
| `src/Plano.jsx` | El SVG. Recorre `modulos` y pinta un rectángulo por pieza |

Conviene la pantalla en el navegador y `datos.js` visible. La marca del encabezado dice «React + SVG» y el fondo es nogal. El fregadero empieza seleccionado: su centro, 160 cm y 290 cm, es el mismo número en la ficha y en el plano.

## Qué se va a comprobar

1. Arrastrar el fregadero cambia el centro de la ficha y mueve el rectángulo. No hay un segundo dibujo que actualizar.
2. Girar deja la marca de cobre en el frente del módulo. El giro es un número de la pieza; el SVG lo aplica con `rotate`.
3. Cambiar el ancho de la ventana abre o cierra el muro norte. La ventana es un dato de la sala, no un trazo suelto.
4. El presupuesto de arriba usa la misma lista. Ensanchar un módulo cambia su precio porque el precio es ancho por tarifa.
5. Soltar un módulo encima de otro pone el trazo en rojo y escribe el aviso. Meter uno en el arco de la puerta lo pone en ocre. Las dos reglas leen la lista; no viven dentro del dibujo.
6. Recargar la pestaña deshace el plano: la memoria está en el estado de `App`, no en el SVG.
