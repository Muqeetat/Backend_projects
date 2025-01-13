import argparse
import json
from datetime import datetime

# Load existing tasks from a file
try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []

def addTask():
    if args.task:
            # any() returns True if at least one task has the same description, and False otherwise.
         if any(task["description"] == args.task for task in tasks):
            print(f"Error: Task with description '{args.task}' already exists.")
         else:
            # Create a new task dictionary
            task = {
                "index": len(tasks),  # Auto-assign index based on the length of the list
                "description": args.task,
                "status": "todo",  # New tasks are "todo" by default
                "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "updatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            tasks.append(task)
            index = len(tasks) - 1
            print(f"Task added successfully (ID: {index})")
            saveFile()
    else:
        print("Error: Please provide a task description.")
    
def updateTask():
    if 0 <= args.index < len(tasks):
        task = tasks[args.index]
        old_description = task["description"]
        task["description"] = args.task
        task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Task updated: '{old_description}' -> '{args.task}'")
        saveFile()
    else:
        print(f"Error: Task index {args.index} is out of range.")
from datetime import datetime

# Function to mark task as "in-progress"
def markTaskInProgress():
    if args.index is not None:
        if 0 <= args.index < len(tasks):
            tasks[args.index]["status"] = "in-progress"  # Update the status
            tasks[args.index]["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Update timestamp
            print(f"Task at index {args.index} marked as 'in-progress': {tasks[args.index]['description']}")
            saveFile()
        else:
            print(f"Error: Task index {args.index} is out of range.")
    else:
        print("Error: Please provide a valid task index.")

# Function to mark task as "done"
def markTaskAsDone():
    if args.index is not None:
        if 0 <= args.index < len(tasks):
            tasks[args.index]["status"] = "done"  # Update the status
            tasks[args.index]["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Update timestamp
            print(f"Task at index {args.index} marked as 'done': {tasks[args.index]['description']}")
            saveFile()
        else:
            print(f"Error: Task index {args.index} is out of range.")
    else:
        print("Error: Please provide a valid task index.")

def listTasks():
    # If a status is provided, filter tasks by status
    if args.status:
        valid_statuses = ["done", "todo", "in-progress"]
        
        # Check if the provided status is valid
        if args.status not in valid_statuses:
            print(f"Error: '{args.status}' is not a valid status. Use one of {valid_statuses}.")
            return
        
        # Filter tasks by status
        filtered_tasks = [task for task in tasks if task["status"] == args.status]
        
        # Display filtered tasks
        if filtered_tasks:
            print(f"Tasks with status '{args.status}':")
            for task in filtered_tasks:
                print(f"Index: {task['index']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['createdAt']}, Updated At: {task['updatedAt']}")
        else:
            print(f"No tasks found with status '{args.status}'.")
    else:
        # If no status is provided, list all tasks
        if tasks:
            print("All tasks:")
            for task in tasks:
                print(f"Index: {task['index']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['createdAt']}, Updated At: {task['updatedAt']}")
        else:
            print("No tasks found.")


def deleteTask():
    try:
        if 0 <= args.index < len(tasks):
            tasks.pop(args.index)
            print(f"Task '{args.index}' has been removed.")

              # Save tasks to the file
            saveFile()
        else:
            print(f"Task #{args.index} was not found.")
    except:
        print("Invalid input.")

def saveFile():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

# Initialize the main parser
parser = argparse.ArgumentParser(description="Task CLI to manage your tasks.")
subparsers = parser.add_subparsers(dest="operation", required=True, help="Sub-operations: add, list, update,delete")

# Add parser for the "add" operation
add_parser = subparsers.add_parser("add", help="Add a new task")
add_parser.add_argument("task", type=str, help="The task description")

# Add parser for the "list" operation
list_parser = subparsers.add_parser("list", help="List all tasks")
list_parser.add_argument("status", type=str, nargs="?", help="Filter tasks by status (e.g., 'done', 'todo', 'in-progress')")

# Add parser for the "update" operation
update_parser = subparsers.add_parser("update", help="Update an existing task")
update_parser.add_argument("index", type=int, help="Index of the task to update")
update_parser.add_argument("task", type=str, help="The new task description")

# Add subcommand for "mark-in-progress"
mark_in_progress_parser = subparsers.add_parser("mark-in-progress", help="Mark a task as in-progress")
mark_in_progress_parser.add_argument("index", type=int, help="Index of the task to mark as in-progress")

# Add subcommand for "mark-done"
mark_done_parser = subparsers.add_parser("mark-done", help="Mark a task as done")
mark_done_parser.add_argument("index", type=int, help="Index of the task to mark as done")

# Add parser for the "delete" operation
update_parser = subparsers.add_parser("delete", help="delete an existing task")
update_parser.add_argument("index", type=int, help="Index of the task to delete")

# Parse arguments
args = parser.parse_args()

# Handle operations
if args.operation == "add":
    addTask()

elif args.operation == "list":
    listTasks()
    
elif args.operation == "update":
    updateTask()

elif args.operation == "mark-in-progress":
    markTaskInProgress()

elif args.operation == "mark-done":
    markTaskAsDone()

elif args.operation == "delete":
    deleteTask()

