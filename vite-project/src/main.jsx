import { createRoot } from 'react-dom/client'
import './index.css'
import MiComponente from './MiComponente.jsx'

const contadores = ["juan", "maria", "pedro", "luis", "ana"]


createRoot(document.getElementById('root')).render(
    <>
      {contadores.map((nombre) => (
        <MiComponente nombre={nombre} onChange={(count) => console.log(`${nombre} changed count to ${count}`)} />
      ))}
    </>
)
