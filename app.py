from flask import Flask, render_template, request, jsonify
from chatbot_logic import chatbot_response
import sqlite3
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    response = chatbot_response(user_input)

    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO chats (question, answer) VALUES (?, ?)", (user_input, response))
    conn.commit()
    conn.close()

    return jsonify({"reply": response})

@app.route("/admin")
def admin():
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM chats")
    data = cursor.fetchall()
    conn.close()
    return render_template("admin.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))