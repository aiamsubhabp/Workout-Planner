from config import app, db
from models import User, UserExercise, Exercise
import datetime

if __name__ == "__main__":
  with app.app_context():
    print('Deleting all records...')
    UserExercise.query.delete()
    User.query.delete()
    Exercise.query.delete()

    print('Seeding data in process...')
    
    u1 = User(username = 'mike_tyson')
    u1.password_hash = 'password1'

    u2 = User(username = 'brad_pitt')
    u2.password_hash = 'password2'
    
    u3 = User(username = 'KingKong')
    u3.password_hash = 'password3'

    db.session.add_all([u1, u2, u3])
    db.session.commit()

    e1 = Exercise(name = 'push-ups', muscle_group = 'triceps, chest', image = 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Man_Doing_Push_Ups_Cartoon.svg/1024px-Man_Doing_Push_Ups_Cartoon.svg.png')
    e2 = Exercise(name = 'pull-ups', muscle_group = 'back', image = 'https://banner2.cleanpng.com/20180528/qaq/kisspng-chin-up-pull-up-exercise-biceps-weight-training-pull-up-5b0c9456854b48.727682571527551062546.jpg')
    e3 = Exercise(name = 'overhead press', muscle_group = 'shoulders', image = 'https://us.123rf.com/450wm/lawangdesign/lawangdesign2111/lawangdesign211100036/177688817-athletic-boy-lifting-weights-on-white-background.jpg?ver=6')
    e4 = Exercise(name = 'squats', muscle_group = 'legs')
    e5 = Exercise(name = 'bench press', muscle_group = 'chest')
    e6 = Exercise(name = 'deadlift', muscle_group = 'legs, lower back')
    e7 = Exercise(name = 'shoulder press', muscle_group = 'shoulders')
    e8 = Exercise(name = 'bicep curls', muscle_group = 'biceps')
    e9 = Exercise(name = 'tricep extensions', muscle_group = 'triceps')
    e10 = Exercise(name = 'lateral raises', muscle_group = 'shoulders')


    db.session.add_all([e1, e2, e3, e4, e5, e6, e7, e8, e9, e10])
    db.session.commit()
    
    u1_e4 = UserExercise(sets = 5, reps = 5, user = u1, exercise = e4, date = datetime.datetime(2024, 3, 24))
    u1_e5 = UserExercise(sets = 5, reps = 5, user = u1, exercise = e5, date = datetime.datetime(2024, 3, 24))
    u1_e6 = UserExercise(sets = 5, reps = 5, user = u1, exercise = e6, date = datetime.datetime(2024, 3, 24))

    db.session.add_all([u1_e4, u1_e5, u1_e6])

    u2_e5 = UserExercise(sets = 3, reps = 10, user = u2, exercise = e5, date = datetime.datetime(2024, 3, 24))
    u2_e1 = UserExercise(sets = 5, reps = 20, user = u2, exercise = e1, date = datetime.datetime(2024, 3, 24))
    u2_e9 = UserExercise(sets = 5, reps = 10, user = u2, exercise = e9, date = datetime.datetime(2024, 3, 24))

    db.session.add_all([u2_e1, u2_e5, u2_e9])

    u3_e2 = UserExercise(sets = 3, reps = 10, user = u3, exercise = e2, date = datetime.datetime(2024, 3, 24))
    u3_e3 = UserExercise(sets = 3, reps = 10, user = u3, exercise = e3, date = datetime.datetime(2024, 3, 24))
    u3_e8 = UserExercise(sets = 3, reps = 10, notes = 'need big arms', user = u3, exercise = e8, date = datetime.datetime(2024, 3, 24))
    u3_e9 = UserExercise(sets = 3, reps = 10, user = u3, exercise = e9, date = datetime.datetime(2024, 3, 24))

    db.session.add_all([u3_e8, u3_e2, u3_e3, u3_e9])
    db.session.commit()
    
    print('Seeding complete')

