# Task Tracker CLI

A lightweight, command-line based Task Tracker built using Python. This project allows users to manage daily tasks directly from the terminal with persistent storage using a JSON file. It demonstrates core backend and CLI development concepts such as command-line argument parsing, CRUD operations, file handling, and state management.

## 🚀 Features

- Add new tasks
- Update existing task descriptions
- Delete tasks
- Mark tasks as `todo`, `in-progress`, or `done`
- List all tasks or filter by status
- Persistent storage using a JSON file
- Simple, fast, and dependency-free

## 🧱 Task Structure

Each task is stored with the following properties:

- `id` – Unique task identifier
- `description` – Short task description
- `status` – Task status (`todo`, `in-progress`, `done`)
- `createdAt` – Task creation timestamp
- `updatedAt` – Last update timestamp

## 📦 Tech Stack

- **Language:** Python 3
- **Storage:** JSON (file-based persistence)
- **Libraries:** Standard Python libraries (`sys`, `json`, `os`, `datetime`)

## 🖥️ CLI Commands
```bash
# Add a task
task-cli add "Buy groceries and cook dinner"

# Update a task
task-cli update 1 "Buy groceries"

# Delete a task
task-cli delete 1

# Mark task status
task-cli mark-in-progress 1
task-cli mark-done 1

# List tasks
task-cli list
task-cli list todo
task-cli list in-progress
task-cli list done
```

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/task-tracker-cli.git
cd task-tracker-cli
```

2. Make the script executable (optional):
```bash
chmod +x task-cli.py
```

3. Run the task tracker:
```bash
python task-cli.py add "Your first task"
```

## 💡 Concepts Used

- Command Line Interface (CLI) development
- Command-line argument parsing (`sys.argv`)
- CRUD operations (Create, Read, Update, Delete)
- File handling and JSON persistence
- Python data structures (lists, dictionaries)
- Timestamp management
- Error handling and input validation
- Modular and clean code design

## 📈 Learning Outcomes

This project strengthens understanding of how real-world CLI tools work and provides a strong foundation for backend, DevOps, and MLOps tooling. It mirrors patterns used in professional utilities such as Git, Docker, and task automation tools.

## 🔮 Future Enhancements

- Task priorities and due dates
- Search and sort functionality
- Colored terminal output
- Unit tests
- Packaging as a Python executable
- Export tasks to different formats (CSV, Markdown)
- Task categories and tags
- Recurring tasks

## 📄 License

This project is open-source and available for learning and personal use.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

---

**Happy Task Tracking! ✅**
