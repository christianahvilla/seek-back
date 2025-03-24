# 🐍 Seek-Back – Flask Task Management API

Seek-Back is a modular and lightweight Task Management REST API, built using Python + Flask, secured with JWT authentication, and prepared for seamless integration with a React/Vite frontend.

## 🚀 Features

- Secure user authentication via JWT
- Full task management (Create, Read, Update, Delete)
- Modular architecture using Flask Blueprints
- CORS support for frontend-backend integration
- Swagger UI for interactive API documentation
- Unit testing using Flask-Testing + Unittest
- AWS integration ready via Boto3
- Environment configuration using Dotenv
- Docker support for deployment
- DynamoDB (NoSQL Database)

## 🧰 Tech Stack

- Python 3.10+
- Flask 2.3.2
- Flask-JWT-Extended
- Flask-CORS
- Flask-Swagger-UI
- Boto3 (AWS SDK)
- python-dotenv
- Flask-Testing / Unittest

## 📁 Project Structure

seek-back/
|── models/
│   └── user.py
│   └── task.py
├── routes/
│   ├── auth.py
│   └── task.py
├── tests/
│   └── test_tasks.py
│   └── test_auth.py
├── .env
├── app.py
├── create_tables.py
├── requirements.txt
└── README.md

## 🔐 API Endpoints

Method | Route            | Description                | Auth Required
-------|------------------|----------------------------|---------------
POST   | /register        | Register a new user        | No
POST   | /login           | Log in and receive JWT     | No
GET    | /tasks           | Retrieve all tasks         | Yes
POST   | /tasks           | Create a new task          | Yes
PUT    | /tasks/<id>      | Update task by ID          | Yes
DELETE | /tasks/<id>      | Delete task by ID          | Yes

To access protected routes, include this header in your requests:
Authorization: Bearer <your_jwt_token>

## 📄 Swagger Documentation

If Swagger UI is enabled, you can access interactive API documentation at:
http://localhost:5000/api/docs

You can customize or register the Swagger JSON path in main.py.

## ⚙️ Environment Variables

Create a .env file inside the seek-back/ directory with the following content:

JWT_SECRET_KEY=your-super-secret-key

## ▶️ Run the Project Locally

1. Clone the repository:
git clone https://github.com/christianahvilla/seek-back.git
cd seek-back

2. Install dependencies:
pip install -r requirements.txt

3. Start the Flask server:
python app.py

The API will be available at: http://localhost:5000

## 🧪 Run Tests

To execute the test suite:
python -m unittest discover tests

Tests are written using unittest and Flask-Testing.

## 🐳 Docker Deployment (Optional)

1. Build the Docker image:
docker build -t seek-back .

2. Run the container:
docker run -p 5000:5000 seek-back

The API will now be available at: http://localhost:5000

## 📦 Requirements

Flask==2.3.2  
flask-jwt-extended==4.5.2  
boto3==1.28.62  
python-dotenv==1.0.0  
flask-swagger-ui==4.11.1  
flask-cors==4.0.0  
flask-testing==0.8.1

You can install them using:
pip install -r requirements.txt

## ☁️ AWS DynamoDB Integration

This project uses DynamoDB as the main data storage engine. Make sure your AWS credentials are valid and have permission to access the target table.

- Tasks and users are stored and retrieved from the DynamoDB table.
- You can configure the table name and AWS region in the .env file.
- All access is managed using Boto3's DynamoDB client.


## 👨‍💻 Author

Christian Herrejon / GitHub: https://github.com/christianahvilla

