export const CATALOGO = {
  bajo: { nombre: "Mueble bajo", corto: "Bajo", fondo: 60, ancho: 60, precio: 280 },
  alto: { nombre: "Mueble alto", corto: "Alto", fondo: 35, ancho: 60, precio: 190 },
  fregadero: { nombre: "Fregadero", corto: "Freg.", fondo: 60, ancho: 80, precio: 460 },
  vitro: { nombre: "Vitrocerámica", corto: "Vitro", fondo: 60, ancho: 60, precio: 620 },
  horno: { nombre: "Horno", corto: "Horno", fondo: 60, ancho: 60, precio: 740 },
  frigo: { nombre: "Frigorífico", corto: "Frigo", fondo: 60, ancho: 60, precio: 980 },
  lavavajillas: { nombre: "Lavavajillas", corto: "Lavav.", fondo: 60, ancho: 60, precio: 650 },
  isla: { nombre: "Isla", corto: "Isla", fondo: 90, ancho: 150, precio: 1240 },
};

export const TIPOS = ["bajo", "alto", "fregadero", "vitro", "horno", "frigo", "lavavajillas", "isla"];

export const ANCHOS = [30, 40, 45, 50, 60, 80, 90, 120, 150, 180, 200];

export const SALA_INICIAL = {
  ancho: 440,
  fondo: 320,
  huecos: [
    { id: "ventana", tipo: "ventana", pared: "norte", desde: 150, ancho: 140 },
    { id: "puerta", tipo: "puerta", pared: "este", desde: 40, ancho: 80 },
  ],
};

export const MODULOS_INICIALES = [
  { id: "m1", tipo: "frigo", cx: 30, cy: 290, ancho: 60, giro: 180 },
  { id: "m2", tipo: "bajo", cx: 90, cy: 290, ancho: 60, giro: 180 },
  { id: "m3", tipo: "fregadero", cx: 160, cy: 290, ancho: 80, giro: 180 },
  { id: "m4", tipo: "bajo", cx: 230, cy: 290, ancho: 60, giro: 180 },
  { id: "m5", tipo: "vitro", cx: 290, cy: 290, ancho: 60, giro: 180 },
  { id: "m6", tipo: "horno", cx: 350, cy: 290, ancho: 60, giro: 180 },
  { id: "m7", tipo: "lavavajillas", cx: 410, cy: 290, ancho: 60, giro: 180 },
  { id: "m8", tipo: "bajo", cx: 30, cy: 100, ancho: 200, giro: 270 },
  { id: "m9", tipo: "alto", cx: 90, cy: 302.5, ancho: 60, giro: 180 },
  { id: "m10", tipo: "alto", cx: 160, cy: 302.5, ancho: 80, giro: 180 },
  { id: "m11", tipo: "alto", cx: 230, cy: 302.5, ancho: 60, giro: 180 },
  { id: "m12", tipo: "alto", cx: 17.5, cy: 100, ancho: 200, giro: 270 },
  { id: "m13", tipo: "isla", cx: 210, cy: 115, ancho: 150, giro: 0 },
];

export function capa(modulo) {
  return modulo.tipo === "alto" ? "alto" : "planta";
}

export function medidas(modulo) {
  const fondo = CATALOGO[modulo.tipo].fondo;
  const horizontal = modulo.giro % 180 === 0;
  return {
    w: horizontal ? modulo.ancho : fondo,
    h: horizontal ? fondo : modulo.ancho,
  };
}

export function caja(modulo) {
  const { w, h } = medidas(modulo);
  return { x: modulo.cx - w / 2, y: modulo.cy - h / 2, w, h };
}

export function seSolapan(a, b) {
  const margen = 0.5;
  return a.x < b.x + b.w - margen && a.x + a.w > b.x + margen && a.y < b.y + b.h - margen && a.y + a.h > b.y + margen;
}

export function idsEnSolape(modulos) {
  const ids = new Set();
  for (let i = 0; i < modulos.length; i += 1) {
    for (let j = i + 1; j < modulos.length; j += 1) {
      if (capa(modulos[i]) !== capa(modulos[j])) continue;
      if (seSolapan(caja(modulos[i]), caja(modulos[j]))) {
        ids.add(modulos[i].id);
        ids.add(modulos[j].id);
      }
    }
  }
  return ids;
}

