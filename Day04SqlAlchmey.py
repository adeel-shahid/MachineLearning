#Code First Approach
# from flask import Flask, jsonify
# import sqlalchemy as db
# from sqlalchemy.orm import sessionmaker,declarative_base

# app = Flask(__name__)
# #Creating SQLaAlchemy Engine
# engine = db.create_engine("sqlite:///students.sqlite")
# #Handle Data of db in memory
# session = sessionmaker(bind=engine)
# #its a base class from which each model is derived
# base = declarative_base()
#
# class Student(base):
#     id=db.column(db.INT,primary_Key=True)
#     name=db.column(db.String(100))
#
# with Session() as session:
#     session.add(Student)
#     session.commit()
#
# @app.route("/GetAll")
# def GetAllStudent():
#     return jsonify(student)
#
#
# @app.route("/GetStd/<string:arid>")
# def GetStudent(arid):
#     for s in student:
#         if s["id"] == arid:
#             return jsonify(s)
#     return "Student not Found"
#
# if __name__ == '__main__':
#     app.run(debug=True)
####################################################################
from flask import Flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy as db

from sqlalchemy.ext.declarative import declarative_base

# Create a Flask app
app = Flask(__name__)

# Create a SQLite database engine
engine = create_engine("sqlite:///studentdb.db", echo=True)

# Create a session factory
Session = sessionmaker(bind=engine)
session = Session()

# Create a base class for declarative models
Base = declarative_base()


# Define your models here
class Student(Base):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)

std = Student(name="Adeel Shahid",age=22)
session.add(std)
session.commit()
# Create the database tables
Base.metadata.create_all(engine)


# Route to get student data
@app.route('/students', methods=['GET'])
def get_students():
    students = session.query(Student).all()
    student_list = [{'id': student.id, 'name': student.name, 'age': student.age} for student in students]
    return jsonify(student_list)

if __name__ == '__main__':
    app.run()
