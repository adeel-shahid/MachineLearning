from flask import Flask,jsonify
# app = Flask(__name__)
# @app.route('/Student/<string:name>')
# def welcome(name):
#     dict = {
#         "name" : name,
#         "Program" : "BSCS-7",
#         "id":"2020-arid-3593"
#     }
#     return jsonify(dict)
#
# if __name__ == '__main__':
#     app.run(debug=True)

#################################################
#Task
app = Flask(__name__)
# dict = {
#         "2020-arid-3593" : {
#             "name" : "Adeel",
#             "Section" : "D"
#         },
#         "2020-arid-3634" : {
#             "name" : "Hamid",
#             "Section" : "A"
#         },
#         "2020-arid-3639": {
#             "name": "Usama",
#             "Section": "C"
#         }
# }
student=[
    {
        "id" : "arid-1",
        "name" : "Adeel",
        "Section" : "D"
    },{
        "id" : "arid-2",
        "name" : "Anees",
        "Section" : "C"
    },{
        "id" : "arid-3",
        "name" : "Usama",
        "Section" : "B"
    },{
        "id" : "arid-4",
        "name" : "Abdullah",
        "Section" : "A"
    }
]


@app.route("/GetAll")
def GetAllStudent():
    return jsonify(student)


@app.route("/GetStd/<string:arid>")
def GetStudent(arid):
    for s in student:
        if s["id"] == arid:
            return jsonify(s)
    return "Student not Found"

if __name__ == '__main__':
    app.run()