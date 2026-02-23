from flask import Flask
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
    return myresult
