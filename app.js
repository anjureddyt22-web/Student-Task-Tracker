// Student Task Tracker - Frontend JavaScript

let tasks = [];

async function fetchTasks() {
    try {
        const response = await fetch('/api/tasks');
        const data = await response.json();
        tasks = data.tasks || [];
        updateStats(data.stats);
        renderTasks();
    } catch (error) {
        console.error('Error fetching tasks:', error);
    }
}

function updateStats(stats) {
    document.getElementById('stat-total').textContent = stats.total || 0;
    document.getElementById('stat-completed').textContent = stats.completed || 0;
    document.getElementById('stat-pending').textContent = stats.pending || 0;
}

function renderTasks() {
    const tasksList = document.getElementById('tasksList');
    const emptyState = document.getElementById('emptyState');
    
    tasksList.innerHTML = '';
    
    if (tasks.length === 0) {
        emptyState.style.display = 'block';
        return;
    }
    
    emptyState.style.display = 'none';
    
    // Sort: pending first, then completed
    const sortedTasks = [...tasks].sort((a, b) => {
        if (a.completed === b.completed) {
            return b.id - a.id;
        }
        return a.completed ? 1 : -1;
    });
    
    sortedTasks.forEach(task => {
        const taskCard = document.createElement('div');
        taskCard.className = 'task-card' + (task.completed ? ' completed' : '');
        taskCard.setAttribute('data-id', task.id);
        
        const taskInfo = document.createElement('div');
        taskInfo.className = 'task-info';
        
        const taskName = document.createElement('div');
        taskName.className = 'task-name';
        taskName.textContent = task.name;
        
        const taskMeta = document.createElement('div');
        taskMeta.className = 'task-meta';
        taskMeta.textContent = `Created: ${task.created_at || 'Unknown'}`;
        
        taskInfo.appendChild(taskName);
        taskInfo.appendChild(taskMeta);
        
        const taskActions = document.createElement('div');
        taskActions.className = 'task-actions';
        
        if (!task.completed) {
            const completeBtn = document.createElement('button');
            completeBtn.className = 'btn btn-success btn-small';
            completeBtn.textContent = 'Complete';
            completeBtn.onclick = () => markComplete(task.id);
            taskActions.appendChild(completeBtn);
        }
        
        const deleteBtn = document.createElement('button');
        deleteBtn.className = 'btn btn-danger btn-small';
        deleteBtn.textContent = 'Delete';
        deleteBtn.onclick = () => deleteTask(task.id);
        taskActions.appendChild(deleteBtn);
        
        taskCard.appendChild(taskInfo);
        taskCard.appendChild(taskActions);
        tasksList.appendChild(taskCard);
    });
}

async function addTask() {
    const taskInput = document.getElementById('taskInput');
    const addTaskMsg = document.getElementById('addTaskMsg');
    const taskName = taskInput.value;
    
    if (!taskName.trim()) {
        addTaskMsg.textContent = 'Please enter a task name';
        addTaskMsg.style.color = 'var(--red-primary)';
        setTimeout(() => {
            addTaskMsg.textContent = '';
        }, 2000);
        return;
    }
    
    try {
        const response = await fetch('/api/tasks', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name: taskName.trim() })
        });
        
        if (response.ok) {
            taskInput.value = '';
            addTaskMsg.textContent = 'Task added successfully!';
            addTaskMsg.style.color = 'var(--green-primary)';
            setTimeout(() => {
                addTaskMsg.textContent = '';
            }, 2000);
            fetchTasks();
        } else {
            const data = await response.json();
            addTaskMsg.textContent = data.error || 'Error adding task';
            addTaskMsg.style.color = 'var(--red-primary)';
            setTimeout(() => {
                addTaskMsg.textContent = '';
            }, 2000);
        }
    } catch (error) {
        console.error('Error adding task:', error);
        addTaskMsg.textContent = 'Error adding task';
        addTaskMsg.style.color = 'var(--red-primary)';
        setTimeout(() => {
            addTaskMsg.textContent = '';
        }, 2000);
    }
}

async function markComplete(taskId) {
    try {
        const response = await fetch(`/api/tasks/${taskId}/complete`, {
            method: 'PUT'
        });
        
        if (response.ok) {
            fetchTasks();
        }
    } catch (error) {
        console.error('Error completing task:', error);
    }
}

async function deleteTask(taskId) {
    if (!confirm('Are you sure you want to delete this task?')) {
        return;
    }
    
    try {
        const response = await fetch(`/api/tasks/${taskId}`, {
            method: 'DELETE'
        });
        
        if (response.ok) {
            fetchTasks();
        }
    } catch (error) {
        console.error('Error deleting task:', error);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    fetchTasks();
    
    const addTaskBtn = document.getElementById('addTaskBtn');
    const taskInput = document.getElementById('taskInput');
    
    addTaskBtn.addEventListener('click', addTask);
    
    taskInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            addTask();
        }
    });
});
