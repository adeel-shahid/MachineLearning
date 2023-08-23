from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.Student import Student
from model.Engine import Engine as e


Session = sessionmaker(bind=e.engine)
session = Session()

class StudentController:


    def createStudent(self,nam,sc,ard,gpa):
        std = Student(name=nam,sec=sc,cgpa=gpa)
        session.add(std)
        session.commit()
        return True


    def GetStudent(self):
        students = session.query(Student).all()
        student_list = [{'id': student.id, 'name': student.name, 'age': student.age} for student in students]
        return jsonify(student_list)