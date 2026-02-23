from flask import Flask, render_template, request, jsonify, make_response, session
app = Flask(__name__)

@app.route('/ciudades')
def consultas():
    import mysql.connector
    mydb = mysql.connector.connect(
      host="46.28.42.226",
      user="u760464709_24005224_usr",
      password="8PEd!gd5x+Sb",
      database="u760464709_24005224_bd"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ciudades")
    myresult = mycursor.fetchall()
    return make_result(justify(myresult))
