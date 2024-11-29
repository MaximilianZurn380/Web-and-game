from flask import Flask, request, jsonify
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