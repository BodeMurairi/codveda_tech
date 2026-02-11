#!/usr/bin/env python3

import json
import os

FILE_NAME = "tasks.json"

def initialize_file():
    """Create tasks.json if it does not exist"""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            json.dump([], file)

def load_tasks():
    """Load tasks from JSON file"""
    with open(FILE_NAME, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    """Save tasks to JSON file"""
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    title = input("Enter task title: ").strip()

    if not title:
        print("Task cannot be empty.")
        return

    tasks.append({
        "title": title,
        "completed": False
    })

    save_tasks(tasks)
    print("Task added successfully.")


def list_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["completed"] else "✘"
        print(f"{i}. [{status}] {task['title']}")
    print()


def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return

    list_tasks(tasks)

    try:
        index = int(input("Enter task number to delete: "))

        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks(tasks)
            print(f"Deleted task: {removed['title']}")
        else:
            print("Task number does not exist.")

    except ValueError:
        print("Please enter a valid number.")


def mark_done(tasks):
    if not tasks:
        print("No tasks available.")
        return

    list_tasks(tasks)

    try:
        index = int(input("Enter task number to mark as done: "))

        if 1 <= index <= len(tasks):
            tasks[index - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed.")
        else:
            print("Task number does not exist.")

    except ValueError:
        print("Please enter a valid number.")

def main():
    initialize_file()

    while True:
        tasks = load_tasks()

        print("TO-DO LIST")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Done")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            list_tasks(tasks)

        elif choice == "3":
            delete_task(tasks)

        elif choice == "4":
            mark_done(tasks)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-5.")

        print()

if __name__ == "__main__":
    main()
