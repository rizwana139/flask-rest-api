from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store
users = {}

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# GET a single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# POST a new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user_id = data.get('id')
    if user_id in users:
        return jsonify({"error": "User already exists"}), 400
    users[user_id] = {
        "name": data.get("name"),
        "email": data.get("email")
    }
    return jsonify({"message": "User added successfully"}), 201

# PUT to update an existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    users[user_id].update({
        "name": data.get("name"),
        "email": data.get("email")
    })
    return jsonify({"message": "User updated successfully"})

# DELETE a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted successfully"})
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)