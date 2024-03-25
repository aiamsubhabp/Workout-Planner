import { useEffect, useState } from 'react'



function ExerciseCard({id, name, muscle_group}){




    return (
        <div>
            <h1>{name}</h1>
            <h1>{muscle_group}</h1>
        </div>
    )
}

export default ExerciseCard