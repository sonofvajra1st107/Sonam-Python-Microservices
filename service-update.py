from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
# import jwt
import data_user as us

app = Flask(__name__)

@app.route('/update', methods=['PUT'])
def register():
    # Get the user's login information from the request
    user = request.form.get('username')
    passwd = request.form.get('password')
    name = request.form.get('name')

    _user = us.user_name()
    data = [x for x in _user if x["user"]==user]
    # return jsonify(_user)
    #Get Data
    if data:
        us.update_user(user,passwd,name)
        return jsonify({'message': 'Update successfully.'}), 200
    else:
        return jsonify({'message': 'Cannot update user.'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True) #127.0.0.1