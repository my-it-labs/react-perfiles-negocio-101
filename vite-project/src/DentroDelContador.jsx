import { useState } from "react"

const DentroDelContador = ({ nombre, onChange }) => {
    const [count, setCount] = useState(0)

    const handleCountChange = (newCount) => {
        setCount(newCount)
        if (onChange) {
            onChange(newCount)
        }
    }

    return (
        <div>
            <p>Hola, {nombre}!</p>
            <button onClick={() => handleCountChange(count + 1)}>Contar</button>
            <p>Contador: {count}</p>
        </div>
    )
}

export default DentroDelContador