# Task Tracker CLI

A simple Command Line Interface (CLI) application to manage tasks. This CLI allows you to add, update, list, and mark tasks with different statuses. It supports basic task management functionalities like tracking tasks, updating task descriptions, and changing their statuses (e.g., "todo", "in-progress", "done").

## Features

- **Add a new task**: Add a task with a description.
- **Update an existing task**: Update the description of a task.
- **List tasks**: List all tasks or filter by status (e.g., "todo", "in-progress", "done").
- **Mark tasks**: Mark tasks as "in-progress" or "done".
- **Persistent storage**: Tasks are saved in a JSON file, so they persist between sessions.

## Requirement

- Python 3.x
- A JSON file to store tasks (`tasks.json`).

## Installation

1. Clone this repository to your local machine.
   
   ```bash
   git clone https://github.com/yourusername/task-tracker-cli.git
   cd task-tracker-cli
   ```

2. Install dependencies (if any):
   
   You can use a `requirements.txt` file if your project has external dependencies. For now, this project doesn't require any external packages other than Python's standard library.

   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have the necessary permissions to run the script.

## Usage

### 1. **Adding a Task**

To add a new task, use the `add` command followed by the task description:

```bash
python main.py add "Buy groceries"
```

- **Example**: 
  ```bash
  python main.py add "Finish homework"
  ```

This will add a new task with the description "Finish homework", set its status to "todo", and store the creation timestamp.

### 2. **Listing Tasks**

To list all tasks, use the `list` command:

```bash
python main.py list
```

This will display all tasks in your task list.

You can also filter tasks by status (e.g., "todo", "in-progress", or "done"):

```bash
python main.py list todo
python main.py list in-progress
python main.py list done
```

- **Example**:
  ```bash
  python main.py list done
  ```

This will show all tasks that are marked as "done".

### 3. **Marking a Task as In Progress or Done**

To mark a task as "in-progress" or "done", use the `mark-in-progress` or `mark-done` command followed by the task index:

```bash
python main.py mark-in-progress 1
python main.py mark-done 2
```

- **Example**:
  ```bash
  python main.py mark-done 1
  ```

This will mark the task at index `1` as "done".

### 4. **Updating a Task**

To update the description of a task, use the `update` command followed by the task index and the new description:

```bash
python main.py update 1 "Buy food"
```

- **Example**:
  ```bash
  python main.py update 2 "Complete homework"
  ```

This will update the description of the task at index `2` to "Complete homework".

### 5. **Error Handling**

- If you try to add a task with a description that already exists, you will see an error message like:
  ```bash
  Error: Task with description 'Buy groceries' already exists.
  ```

- If you provide an invalid task index (e.g., a number outside the valid range), you will get an error like:
  ```bash
  Error: Task index 5 is out of range.
  ```

## Example Commands

Here’s a summary of the commands you can use:

| Command                             | Description                                                  |
|-------------------------------------|--------------------------------------------------------------|
| `python main.py add "Task description"`  | Add a new task with the given description.                   |
| `python main.py list`                | List all tasks.                                              |
| `python main.py list todo`           | List tasks with "todo" status.                               |
| `python main.py list in-progress`    | List tasks with "in-progress" status.                        |
| `python main.py list done`           | List tasks with "done" status.                               |
| `python main.py mark-in-progress <index>` | Mark a task as "in-progress" by index.                        |
| `python main.py mark-done <index>`   | Mark a task as "done" by index.                              |
| `python main.py update <index> "New description"` | Update a task's description by index.                        |

## Data Storage

- Tasks are stored in a JSON file (`tasks.json`). Each task is represented as a dictionary with the following fields:
  - `index`: The index of the task in the list.
  - `description`: The task's description.
  - `status`: The task's current status (e.g., "todo", "in-progress", "done").
  - `createdAt`: The timestamp when the task was created.
  - `updatedAt`: The timestamp when the task was last updated.

### Example `tasks.json`:
```json
[
  {
    "index": 0,
    "description": "Buy groceries",
    "status": "todo",
    "createdAt": "2025-01-12 12:00:00",
    "updatedAt": "2025-01-12 12:00:00"
  },
  {
    "index": 1,
    "description": "Complete homework",
    "status": "in-progress",
    "createdAt": "2025-01-12 12:30:00",
    "updatedAt": "2025-01-12 12:30:00"
  }
]
```