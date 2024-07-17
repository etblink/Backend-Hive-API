# Hive Custom Frontend API

This is a proof-of-concept backend API for creating customizable niche frontends on the Hive blockchain. The API allows users to create custom frontends, post updates, and interact with content. The goal is to provide a platform for brands, content creators, and companies to easily create and manage their own frontends with custom tokens, algorithms, and styles.

## Features

- Create a new custom frontend
- Post updates to a specific frontend
- Retrieve posts for a specific frontend

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Postman (for testing API endpoints)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/hive-custom-frontend.git
   cd hive-custom-frontend
   
2. Create a virtual environment:  
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install dependencies:
   ```bash
   pip install flask flask-jwt-extended

### Running the Application

#### Create a New Frontend
- URL: `/create_frontend`
- Method: `POST`
- Headers: `Content-Type: application/json`
- Body:
  ```json
  {
  "name": "4th Street Bar"
  }
- Response:
  ```json
  {
    "message": "Frontend created successfully",
    "frontend": {
      "name": "4th Street Bar"
    }
  }

#### Post an Update
- URL: `/post_update/<int:frontend_id>`
- Method: `POST`
- Headers: `Content-Type: application/json`
- Body:
  ```json
  {
  "content": "Happy Hour Specials!"
  }
- Response:
  ```json
  {
    "message": "Post created successfully",
    "post": {
      "frontend_id": 0,
      "content": "Happy Hour Specials!"
    }
  }

#### Get Posts for a Frontend
- URL: `/get_posts/<int:frontend_id>`
- Method: `GET`
- Response:
  ```json
  {
    "posts": [
      {
        "frontend_id": 0,
        "content": "Happy Hour Specials!"
      }
    ]
  }

### Authentication
Currently, the API uses JWT-based authentication to secure endpoints. To use the authenticated endpoints, follow these steps:
#### Login
- URL: `/login`
- Method: `POST`
- Headers: `Content-Type: application/json`
- Body:
  ```json
  {
    "username": "testuser",
    "password": "testpassword"
  }
- Response:
  ```json
  {
    "access_token": "<your_jwt_token>"
  }

 #### Authenticated Requests
 For endpoints that require authentication (`/create_frontend`, `/post_update`, `/get_posts`), add an `Authorization` header with the JWT token received from the login endpoint:
- Header: `Authorization: Bearer <your_jwt_token>`

## Contributing
We welcome contributions! Please open an issue or submit a pull request.
