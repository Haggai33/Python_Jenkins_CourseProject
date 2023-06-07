from flask import Flask, request, jsonify
from db_connector import DBConnector
import pymysql
import datetime
import backend_testing
import os
import signal
# Constants

host = 'sql.freedb.tech'
port = 3306
user = 'freedb_haggai'
password = '7p8Gc!Ycp!MB?%A'
database = 'freedb_users_10'


# initialize the DBConnector class
db = DBConnector(host, port, user, password, database)

# Flask App
app = Flask(__name__)


@app.route('/data/<user_id>', methods=['GET'])
def get_user_name(user_id):
    # Get User
    user_name = db.get_user_name(user_id)

    if user_name is None:
        return jsonify({'status': 'error', 'reason': 'no such id'}), 500
    else:
        return jsonify({'status': 'ok', 'user_name': user_name}), 200
    # POST


@app.route('/data/<user_id>', methods=['POST'])
def adduser(user_id):
    user_name = request.json.get("user_name")
    if user_name is None:
        return jsonify({'status': 'error', 'reason': 'there is no such user'}), 400
    if db.get_user_name(user_id) is not None:
        return jsonify({'status': 'error', 'reason': 'id already exists'}), 500
    db.adduser(user_id, user_name)
    return jsonify({'status': 'ok', 'user_added': user_name}), 200

    # Update user


@app.route('/data/<user_id>', methods=['PUT'])
def update_user(user_id):
    user_name = request.json.get('user_name')
    if user_name is None:
        return jsonify({'status': 'error', 'reason': 'there is no user_name'}), 400

    if db.get_user_name(user_id) is None:
        return jsonify({'status': 'error', 'reason': 'no such id'}), 500

    db.update_user_name(user_id, user_name)
    return jsonify({'status': 'ok', 'user_updated': user_name}), 200


@app.route('/data/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if db.get_user_name(user_id) is None:
        return jsonify({'status': 'error', 'reason': 'no such id'}), 500
    db.delete_user(user_id)
    return jsonify({'status': 'ok', 'user_deleted': user_id}), 200


@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'server stopped'


app.run(host='127.0.0.1', debug=True, port=5000)

