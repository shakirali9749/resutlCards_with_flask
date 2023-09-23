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
        # q = "select persons.name, subjects.subject_name, subjects.total_marks, marks.obtained_marks from persons JOIN marks on persons.reg_number = marks.person_id join subjects on marks.subject_id = subjects.subject_id;"
        query = f'select * from persons where roll_number={rollnumber}'
        myresult = execute_query(query)

        person_record = myresult[0]

        registration_number = myresult[0][0]

        query = f'''select subjects.subject_name, subjects.total_marks,
         marks.obtained_marks from subjects join marks ON 
         marks.subject_id=subjects.subject_id and 
         marks.person_id="{registration_number}"'''
        
        subjects_data = execute_query(query)



        
        person_data = {
            'name': person_record[1],
            'registration_number': person_record[0],
            'father_name': person_record[2],
            'roll_number': person_record[3],
            'date_of_birth': person_record[4],
            'subjects_detail': subjects_data
        }


        return render_template("form.html", person=person_data)

    return render_template("form.html")
