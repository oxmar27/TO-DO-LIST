import json
import os

FILE_NAME = "tasks.json"

# ---------------- Storage ----------------
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f)


# ---------------- Core Functions ----------------
def add_task(tasks, title):
    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)

def mark_completed(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)

def edit_task(tasks, index, new_title):
    if 0 <= index < len(tasks):
        tasks[index]["title"] = new_title
        save_tasks(tasks)

def show_tasks(tasks):
    if not tasks:
        print("No tasks found!")
        return

    for i, task in enumerate(tasks):
        status = "✔" if task["completed"] else "✘"
        print(f"{i}. {task['title']} [{status}]")


# ---------------- NEW: Search ----------------
def search_tasks(tasks, keyword):
    found = False
    for i, task in enumerate(tasks):
        if keyword.lower() in task["title"].lower():
            status = "✔" if task["completed"] else "✘"
            print(f"{i}. {task['title']} [{status}]")
            found = True

    if not found:
        print("No matching tasks found!")


# ---------------- Main ----------------
def main():
    tasks = load_tasks()

    while True:
        print("\n1. Show Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Edit Task")
        print("6. Search Task")
        print("7. Exit")

        choice = input("Choose: ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            title = input("Enter task: ")
            add_task(tasks, title)

        elif choice == "3":
            index = int(input("Enter task index: "))
            delete_task(tasks, index)

        elif choice == "4":
            index = int(input("Enter task index: "))
            mark_completed(tasks, index)

        elif choice == "5":
            index = int(input("Enter task index: "))
            new_title = input("Enter new title: ")
            edit_task(tasks, index, new_title)

        elif choice == "6":
            keyword = input("Enter keyword to search: ")
            search_tasks(tasks, keyword)

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()