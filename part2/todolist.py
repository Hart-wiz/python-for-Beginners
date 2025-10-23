# Mini Project: To-Do List with Save File
# 🧩 Project Overview:

# Build a command-line To-Do List app that lets users:

# Add new tasks

# View all tasks

# Mark tasks as done

# Save and load tasks from a JSON file

# ---------------------------------------------------------------------------------

import json
tasks = []

try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []


while True:
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Save & Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        for i, task in enumerate(tasks, 1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {task['title']} {status}")

    elif choice == "2":
        title = input("Enter new task: ")
        tasks.append({"title": title, "done": False})
        print("Task added!")

    elif choice == "3":
        task_num = int(input("Enter task number to mark done: "))
        if 0 < task_num <= len(tasks):
            tasks[task_num - 1]["done"] = True
            print("Task marked as done!")

    elif choice == "4":
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)
        print("Tasks saved. Goodbye!")
        break

    else:
        print("Invalid choice, try again.")
