import { useRef } from "react";
import { CATALOGO, medidas } from "./datos.js";

const MARGEN = 52;
const ESPESOR = 10;
const PASO = 20;

function ajustar(valor) {
  return Math.round(valor / 5) * 5;
}

function limitar(valor, min, max) {
  if (min > max) return (min + max) / 2;
  return Math.min(max, Math.max(min, valor));
}

function puntoEnPlano(evento, svg) {
  const punto = svg.createSVGPoint();
  punto.x = evento.clientX;
  punto.y = evento.clientY;
  const local = punto.matrixTransform(svg.getScreenCTM().inverse());
  return { x: local.x - MARGEN, y: local.y - MARGEN };
}

function tramos(largo, aberturas) {
  const ordenadas = [...aberturas].sort((a, b) => a.desde - b.desde);
  const partes = [];
  let cursor = 0;
  for (const abertura of ordenadas) {
    const desde = Math.max(0, Math.min(largo, abertura.desde));
    const hasta = Math.max(desde, Math.min(largo, abertura.desde + abertura.ancho));
    if (desde > cursor) partes.push([cursor, desde]);
    cursor = hasta;
  }
  if (cursor < largo) partes.push([cursor, largo]);
  return partes;
}

function simbolo(tipo, ancho, fondo) {
  const y = fondo / 2 - 14;
  if (tipo === "fregadero") {
    return (
      <g className="simbolo fregadero" transform={`translate(0 ${y})`}>
        <ellipse cx="0" cy="0" rx={Math.min(ancho * 0.22, 16)} ry="5.5" />
        <circle cx="0" cy="-8" r="1.8" />
      </g>
    );
  }
  if (tipo === "vitro") {
    return (
      <g className="simbolo vitro" transform={`translate(0 ${y})`}>
        <rect x={-ancho * 0.26} y="-6" width={ancho * 0.52} height="12" rx="1.5" />
        <circle cx={-ancho * 0.1} cy="0" r="2.2" fill="none" />
        <circle cx={ancho * 0.1} cy="0" r="2.2" fill="none" />
      </g>
    );
  }
  if (tipo === "horno") {
    return (
      <g className="simbolo horno" transform={`translate(0 ${y})`}>
        <rect x={-ancho * 0.24} y="-6" width={ancho * 0.48} height="12" rx="1.2" />
        <rect x={-ancho * 0.12} y="-3" width={ancho * 0.24} height="6" />
      </g>
    );
  }
  if (tipo === "frigo") {
    return (
      <g className="simbolo" transform={`translate(0 ${y})`}>
        <line x1={-ancho * 0.16} y1="-6" x2={-ancho * 0.16} y2="6" />
      </g>
    );
  }
  if (tipo === "lavavajillas") {
    return (
      <g className="simbolo" transform={`translate(0 ${y})`}>
        <line x1={-ancho * 0.18} y1="-2" x2={ancho * 0.18} y2="-2" />
        <line x1={-ancho * 0.18} y1="3" x2={ancho * 0.18} y2="3" />
      </g>
    );
  }
  if (tipo === "isla") {
    return <rect className="simbolo-isla" x={-ancho / 2 + 7} y={-fondo / 2 + 7} width={ancho - 14} height={fondo - 14} rx="1" />;
  }
  if (tipo === "alto") {
    return <rect className="simbolo-alto" x={-ancho / 2 + 3} y={-fondo / 2 + 3} width={ancho - 6} height={fondo - 6} />;
  }
  if (ancho >= 70) {
    return <line className="simbolo" x1="0" y1={y - 6} x2="0" y2={y + 6} />;
  }
  return null;
}

