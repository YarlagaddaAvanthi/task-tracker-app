# Task Tracker App

A Flask-based Task Tracker built with Python and SQL to manage daily tasks efficiently.  
It supports user registration and login, task creation, status updates, and full CRUD operations via a simple web interface.

## Features

- User registration and login (per-user tasks)
- Add, view, edit, and delete tasks (CRUD)
- Task fields: title, description, status, priority, created time
- Status workflow: Pending, In Progress, Completed
- Summary panel showing total, pending, in-progress, and completed tasks
- Responsive UI with basic styling using HTML and CSS

## Tech Stack

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Login
- SQLite (via SQLAlchemy)
- HTML, CSS (custom)

## Project Structure

```text
task-tracker-app/
├── run.py
├── requirements.txt
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── auth_routes.py
├── templates/
│   ├── base.html
│   ├── tasks.html
│   ├── add_task.html
│   ├── edit_task.html
│   ├── login.html
│   └── register.html
└── static/
    └── style.css
```

## How to Run Locally

1. **Clone the repo**

```bash
git clone https://github.com/your-username/task-tracker-app.git
cd task-tracker-app
```

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
venv\Scripts\activate      # on Windows
# source venv/bin/activate # on Linux/Mac
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the app**

```bash
python run.py
```

5. **Open in browser**

```text
http://127.0.0.1:5000
```

## Usage

1. Register a new user account.
2. Log in with your email and password.
3. Go to the Tasks page:
   - Create new tasks from **Add Task**.
   - Edit tasks to update status (Pending, In Progress, Completed).
   - Delete tasks that you no longer need.
4. Check the summary panel to see how many tasks are pending, in progress, and completed.

## Future Improvements

- Add due dates and reminders
- Filter and search tasks
- Tagging or categories for tasks
- API endpoints for integration with other tools
- Deployment on a free hosting platform (Render, Railway, etc.)
