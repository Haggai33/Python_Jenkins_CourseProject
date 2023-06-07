import requests
from flask import Flask, render_template
from db_connector import DBConnector
from flask import Flask, jsonify
from flask import Flask, request
import os
import signal


host = 'sql.freedb.tech'
port = 3306
user = 'freedb_haggai'
password = '7p8Gc!Ycp!MB?%A'
database = "freedb_users_10"


# initialize the DBConnector class
db = DBConnector(host, port, user, password, database)

# initialize the Flask (constructor)
app = Flask(__name__)

# returns the userName from the MySQL DB by the given user id
# and show him in a html template


@app.route('/users/get_user_name/<user_id>')
def get_user_name(user_id):
    user_name = db.get_user_name(user_id)
    if request.method == 'GET':
        try:
            user_name = db.get_user_name(user_id)
            return "<h1 id='user_name'>" + user_name + "</h1>"
        except Exception as e:
            return "<h1 id='error'>" + "no such user" "</h1>"


@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'server stopped'


print()

app.run(host='127.0.0.1', debug=True, port=5001)

