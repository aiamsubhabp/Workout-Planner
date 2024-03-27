from config import app, db, api
from flask import Flask, make_response, session, request, jsonify
from flask_migrate import Migrate
from flask_restful import Resource

from models import User, UserExercise, Exercise

migrate = Migrate(app, db)

@app.route('/')
def index():
  return '<h1>Workout Tracker Api</h1>'

class Users(Resource):
  def get(self):
    users = User.query.all()
    users_dict = [user.to_dict() for user in users]

    return users_dict, 200
  
  def post(self):
    data = request.get_json()

    new_user = User(
      username = data['username'],
      _password_hash = data['_password_hash']
    )

    try:
      db.session.add(new_user)
      db.session.commit()
      return new_user.to_dict(), 201
    except:
      response = 'Failed to create new user', 400
      return response

api.add_resource(Users, '/api/users')

class Exercises(Resource):
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

api.add_resource(Exercises, '/api/exercises')

class ExerciseById(Resource):
  def get(self, id):
    exercise = Exercise.query.filter(Exercise.id == id).first()
    if not exercise:
      return make_response('Exercise not found', 404)
    
    exercise_dict = exercise.to_dict()

    return make_response(jsonify(exercise_dict), 200)
  
  def patch(self, id):
    exercise = Exercise.query.filter(Exercise.id == id).first()
    if not exercise:
      return make_response('Exercise not found', 404)
    
    try:
      data = request.get_json()
      for attr in data:
        setattr(exercise, attr, data[attr])
      db.session.add(exercise)
      db.session.commit()
      return make_response(exercise.to_dict(), 202)
    except:
      return make_response('Failed to update exercise', 400)
    
  def delete(self, id):
    exercise = Exercise.query.filter(Exercise.id == id).first()
    if not exercise:
      return make_response('Exercise not found', 404)      
    
    db.session.delete(exercise)
    db.session.commit()

    return make_response("Exercise sucessfully deleted", 204)
  
api.add_resource(ExerciseById, '/api/exercises/<int:id>')

if __name__ == "__main__":
  app.run(port=5555, debug=True)
