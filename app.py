from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
host = "10.2.2.211",
user = "Max@%",
password = "AX-d120",
database = "player_scores",
charset = "utf8mb4",
collation = "utf8mb4_general_ci"
)

#mycursor = mydb.cursor()

#def function_db():
 #   conn = get_connection()
  #  cursor = conn.cursor()
   # cursor.execute('''
    #    CREATE TABLE IF NOT EXISTS scores (
     #       id INT AUTO_INCREMENT PRIMARY KEY,
      #      player_name VARCHAR(255) NOT NULL,
       #     score INTE NOT NULL
        #)
    #''')
    #conn.commit()
    #ursor.close()
    #conn.close()

#function_db()


@app.route('/save-score', methods=['POST'])
def save_score():
    data = request.json
    player_name = data['player_name']
    score = data['score']


    mycursor = mydb.cursor()
    sql = "INSERT INTO scores (player_name, score) VALUES (%s, %s)"
    val = (player_name, score)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()

    return jsonify({"message": "Score saved"}), 201


@app.route('/')
def index():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT player_name, score FROM scores ORDER BY score DESC LIMIT 10")
    scores = mycursor.fetchall()
    mycursor.close()

    return render_template('index.html', scores = scores)

if __name__ == '__main__':
    app.run(debug=True)


#1. lag en variabel mydb av typen mysql.connector.connect(INFO)
#2. lag en "cursor" for å kunne kjøre sql. mydb.cursor() 
#3. mycursor.execute(sql)
#4. mydb.commit()