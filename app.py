from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)


def function_db():
    conn = sqlite3.connect("scores.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_name TEXT NOT NULL,
            score INTEGER NOT NULL
        )
    ''')
    conn.commit
    conn.close

function_db()


@app.route('/save-score', methods=['POST'])
def save_score():
    data = request.json
    player_name = data['player_name']
    score = data['score']

    conn = sqlite3.connect("scores.db")
    c = conn.cursor()
    c. execute("INSERT INTO scores (player_name, score) VALUES (?, ?)", (player_name, score))
    conn.commit()
    conn.close()

    return jsonify({"message": "Score saved"}), 201


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)