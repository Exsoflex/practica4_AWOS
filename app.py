from flask import Flask, render_template, report, justify, make_response, session
app = Flask(__name__)

@app.route('/ciudades')
def consultas():
    import mysql.connector
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="clima_app"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ciudades")
    myresult = mycursor.fetchall()
    return make_result(justify(myresult))