function Modulo({ modulo, seleccionado, solape, puerta, onSeleccionar, alPulsar }) {
  const def = CATALOGO[modulo.tipo];
  const trazo = solape ? "#9f1d1d" : puerta ? "#9a5b12" : seleccionado ? "#c4622d" : modulo.tipo === "alto" ? "#8d7356" : "#2c2825";
  return (
    <g
      className={seleccionado ? "modulo activo" : "modulo"}
      role="button"
      aria-label={`${def.nombre}, ${modulo.ancho} centímetros`}
      transform={`translate(${modulo.cx} ${modulo.cy}) rotate(${modulo.giro})`}
      onPointerDown={(evento) => {
        evento.stopPropagation();
        onSeleccionar(modulo.id);
        alPulsar(evento, modulo);
      }}
    >
      <rect
        x={-modulo.ancho / 2}
        y={-def.fondo / 2}
        width={modulo.ancho}
        height={def.fondo}
        rx="1.2"
        fill={modulo.tipo === "alto" ? "#fbf6ee" : modulo.tipo === "isla" ? "#f4e4c4" : modulo.tipo === "frigo" ? "#e7eef2" : "#f7f1e8"}
        stroke={trazo}
        strokeWidth={seleccionado || solape ? 2.4 : 1.15}
        strokeDasharray={modulo.tipo === "alto" ? "4 2" : undefined}
      />
      {simbolo(modulo.tipo, modulo.ancho, def.fondo)}
      <line className="frente" x1={-modulo.ancho * 0.18} y1={def.fondo / 2 - 3.2} x2={modulo.ancho * 0.18} y2={def.fondo / 2 - 3.2} stroke={trazo} />
      {modulo.ancho >= 45 && def.fondo >= 34 ? (
        <text y={modulo.tipo === "alto" ? 1 : 8} textAnchor="middle" dominantBaseline="middle" fontSize="8">
          {def.corto}
        </text>
      ) : null}
    </g>
  );
}

