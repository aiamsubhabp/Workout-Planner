from config import app, db, api
from models import User, UserExercises, Exercise
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Resource


if __name__ == "__main__":
  app.run(port=5555, debug=True)
