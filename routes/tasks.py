from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from models.task import create_task, get_tasks, get_task, update_task, delete_task
import uuid

task_routes = Blueprint('tasks', __name__)

@task_routes.route('/tasks', methods=['POST'])
@jwt_required()
def create_new_task():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    status = data.get('status', 'todo')
    if not title or not description:
        return jsonify({"message": "Title and description are required"}), 400
    task_id = str(uuid.uuid4())
    create_task(task_id, title, description, status)
    return jsonify({"task_id": task_id}), 201

@task_routes.route('/tasks', methods=['GET'])
@jwt_required()
def get_all_tasks():
    tasks = get_tasks()
    
    cleaned_tasks = []
    for task in tasks:
        cleaned_tasks.append({
            "id": task["PK"].split("#")[1], 
            "title": task.get("title"),
            "description": task.get("description"),
            "status": task.get("status")
        })

    return jsonify(cleaned_tasks), 200

@task_routes.route('/tasks/<task_id>', methods=['GET'])
@jwt_required()
def get_single_task(task_id):
    task = get_task(task_id)
    if not task:
        return jsonify({"message": "Task not found"}), 404

    cleaned_task = {
        "id": task_id,
        "title": task.get("title"),
        "description": task.get("description"),
        "status": task.get("status")
    }

    return jsonify(cleaned_task), 200

@task_routes.route('/tasks/<task_id>', methods=['PUT'])
@jwt_required()
def update_existing_task(task_id):
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    status = data.get('status')

    update_task(task_id, title, description, status)

    updated_task = get_task(task_id)
    if not updated_task:
        return jsonify({"message": "Task not found"}), 404

    cleaned_task = {
        "id": task_id,
        "title": updated_task.get("title"),
        "description": updated_task.get("description"),
        "status": updated_task.get("status")
    }

    return jsonify(cleaned_task), 200


@task_routes.route('/tasks/<task_id>', methods=['DELETE'])
@jwt_required()
def delete_existing_task(task_id):
    delete_task(task_id)
    return jsonify({"message": "Task deleted successfully"}), 200