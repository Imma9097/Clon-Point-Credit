from flask import Flask, request, jsonify
import bcrypt
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Mock Database
users = {}

# Register User
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    users[data['username']] = hashed_password
    return jsonify({'message': 'User registered successfully!'}), 201

# Login User
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    if username in users and bcrypt.checkpw(password.encode('utf-8'), users[username]):
        token = jwt.encode(
            {'username': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
            app.config['SECRET_KEY'],
            algorithm='HS256'
        )
        return jsonify({'token': token}), 200
    return jsonify({'message': 'Invalid credentials!'}), 401

# Protected Route
@app.route('/protected', methods=['GET'])
def protected():
    token = request.headers.get('Authorization')
    try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return jsonify({'message': f'Welcome {data["username"]}!'}), 200
    except:
        return jsonify({'message': 'Token is invalid or expired!'}), 401

if __name__ == '__main__':
    app.run(debug=True)