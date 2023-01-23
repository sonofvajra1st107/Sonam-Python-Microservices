from flask import Flask, request, jsonify
import datetime
import data_user as us

app = Flask(__name__)


@app.route('/username', methods=['GET'])
def user():
    _user = us.user_name()
    return jsonify(_user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True) #127.0.0.1