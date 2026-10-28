# Student Task Tracker (Web App)

An upgraded version of the Student Task Tracker with a modern web front end using HTML, CSS, JavaScript, Flask, and local JSON storage.

## Features

- **Modern Dashboard**: View total tasks, completed tasks, and pending tasks at a glance
- **Add Tasks**: Enter a task in the input box and click "Add Task" (or press Enter)
- **Task Management**: View all tasks as clean cards with "Complete" and "Delete" buttons
- **Responsive Design**: Works great on mobile phones, tablets, and laptops
- **Light Theme**: Pleasant light theme with blue and purple accents, rounded cards
- **Local Storage**: Tasks are saved in `tasks.json` and persist after restarting
- **Full CRUD**: Add, view, complete, and delete tasks via the web interface
- **Original CLI Still Available**: `main.py` remains unchanged and fully functional

## Project Structure

```
studentTaskTracker/
├── app.py              # Flask backend
├── main.py             # Original CLI application (preserved)
├── tasks.json          # Task data storage (shared with CLI)
├── templates/
│   └── index.html      # Main HTML template
├── static/
│   ├── css/
│   │   └── style.css   # Styling
│   └── js/
│       └── app.js      # Frontend JavaScript
└── README.md           # Documentation
```

## Requirements

- Python 3.7 or higher
- Flask 2.0 or higher

All other dependencies are built-in Python modules (`json`, `os`, `datetime`).

## Installation

### 1. Install Python

If you don't have Python installed, download it from [python.org](https://www.python.org/downloads/). Make sure to check "Add Python to PATH" during installation.

### 2. Install Flask

Open a terminal/command prompt in the project folder and run:

```bash
pip install flask
```

If you're using Python 3 and `pip` points to Python 2, use:

```bash
pip3 install flask
```

Alternatively, you can use a virtual environment (recommended):

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate

# Install Flask
pip install flask
```

## Running the Application

### Web Application (Recommended)

1. Open a terminal/command prompt in the project folder
2. Run the Flask app:
   ```bash
   python app.py
   ```
   Or:
   ```bash
   python3 app.py
   ```
3. Open your web browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)
4. Start adding, completing, and deleting tasks!

To stop the server, press `Ctrl+C` in the terminal.

### Original CLI Application

If you want to use the original command-line version, run:

```bash
python main.py
```

Both versions share the same `tasks.json` file, so tasks are synchronized between them.

## How to Use the Web App

1. **View Stats**: The dashboard at the top shows total, completed, and pending tasks
2. **Add a Task**: Type your task in the input box and click "Add Task" or press Enter
3. **Complete a Task**: Click the "Complete" button on a pending task card
4. **Delete a Task**: Click the "Delete" button to remove a task (you'll be asked to confirm)
5. **Responsive**: The layout adjusts automatically for mobile and laptop screens

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Storage**: JSON file
- **Fonts**: Inter (Google Fonts)

## Notes

- The app runs in debug mode by default. For production use, disable debug mode.
- Tasks are stored in `tasks.json` in the project root - same file used by `main.py`
- No external APIs or paid services are used
- All code is contained within the project folder
