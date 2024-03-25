import { useEffect, useState } from 'react'
import ExerciseCard from './ExerciseCard'



function ExercisePage({exercises}){
    const exerciseList = exercises.map(exercise => (
        <ExerciseCard
            key={exercise.id}
            name={exercise.name}
            muscle_group={exercise.muscle_group} 
            image = {exercise.image}
        />
    ))
    return (
        <ul className='cards'>
            {exerciseList}
        </ul>
    )
}

export default ExercisePage