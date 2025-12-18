import sys
import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"


# ---------------- Utility Functions ---------------- #

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def get_current_time():
    return datetime.now().isoformat(timespec="seconds")


def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


# ---------------- Core Features ---------------- #

def add_task(description):
    tasks = load_tasks()
    task = {
        "id": get_next_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": get_current_time(),
        "updatedAt": get_current_time()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task['id']})")


def update_task(task_id, description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            task["updatedAt"] = get_current_time()
            save_tasks(tasks)
            print("Task updated successfully")
            return
    print("Task not found")


def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task["id"] != task_id]
    if len(updated_tasks) == len(tasks):
        print("Task not found")
        return
    save_tasks(updated_tasks)
    print("Task deleted successfully")


def mark_task(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = get_current_time()
            save_tasks(tasks)
            print(f"Task marked as {status}")
            return
    print("Task not found")


def list_tasks(filter_status=None):
    tasks = load_tasks()
    if filter_status:
        tasks = [task for task in tasks if task["status"] == filter_status]

    if not tasks:
        print("No tasks found")
        return

    for task in tasks:
        print(f"[{task['id']}] {task['description']} "
              f"({task['status']})")


# ---------------- CLI Handler ---------------- #

def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [arguments]")
        return

    command = sys.argv[1]

    try:
        if command == "add":
            add_task(sys.argv[2])

        elif command == "update":
            update_task(int(sys.argv[2]), sys.argv[3])

        elif command == "delete":
            delete_task(int(sys.argv[2]))

        elif command == "mark-in-progress":
            mark_task(int(sys.argv[2]), "in-progress")

        elif command == "mark-done":
            mark_task(int(sys.argv[2]), "done")

        elif command == "list":
            if len(sys.argv) == 3:
                list_tasks(sys.argv[2])
            else:
                list_tasks()

        else:
            print("Unknown command")

    except IndexError:
        print("Invalid arguments supplied")
    except ValueError:
        print("Task ID must be a number")


if __name__ == "__main__":
    main()
