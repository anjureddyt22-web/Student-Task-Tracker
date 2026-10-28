# Student Task Tracker

A simple, beginner-friendly command-line Python application to help students manage their tasks. All tasks are saved locally in a JSON file, so your tasks remain available even after closing the program.

## Features

1. **Add a task** - Create new tasks with automatic timestamps
2. **Display all tasks** - View all your tasks with their status and creation time
3. **Mark a task as completed** - Update task status when completed
4. **Delete a task** - Remove tasks you no longer need
5. **Auto-save** - Tasks are automatically saved to `tasks.json`

## Project Files

- `main.py` - The main program with all functionality
- `tasks.json` - Automatically created when you save tasks (stores all your task data)
- `README.md` - This documentation file

## Requirements

- Python 3.x (no external libraries needed - only built-in modules: `json`, `os`, `datetime`)
- Works on Windows, macOS, and Linux

## How to Run

### Option 1: Using Command Prompt/Terminal

1. Open a terminal/command prompt in the project folder
2. Run the following command:
   ```bash
   python main.py
   ```
   Or on some systems:
   ```bash
   python3 main.py
   ```

### Option 2: Using IDLE

1. Open `main.py` in Python IDLE
2. Press `F5` or go to `Run > Run Module`

## How to Use

1. **Add a task** - Select option 1, enter the task name
2. **Display all tasks** - Select option 2 to see all tasks with their ID, status, and creation time
3. **Mark task as completed** - Select option 3, enter the task ID from the displayed list
4. **Delete a task** - Select option 4, enter the task ID from the displayed list
5. **Exit** - Select option 5 to save and exit

## Tips for Beginners

- Each task gets a unique ID - use these IDs to mark complete or delete tasks
- Tasks are automatically saved when you add, complete, or delete them
- The `tasks.json` file can be opened in any text editor to view your data
- If the JSON file gets corrupted, the program will start fresh with a warning

## Code Structure

- `load_tasks()` - Loads tasks from JSON file
- `save_tasks()` - Saves tasks to JSON file
- `add_task()` - Adds a new task
- `display_tasks()` - Displays all tasks
- `mark_completed()` - Marks a task as done
- `delete_task()` - Deletes a task
- `main()` - Handles the menu and program flow

Enjoy tracking your tasks! 🎓
