from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple in-memory data (resets when server restarts)
users = {}

@app.route('/')
def home():
    return "Loyalty Card Software Running"

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    name = data.get('name')
    if not name:
        return jsonify({'error': 'Name required'}), 400

    users[name] = {'points': 0}
    return jsonify({'message': f'User {name} added.'})

@app.route('/add_points', methods=['POST'])
def add_points():
    data = request.json
    name = data.get('name')
    points = data.get('points', 0)

    if name not in users:
        return jsonify({'error': 'User not found'}), 404

    users[name]['points'] += points
    return jsonify({'message': f'{points} points added to {name}.'})

@app.route('/get_points', methods=['GET'])
def get_points():
    name = request.args.get('name')

    if name not in users:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({'name': name, 'points': users[name]['points']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
mkdir loyalty-program
cd loyalty-program
npm init -y
npm install express mongoose cors dotenv