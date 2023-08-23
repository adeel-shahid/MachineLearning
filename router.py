from flask import Flask, jsonify
from controller.StudentController import StudentController
app = Flask(__name__)


@app.route("/GetStudents")
def GetStudents():
    controller.GetStudent()


if __name__ == '__main__':
    app.run(debug=True)