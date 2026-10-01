import { useMemo, useState } from "react";
import { Plano } from "./Plano.jsx";
import {
  ANCHOS,
  CATALOGO,
  MODULOS_INICIALES,
  SALA_INICIAL,
  TIPOS,
  giroInicial,
  huecoLibre,
  idsEnPuerta,
  idsEnSolape,
  limitarCentro,
  precioDe,
  resumen,
} from "./datos.js";

const euros = new Intl.NumberFormat("es-ES", {
  style: "currency",
  currency: "EUR",
  maximumFractionDigits: 0,
});

const centimetros = new Intl.NumberFormat("es-ES", {
  minimumFractionDigits: 1,
  maximumFractionDigits: 1,
});

function clonar(valor) {
  return structuredClone(valor);
}

export function App() {
  const [sala, setSala] = useState(() => clonar(SALA_INICIAL));
  const [modulos, setModulos] = useState(() => clonar(MODULOS_INICIALES));
  const [seleccionado, setSeleccionado] = useState("m3");

  const solapes = useMemo(() => idsEnSolape(modulos), [modulos]);
  const enPuerta = useMemo(() => idsEnPuerta(sala, modulos), [sala, modulos]);
  const cuenta = useMemo(() => resumen(modulos), [modulos]);
  const activo = modulos.find((modulo) => modulo.id === seleccionado) ?? null;

  function mover(id, cx, cy) {
    setModulos((lista) => lista.map((modulo) => (modulo.id === id ? { ...modulo, cx, cy } : modulo)));
  }

  function cambiarSala(campo, valor) {
    if (!Number.isFinite(valor)) return;
    const medida = Math.min(700, Math.max(260, valor));
    setSala((actual) => {
      const siguiente = { ...actual, [campo]: medida };
      siguiente.huecos = actual.huecos.map((hueco) => {
        const largo = hueco.pared === "norte" || hueco.pared === "sur" ? siguiente.ancho : siguiente.fondo;
        const ancho = Math.min(hueco.ancho, largo - 20);
        const desde = Math.min(hueco.desde, Math.max(0, largo - ancho));
        return { ...hueco, ancho, desde };
      });
      return siguiente;
    });
    setModulos((lista) => lista.map((modulo) => limitarCentro({ ...sala, [campo]: medida }, modulo)));
  }

  function cambiarHueco(id, campo, valor) {
    if (!Number.isFinite(valor)) return;
    setSala((actual) => ({
      ...actual,
      huecos: actual.huecos.map((hueco) => {
        if (hueco.id !== id) return hueco;
        const largo = hueco.pared === "norte" || hueco.pared === "sur" ? actual.ancho : actual.fondo;
        const siguiente = { ...hueco, [campo]: valor };
        siguiente.ancho = Math.min(Math.max(40, siguiente.ancho), largo - 20);
        siguiente.desde = Math.min(Math.max(0, siguiente.desde), largo - siguiente.ancho);
        return siguiente;
      }),
    }));
  }

  function agregar(tipo) {
    const pieza = {
      id: `m${Date.now()}`,
      tipo,
      cx: 0,
      cy: 0,
      ancho: CATALOGO[tipo].ancho,
      giro: giroInicial(tipo),
    };
    const sitio = huecoLibre(modulos, pieza, sala);
    const nuevo = limitarCentro(sala, { ...pieza, ...sitio });
    setModulos((lista) => [...lista, nuevo]);
    setSeleccionado(nuevo.id);
  }

  function cambiarAncho(ancho) {
    if (!activo) return;
    setModulos((lista) =>
      lista.map((modulo) => (modulo.id === activo.id ? limitarCentro(sala, { ...modulo, ancho }) : modulo)),
    );
  }

  function girar() {
    if (!activo) return;
    setModulos((lista) =>
      lista.map((modulo) =>
        modulo.id === activo.id ? limitarCentro(sala, { ...modulo, giro: (modulo.giro + 90) % 360 }) : modulo,
      ),
    );
  }

  function quitar() {
    if (!activo) return;
    setModulos((lista) => lista.filter((modulo) => modulo.id !== activo.id));
    setSeleccionado(null);
  }

  function reiniciar() {
    setSala(clonar(SALA_INICIAL));
    setModulos(clonar(MODULOS_INICIALES));
    setSeleccionado("m3");
  }

  const nombresSolape = modulos.filter((modulo) => solapes.has(modulo.id)).map((modulo) => CATALOGO[modulo.tipo].nombre);
  const nombresPuerta = modulos.filter((modulo) => enPuerta.has(modulo.id)).map((modulo) => CATALOGO[modulo.tipo].nombre);
  const ventana = sala.huecos.find((hueco) => hueco.tipo === "ventana");
  const puerta = sala.huecos.find((hueco) => hueco.tipo === "puerta");

  return (
    <div className="app">
      <header>
        <div>
          <p className="marca">React + SVG</p>
          <h1>Planner de cocinas</h1>
        </div>
        <p className="lema">Cada módulo es un dato. El plano y el presupuesto salen de la misma lista.</p>
      </header>
      <div className="cuerpo">
        <aside className="panel">
          <section className="tarjeta resumen">
            <h2>Resumen</h2>
            <p className="precio">{euros.format(cuenta.euros)}</p>
            <dl>
              <div>
                <dt>Piezas</dt>
                <dd>{cuenta.piezas}</dd>
              </div>
              <div>
                <dt>Bajo</dt>
                <dd>{centimetros.format(cuenta.bajo / 100)} m</dd>
              </div>
              <div>
                <dt>Alto</dt>
                <dd>{centimetros.format(cuenta.alto / 100)} m</dd>
              </div>
              <div>
                <dt>Islas</dt>
                <dd>{cuenta.islas}</dd>
              </div>
            </dl>
          </section>

          {nombresSolape.length > 0 ? (
            <p className="aviso" role="status">
              Se pisan: {nombresSolape.join(", ")}. El plano lo pinta igual; el aviso es otra lectura de la lista.
            </p>
          ) : null}
          {nombresPuerta.length > 0 ? (
            <p className="aviso puerta" role="status">
              La puerta no abre: {nombresPuerta.join(", ")}.
            </p>
          ) : null}

          <section className="tarjeta">
            <h2>Sala</h2>
            <div className="campos">
              <label>
                Ancho
                <input
                  type="number"
                  min="260"
                  max="700"
                  step="10"
                  value={sala.ancho}
                  onChange={(evento) => cambiarSala("ancho", Number(evento.target.value))}
                />
                <span>cm</span>
              </label>
              <label>
                Fondo
                <input
                  type="number"
                  min="260"
                  max="700"
                  step="10"
                  value={sala.fondo}
                  onChange={(evento) => cambiarSala("fondo", Number(evento.target.value))}
                />
                <span>cm</span>
              </label>
              <label>
                Ventana
                <input
                  type="number"
                  min="40"
                  max="280"
                  step="10"
                  value={ventana.ancho}
                  onChange={(evento) => cambiarHueco(ventana.id, "ancho", Number(evento.target.value))}
                />
                <span>cm</span>
              </label>
              <label>
                Puerta
                <input
                  type="number"
                  min="60"
                  max="140"
                  step="10"
                  value={puerta.ancho}
                  onChange={(evento) => cambiarHueco(puerta.id, "ancho", Number(evento.target.value))}
                />
                <span>cm</span>
              </label>
            </div>
          </section>

          <section className="tarjeta">
            <h2>Catálogo</h2>
            <div className="catalogo">
              {TIPOS.map((tipo) => (
                <button key={tipo} type="button" onClick={() => agregar(tipo)}>
                  <span className={`muestra ${tipo}`} />
                  {CATALOGO[tipo].nombre}
                  <small>{euros.format(CATALOGO[tipo].precio)}</small>
                </button>
              ))}
            </div>
          </section>

          <section className="tarjeta">
            <h2>Selección</h2>
            {activo ? (
              <>
                <p className="nombre-seleccion">{CATALOGO[activo.tipo].nombre}</p>
                <dl className="dato">
                  <div>
                    <dt>Centro</dt>
                    <dd>
                      {activo.cx} cm, {activo.cy} cm
                    </dd>
                  </div>
                  <div>
                    <dt>Giro</dt>
                    <dd>{activo.giro}°</dd>
                  </div>
                  <div>
                    <dt>Precio</dt>
                    <dd>{euros.format(precioDe(activo))}</dd>
                  </div>
                </dl>
                <label className="ancho">
                  Ancho
                  <select value={activo.ancho} onChange={(evento) => cambiarAncho(Number(evento.target.value))}>
                    {ANCHOS.map((ancho) => (
                      <option key={ancho} value={ancho}>
                        {ancho} cm
                      </option>
                    ))}
                  </select>
                </label>
                <div className="acciones">
                  <button type="button" onClick={girar}>
                    Girar
                  </button>
                  <button type="button" className="peligro" onClick={quitar}>
                    Quitar
                  </button>
                </div>
              </>
            ) : (
              <p className="vacio">Pulsa un módulo del plano o de la lista.</p>
            )}
          </section>

          <section className="tarjeta">
            <h2>La lista</h2>
            <p className="nota">El SVG recorre esta lista. No hay un dibujo aparte.</p>
            <ul className="lista">
              {modulos.map((modulo) => (
                <li key={modulo.id}>
                  <button
                    type="button"
                    className={modulo.id === seleccionado ? "fila activa" : "fila"}
                    onClick={() => setSeleccionado(modulo.id)}
                  >
                    <span>{CATALOGO[modulo.tipo].corto}</span>
                    <span>
                      {modulo.cx},{modulo.cy}
                    </span>
                    <span>{modulo.ancho} cm</span>
                  </button>
                </li>
              ))}
            </ul>
            <button type="button" className="secundario" onClick={reiniciar}>
              Reiniciar plano
            </button>
          </section>
        </aside>
        <main className="lienzo">
          <Plano
            sala={sala}
            modulos={modulos}
            seleccionado={seleccionado}
            solapes={solapes}
            enPuerta={enPuerta}
            onSeleccionar={setSeleccionado}
            onMover={mover}
          />
          <p className="pista">Arrastra un módulo. El centro encaja cada 5 cm y la ficha de la izquierda cambia con él.</p>
        </main>
      </div>
    </div>
  );
}
