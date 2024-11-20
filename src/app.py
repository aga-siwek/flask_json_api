from flask import Flask, request, jsonify
import json_connection as data_connection

app = Flask(__name__)


@app.route("/")
def hello_world():
    return jsonify({"response":f"Home page"})


@app.route("/register/", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        post_data = request.json
        user_name = post_data["user"]
        user_password = post_data["password"]
        if data_connection.register(user_name, user_password):
            return jsonify({"response":f"Hi {user_name} you are added to database"})
        else:
            return jsonify({"response": f"Hi {user_name} you are in database, you should login"})
    else:
        return jsonify({"response":f"Register page"})


@app.route("/login/", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        post_data = request.json
        user_name = post_data["user"]
        user_password = post_data["password"]
        if data_connection.login(user_name, user_password):
            return jsonify({"response": f"Hi {user_name} you are log in"})
        else:
            return jsonify({"response": "Wrong user or password"})


    return jsonify({"response":"login page"})


@app.route("/tasks/", methods=['GET', 'POST', 'DELETE'])
def tasks():
    return "<p>Add task, see tasks, delete task</p>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
