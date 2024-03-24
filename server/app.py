from config import app, db, api
from models import User, UserExercise, Exercise
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Resource

migrate = Migrate(app, db)


if __name__ == "__main__":
  app.run(port=5555, debug=True)