export function zonaPuerta(sala) {
  const puerta = sala.huecos.find((hueco) => hueco.tipo === "puerta");
  if (!puerta || puerta.pared !== "este") return null;
  return {
    x: sala.ancho - puerta.ancho,
    y: puerta.desde,
    w: puerta.ancho,
    h: puerta.ancho,
  };
}

export function idsEnPuerta(sala, modulos) {
  const zona = zonaPuerta(sala);
  if (!zona) return new Set();
  const ids = new Set();
  for (const modulo of modulos) {
    if (capa(modulo) === "planta" && seSolapan(caja(modulo), zona)) ids.add(modulo.id);
  }
  return ids;
}

export function precioDe(modulo) {
  const def = CATALOGO[modulo.tipo];
  return Math.round(def.precio * (modulo.ancho / def.ancho));
}

export function resumen(modulos) {
  return modulos.reduce(
    (total, modulo) => {
      total.piezas += 1;
      total.euros += precioDe(modulo);
      if (modulo.tipo === "isla") total.islas += 1;
      else if (modulo.tipo === "alto") total.alto += modulo.ancho;
      else total.bajo += modulo.ancho;
      return total;
    },
    { piezas: 0, euros: 0, bajo: 0, alto: 0, islas: 0 },
  );
}

export function giroInicial(tipo) {
  if (tipo === "alto" || tipo === "isla") return 0;
  return 180;
}

export function cabe(sala, pieza) {
  const { w, h } = medidas(pieza);
  return pieza.cx - w / 2 >= -0.1 && pieza.cy - h / 2 >= -0.1 && pieza.cx + w / 2 <= sala.ancho + 0.1 && pieza.cy + h / 2 <= sala.fondo + 0.1;
}

export function huecoLibre(modulos, pieza, sala) {
  const { w, h } = medidas(pieza);
  const paso = 10;
  const candidatos = [];
  if (pieza.tipo === "isla") {
    candidatos.push({ cx: sala.ancho / 2, cy: sala.fondo / 2 });
  }
  if (pieza.tipo === "alto") {
    for (let x = 0; x <= sala.ancho - w; x += paso) candidatos.push({ cx: x + w / 2, cy: h / 2 });
    for (let y = 0; y <= sala.fondo - h; y += paso) candidatos.push({ cx: w / 2, cy: y + h / 2 });
  } else {
    for (let x = 0; x <= sala.ancho - w; x += paso) candidatos.push({ cx: x + w / 2, cy: sala.fondo - h / 2 });
    for (let y = 0; y <= sala.fondo - h; y += paso) candidatos.push({ cx: w / 2, cy: y + h / 2 });
  }
  for (let y = 0; y <= sala.fondo - h; y += paso) {
    for (let x = 0; x <= sala.ancho - w; x += paso) candidatos.push({ cx: x + w / 2, cy: y + h / 2 });
  }
  for (const candidato of candidatos) {
    const prueba = { ...pieza, ...candidato };
    if (!cabe(sala, prueba)) continue;
    const choca = modulos.some((otro) => capa(otro) === capa(prueba) && seSolapan(caja(otro), caja(prueba)));
    const enPuerta = capa(prueba) === "planta" && idsEnPuerta(sala, [prueba]).size > 0;
    if (!choca && !enPuerta) return candidato;
  }
  return { cx: sala.ancho / 2, cy: sala.fondo / 2 };
}

export function limitarCentro(sala, modulo) {
  const { w, h } = medidas(modulo);
  const minX = w / 2;
  const maxX = Math.max(minX, sala.ancho - w / 2);
  const minY = h / 2;
  const maxY = Math.max(minY, sala.fondo - h / 2);
  return {
    ...modulo,
    cx: Math.min(maxX, Math.max(minX, modulo.cx)),
    cy: Math.min(maxY, Math.max(minY, modulo.cy)),
  };
}
