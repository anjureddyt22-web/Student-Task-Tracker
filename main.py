import json
import os
from datetime import datetime

# File to store tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file. If file doesn't exist, return empty list."""
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, 'r', encoding='utf-8') as file:
                tasks = json.load(file)
                return tasks
        except (json.JSONDecodeError, IOError):
            # If file is corrupted, start with empty list
            print("Warning: tasks.json was corrupted. Starting with empty task list.")
            return []
    else:
        return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    try:
        with open(TASKS_FILE, 'w', encoding='utf-8') as file:
            json.dump(tasks, file, indent=4, ensure_ascii=False)
        print("Tasks saved successfully!")
    except IOError:
        print("Error: Could not save tasks to file.")

def add_task(tasks):
    """Add a new task to the list."""
    print("\n--- ADD NEW TASK ---")
    task_name = input("Enter task name: ").strip()
    
    if not task_name:
        print("Error: Task name cannot be empty!")
        return tasks
    
    # Create new task with unique ID
    task_id = len(tasks) + 1
    # Make sure ID is unique in case of deletions
    if tasks:
        task_id = max(task['id'] for task in tasks) + 1
    
    new_task = {
        "id": task_id,
        "name": task_name,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    tasks.append(new_task)
    print(f"Task '{task_name}' added successfully! (ID: {task_id})")
    save_tasks(tasks)
    return tasks

def display_tasks(tasks):
    """Display all tasks in a nice format."""
    print("\n--- YOUR TASKS ---")
    
    if not tasks:
        print("No tasks found! Add some tasks to get started.")
        return
    
    for task in tasks:
        status = "✓ DONE" if task['completed'] else "✗ PENDING"
        print(f"ID: {task['id']} | Status: {status} | Task: {task['name']}")
        print(f"    Created: {task.get('created_at', 'Unknown')}")
        print()

def mark_completed(tasks):
    """Mark a task as completed."""
    display_tasks(tasks)
    
    if not tasks:
        return tasks
    
    try:
        task_id = int(input("\nEnter task ID to mark as completed: ").strip())
    except ValueError:
        print("Error: Please enter a valid number!")
        return tasks
    
    # Find task by ID
    for task in tasks:
        if task['id'] == task_id:
            if task['completed']:
                print(f"Task '{task['name']}' is already completed!")
            else:
                task['completed'] = True
                print(f"Task '{task['name']}' marked as completed!")
                save_tasks(tasks)
            return tasks
    
    print(f"Error: Task with ID {task_id} not found!")
    return tasks

def delete_task(tasks):
    """Delete a task from the list."""
    display_tasks(tasks)
    
    if not tasks:
        return tasks
    
    try:
        task_id = int(input("\nEnter task ID to delete: ").strip())
    except ValueError:
        print("Error: Please enter a valid number!")
        return tasks
    
    # Find and remove task by ID
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            deleted_task = tasks.pop(i)
            print(f"Task '{deleted_task['name']}' deleted successfully!")
            save_tasks(tasks)
            return tasks
    
    print(f"Error: Task with ID {task_id} not found!")
    return tasks

def main():
    """Main function to run the Student Task Tracker program."""
    print("=" * 40)
    print("   STUDENT TASK TRACKER")
    print("=" * 40)
    
    # Load tasks from file
    tasks = load_tasks()
    print(f"Loaded {len(tasks)} task(s) from {TASKS_FILE}")
    
    while True:
        print("\n" + "=" * 40)
        print("MENU:")
        print("1. Add a task")
        print("2. Display all tasks")
        print("3. Mark task as completed")
        print("4. Delete a task")
        print("5. Exit")
        print("=" * 40)
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            tasks = add_task(tasks)
        elif choice == '2':
            display_tasks(tasks)
        elif choice == '3':
            tasks = mark_completed(tasks)
        elif choice == '4':
            tasks = delete_task(tasks)
        elif choice == '5':
            print("\nThank you for using Student Task Tracker!")
            print("Your tasks are saved. Goodbye!")
            break
        else:
            print("Error: Invalid choice! Please enter a number from 1 to 5.")

# Run the program
if __name__ == "__main__":
    main()
