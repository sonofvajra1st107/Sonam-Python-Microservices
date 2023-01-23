from flask import Flask, request, jsonify
import datetime
import data_user as us

app = Flask(__name__)

username = us.user_name()




@app.route('/delete/<user>', methods=['DELETE'])
def delete(user):
    # Get the user's login information from the request
    _user = us.find_username(user)
    data = [x for x in _user if x["user"]==user]
    if data:
        us.delete_user(user)
        return jsonify({'message': 'User deleted successfully.'}), 200
    else:
        return jsonify({'message': 'User not found.'}), 404   


if __name__=='__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)