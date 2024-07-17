from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data to simulate a database
frontends = []
posts = []

@app.route('/')
def home():
    return "Welcome to the Hive Custom Frontend API"

# Endpoint to create a new custom frontend
@app.route('/create_frontend', methods=['POST'])
def create_frontend():
    data = request.json
    frontends.append(data)
    return jsonify({"message": "Frontend created successfully", "frontend": data}), 201

# Endpoint to post updates to a specific frontend
@app.route('/post_update/<int:frontend_id>', methods=['POST'])
def post_update(frontend_id):
    if frontend_id >= len(frontends):
        return jsonify({"error": "Frontend not found"}), 404

    data = request.json
    data['frontend_id'] = frontend_id
    posts.append(data)
    return jsonify({"message": "Post created successfully", "post": data}), 201

# Endpoint to get all posts for a specific frontend
@app.route('/get_posts/<int:frontend_id>', methods=['GET'])
def get_posts(frontend_id):
    if frontend_id >= len(frontends):
        return jsonify({"error": "Frontend not found"}), 404

    frontend_posts = [post for post in posts if post['frontend_id'] == frontend_id]
    return jsonify({"posts": frontend_posts}), 200

if __name__ == '__main__':
    app.run(debug=True)