export function Plano({ sala, modulos, seleccionado, solapes, enPuerta, onSeleccionar, onMover }) {
  const svgRef = useRef(null);
  const arrastre = useRef(null);
  const ancho = sala.ancho + MARGEN * 2;
  const alto = sala.fondo + MARGEN * 2;
  const norte = tramos(
    sala.ancho,
    sala.huecos.filter((hueco) => hueco.pared === "norte"),
  );
  const este = tramos(
    sala.fondo,
    sala.huecos.filter((hueco) => hueco.pared === "este"),
  );
  const puerta = sala.huecos.find((hueco) => hueco.tipo === "puerta");
  const ventana = sala.huecos.find((hueco) => hueco.tipo === "ventana");
  const ordenados = [...modulos].sort((a, b) => {
    const peso = (modulo) => (modulo.id === seleccionado ? 2 : modulo.tipo === "alto" ? 1 : 0);
    return peso(a) - peso(b);
  });

  function alPulsar(evento, modulo) {
    const svg = svgRef.current;
    if (!svg) return;
    const punto = puntoEnPlano(evento, svg);
    const { w, h } = medidas(modulo);
    arrastre.current = { id: modulo.id, px: punto.x, py: punto.y, cx: modulo.cx, cy: modulo.cy, w, h };
    try {
      svg.setPointerCapture(evento.pointerId);
    } catch {
      // Si el navegador no captura el puntero, el movimiento sigue en el svg.
    }
  }

  function alMover(evento) {
    const activo = arrastre.current;
    const svg = svgRef.current;
    if (!activo || !svg?.getScreenCTM()) return;
    const punto = puntoEnPlano(evento, svg);
    const cx = limitar(ajustar(activo.cx + punto.x - activo.px), activo.w / 2, sala.ancho - activo.w / 2);
    const cy = limitar(ajustar(activo.cy + punto.y - activo.py), activo.h / 2, sala.fondo - activo.h / 2);
    onMover(activo.id, cx, cy);
  }

  function alSoltar() {
    arrastre.current = null;
  }

  const puertaRoja = enPuerta.size > 0;

  return (
    <svg
      ref={svgRef}
      viewBox={`0 0 ${ancho} ${alto}`}
      role="img"
      aria-label="Planta de la cocina"
      onPointerMove={alMover}
      onPointerUp={alSoltar}
      onPointerCancel={alSoltar}
    >
      <rect width={ancho} height={alto} fill="#fbf8f3" onPointerDown={() => onSeleccionar(null)} />
      <text className="cota" x={MARGEN + sala.ancho / 2} y="22" textAnchor="middle">
        {sala.ancho} cm
      </text>
      <line className="cota-linea" x1={MARGEN} y1="28" x2={MARGEN + sala.ancho} y2="28" />
      <text className="cota" transform={`translate(16 ${MARGEN + sala.fondo / 2}) rotate(-90)`} textAnchor="middle">
        {sala.fondo} cm
      </text>
      <line className="cota-linea" x1="28" y1={MARGEN} x2="28" y2={MARGEN + sala.fondo} />
      <text className="norte" x={MARGEN + sala.ancho - 8} y={MARGEN - 16} textAnchor="end">
        N
      </text>

      <g>
        <rect className="suelo" x={MARGEN} y={MARGEN} width={sala.ancho} height={sala.fondo} onPointerDown={() => onSeleccionar(null)} />
        <g clipPath="url(#recorte-suelo)">
          {Array.from({ length: Math.floor(sala.ancho / PASO) + 1 }, (_, indice) => (
            <line key={`v${indice}`} className="rejilla" x1={MARGEN + indice * PASO} y1={MARGEN} x2={MARGEN + indice * PASO} y2={MARGEN + sala.fondo} />
          ))}
          {Array.from({ length: Math.floor(sala.fondo / PASO) + 1 }, (_, indice) => (
            <line key={`h${indice}`} className="rejilla" x1={MARGEN} y1={MARGEN + indice * PASO} x2={MARGEN + sala.ancho} y2={MARGEN + indice * PASO} />
          ))}
        </g>
        <clipPath id="recorte-suelo">
          <rect x={MARGEN} y={MARGEN} width={sala.ancho} height={sala.fondo} />
        </clipPath>
      </g>

      <g className="muros">
        {norte.map(([desde, hasta]) => (
          <rect key={`n${desde}`} x={MARGEN + desde} y={MARGEN - ESPESOR} width={hasta - desde} height={ESPESOR} />
        ))}
        {este.map(([desde, hasta]) => (
          <rect key={`e${desde}`} x={MARGEN + sala.ancho} y={MARGEN + desde} width={ESPESOR} height={hasta - desde} />
        ))}
        <rect x={MARGEN - ESPESOR} y={MARGEN} width={ESPESOR} height={sala.fondo} />
        <rect x={MARGEN} y={MARGEN + sala.fondo} width={sala.ancho} height={ESPESOR} />
      </g>

      {ventana ? (
        <g className="ventana">
          <rect x={MARGEN + ventana.desde} y={MARGEN - ESPESOR} width={ventana.ancho} height={ESPESOR} />
          <line x1={MARGEN + ventana.desde} y1={MARGEN - ESPESOR / 2} x2={MARGEN + ventana.desde + ventana.ancho} y2={MARGEN - ESPESOR / 2} />
        </g>
      ) : null}

      {puerta ? (
        <g className={puertaRoja ? "puerta mal" : "puerta"}>
          <path
            d={`M ${MARGEN + sala.ancho} ${MARGEN + puerta.desde + puerta.ancho} A ${puerta.ancho} ${puerta.ancho} 0 0 1 ${MARGEN + sala.ancho - puerta.ancho} ${MARGEN + puerta.desde}`}
          />
          <line
            x1={MARGEN + sala.ancho}
            y1={MARGEN + puerta.desde}
            x2={MARGEN + sala.ancho - puerta.ancho}
            y2={MARGEN + puerta.desde}
          />
        </g>
      ) : null}

      <g transform={`translate(${MARGEN} ${MARGEN})`}>
        {ordenados.map((modulo) => (
          <Modulo
            key={modulo.id}
            modulo={modulo}
            seleccionado={modulo.id === seleccionado}
            solape={solapes.has(modulo.id)}
            puerta={enPuerta.has(modulo.id)}
            onSeleccionar={onSeleccionar}
            alPulsar={alPulsar}
          />
        ))}
      </g>
    </svg>
  );
}
