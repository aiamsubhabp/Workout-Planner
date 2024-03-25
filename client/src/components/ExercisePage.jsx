import { useEffect, useState } from 'react'
import ExerciseCard from './ExerciseCard'



function ExercisePage({exercises}){
    const exerciseList = exercises.map(exercise => (
        <ExerciseCard
            key={exercise.id}
            name={exercise.name}
            muscle_group={exercise.muscle_group} 
        />
    ))
    return (
        <div>
            {exerciseList}
        </div>
    )
}

export default ExercisePage