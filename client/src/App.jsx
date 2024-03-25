import { useEffect, useState } from 'react'
import ExercisePage from './components/ExercisePage'
import './App.css'

function App() {
  const [exercises, setExercises] = useState([])

  useEffect(() => {
    fetch('/api/exercises')
      .then(r => r.json())
      .then (data => setExercises(data))
  }, [])

  return (
    <div className='app'>
      <ExercisePage exercises = {exercises}/>

    </div>
  )
}

export default App
