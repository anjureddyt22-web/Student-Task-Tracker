from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, 'r', encoding='utf-8') as file:
                tasks = json.load(file)
                return tasks
        except (json.JSONDecodeError, IOError):
            return []
    else:
        return []

def save_tasks(tasks):
    try:
        with open(TASKS_FILE, 'w', encoding='utf-8') as file:
            json.dump(tasks, file, indent=4, ensure_ascii=False)
        return True
    except IOError:
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = load_tasks()
    total = len(tasks)
    completed = sum(1 for t in tasks if t.get('completed', False))
    pending = total - completed
    return jsonify({
        'tasks': tasks,
        'stats': {
            'total': total,
            'completed': completed,
            'pending': pending
        }
    })

@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task_name = data.get('name', '').strip() if data else ''
    if not task_name:
        return jsonify({'error': 'Task name cannot be empty'}), 400
    
    tasks = load_tasks()
    if tasks:
        task_id = max(task['id'] for task in tasks) + 1
    else:
        task_id = 1
    
    new_task = {
        "id": task_id,
        "name": task_name,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(new_task)
    if save_tasks(tasks):
        return jsonify(new_task), 201
    else:
        return jsonify({'error': 'Failed to save task'}), 500

@app.route('/api/tasks/<int:task_id>/complete', methods=['PUT'])
def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            if save_tasks(tasks):
                return jsonify(task)
            else:
                return jsonify({'error': 'Failed to save task'}), 500
    return jsonify({'error': 'Task not found'}), 404

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            deleted_task = tasks.pop(i)
            if save_tasks(tasks):
                return jsonify(deleted_task)
            else:
                return jsonify({'error': 'Failed to save task'}), 500
    return jsonify({'error': 'Task not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
