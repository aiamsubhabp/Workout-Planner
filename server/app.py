from config import app, db, api
from flask import Flask, make_response, session, request
from flask_migrate import Migrate
from flask_restful import Resource

from models import User, UserExercise, Exercise

migrate = Migrate(app, db)

class ExerciseList(Resource):
  def get(self):
    exercises = Exercise.query.all()
    exercises_dict = [exercise.to_dict() for exercise in exercises]

    return make_response(exercises_dict, 200)
  
  def post(self):
    data = request.get_json()

    new_exercise = Exercise(
      name = data['name'],
      muscle_group = data['muscle_group']
    )

    try:
      db.session.add(new_exercise)
      db.session.commit()
      return make_response(new_exercise.to_dict(), 201)
    except:
      return make_response('Failed to create new exercise', 400)

  
api.add_resource(ExerciseList, '/api/exercises')


if __name__ == "__main__":
  app.run(port=5555, debug=True)
