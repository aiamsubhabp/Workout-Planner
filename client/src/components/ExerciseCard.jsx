import { useEffect, useState } from 'react'



function ExerciseCard({id, name, muscle_group, image}){




    return (
        <li className='card'>
            <img src = {image} />
            <h4>{name}</h4>
            <h4>{muscle_group}</h4>
            
        </li>
    )
}

export default ExerciseCard