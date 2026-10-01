import { useReducer, useState } from "react"
import DentroDelContador from "./DentroDelContador"

const MiComponente = ({ nombre }) => {
    const [count, setCount] = useState(0)
    useReducer()



    return (
        <div>
            <p>Hola, {nombre}!</p>
            <p>Contador: {count}</p>
            <DentroDelContador nombre={nombre} onChange={setCount} />
        </div>
    )
}

export default MiComponente