import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__)

def execute_query(query):
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="shakir89",
      database='sourceCode'
    )

    mycursor = mydb.cursor()
    mycursor.execute(query)

    myresult = mycursor.fetchall()

    return myresult


@app.route("/", methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        rollnumber = request.form.get('rollnumber')
        print(f'rollnumber: {rollnumber}')
        # breakpoint()
    q = "select persons.name, subjects.subject_name, subjects.total_marks, marks.obtained_marks from persons JOIN marks on persons.reg_number = marks.person_id join subjects on marks.subject_id = subjects.subject_id;"
    myresult = execute_query(q)

    data = []
    for x in myresult:
      data.append(list(x))


    return render_template("form3.html", persons=data)
