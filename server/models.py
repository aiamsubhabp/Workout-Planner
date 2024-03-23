from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db, bcrypt

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique = True, nullable = False)
    _password_hash = db.Column(db.String)

    def __repr__(self):
        return f'<User {self.id}, {self.username}>'

class Exercise(db.Model, SerializerMixin):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    muscle_group = db.Column(db.String)

    def __repr__(self):
        return f'<User {self.id}, {self.name}, {self.muscle_group}>'

class UserExercises(db.Model, SerializerMixin):
    __tablename__ = 'user_exercises'

    id = db.Column(db.Integer, primary_key = True)
    sets = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    notes = db.Column(db.String, nullable = True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))

    