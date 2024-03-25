from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db, bcrypt

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique = True, nullable = False)
    _password_hash = db.Column(db.String)

    user_exercises = db.relationship('UserExercise', back_populates = 'user')

    serialize_rules = ('-user_exercises.user',)

    def __repr__(self):
        return f'<User {self.id}, {self.username}>'

class Exercise(db.Model, SerializerMixin):
    __tablename__ = 'exercises'

    # serialize_rules = ('-user_exercises.exercise', '-user_exercises.user')
    serialize_rules = ('-user_exercises',)

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    muscle_group = db.Column(db.String)
    image = db.Column(db.String, default = 'https://banner2.cleanpng.com/20180605/fia/kisspng-barbell-dumbbell-weight-training-physical-fitness-dumbbell-5b16616f58d006.4342646415281933913638.jpg')

    user_exercises = db.relationship('UserExercise', back_populates = 'exercise')

    def __repr__(self):
        return f'<Exercise {self.id}, {self.name}, {self.muscle_group}>'

class UserExercise(db.Model, SerializerMixin):
    __tablename__ = 'user_exercises'

    serialize_rules = ('-user.user_exercises', '-exercise.use_exercises')

    id = db.Column(db.Integer, primary_key = True)
    sets = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    notes = db.Column(db.String, nullable = True)
    date = db.Column(db.DateTime)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))

    user = db.relationship('User', back_populates = 'user_exercises')
    exercise = db.relationship('Exercise', back_populates = 'user_exercises')

     

    def __repr__(self):
        return f'<UserExercise {self.id}, {self.sets}, {self.reps}, {self.user.username}, {self.exercise.name}>'

    