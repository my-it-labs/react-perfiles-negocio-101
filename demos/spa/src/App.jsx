import { useState } from "react";
import { lineas } from "./datos.js";
import { TarjetaLinea } from "./components/TarjetaLinea.jsx";

export function App() {
  const [vista, setVista] = useState("listado");
  const [lineaId, setLineaId] = useState(null);
  const linea = lineas.find((item) => item.id === lineaId);


  const nuevaLineaHandler = () => {
    lineas.push({
      id: `L${lineas.length + 1}`,
      nombre: `Linea ${lineas.length + 1}`,
      detalle: `Detalle de la linea ${lineas.length + 1}`,
      estado: "activa",
    });
    setVista("listado");  
  }

  return (
    <>
      <header>
        <p className="marca">SPA React</p>
        <h1>{vista === "detalle" && linea ? `Detalle de ${linea.id}` : "Red de transporte"}</h1>
        <p>Cambiar de vista no recarga el documento.</p>
      </header>
      <main>
        <button onClick={nuevaLineaHandler}>Agrega Linea</button>
        <p>
          Cargas del documento: <strong>1</strong>
        </p>
        {vista === "listado" ? (
          lineas.map((item) => (
            <TarjetaLinea
              key={item.id}
              nombre={item.nombre}
              estado={item.estado}
              onVerDetalle={
                item.id === "L1"
                  ? () => {
                      setLineaId(item.id);
                      setVista("detalle");
                    }
                  : undefined
              }
            />
          ))
        ) : (
          <>
            <article>
              <h2>{linea.nombre}</h2>
              <p>{linea.detalle}</p>
              <p>Estado: {linea.estado}</p>
            </article>
            <p>
              <button
                onClick={() => {
                  setVista("listado");
                  setLineaId(null);
                }}
              >
                Volver al listado
              </button>
            </p>
          </>
        )}
      </main>
    </>
  );
}
