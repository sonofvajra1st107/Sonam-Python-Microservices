from flask import Flask, request, jsonify
import datetime
import data_user as us

app = Flask(__name__)

# Find data in json
def find_user(user, username):
    data = [x for x in username if x["user"]==user]
    return data

@app.route('/login', methods=['POST'])
def login():
    try:
        # Get the user's login information from the request
        username = request.form.get('username')
        password = request.form.get('password')

        _user = us.find_username(username)
        data = [x for x in _user if x["user"]==username and x["password"]==password]
        #Get Data
        if (data):
            return jsonify({'message': 'Login successfully.'}), 200
        else:
            return jsonify({'message': 'Cannot Login.'}), 401
    except:
            return jsonify({'message': 'user not found.'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True) #127.0.0.1