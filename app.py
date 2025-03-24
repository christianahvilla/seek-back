from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS 
from routes.auth import auth_routes
from routes.tasks import task_routes

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600  # 1 hour in seconds
jwt = JWTManager(app)

CORS(app)

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json' 

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seek API"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

app.register_blueprint(auth_routes)
app.register_blueprint(task_routes)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Task Manager API!"}), 200

if __name__ == '__main__':
    app.run(debug=True)