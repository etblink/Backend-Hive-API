from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # Change this to a secure key
jwt = JWTManager(app)

# Sample data to simulate a database
frontends = []
posts = []
users = [{"username": "testuser", "password": "testpassword"}]  # Sample user

@app.route('/')
def home():
    return "Welcome to the Hive Custom Frontend API"

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = next((u for u in users if u["username"] == username and u["password"] == password), None)
    if user:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/create_frontend', methods=['POST'])
@jwt_required()
def create_frontend():
    data = request.json
    frontends.append(data)
    return jsonify({"message": "Frontend created successfully", "frontend": data}), 201

@app.route('/post_update/<int:frontend_id>', methods=['POST'])
@jwt_required()
def post_update(frontend_id):
    if frontend_id >= len(frontends):
        return jsonify({"error": "Frontend not found"}), 404

    data = request.json
    data['frontend_id'] = frontend_id
    posts.append(data)
    return jsonify({"message": "Post created successfully", "post": data}), 201

@app.route('/get_posts/<int:frontend_id>', methods=['GET'])
@jwt_required()
def get_posts(frontend_id):
    if frontend_id >= len(frontends):
        return jsonify({"error": "Frontend not found"}), 404

    frontend_posts = [post for post in posts if post['frontend_id'] == frontend_id]
    return jsonify({"posts": frontend_posts}), 200

if __name__ == '__main__':
    app.run(debug=True)
