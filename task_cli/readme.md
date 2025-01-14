# Task Tracker CLI
Sample solution for the [task-tracker](https://roadmap.sh/projects/task-tracker) challenge from [roadmap.sh](https://roadmap.sh/). 

## How to run

Clone the repository and run the following command:

```bash
git clone https://github.com/Muqeetat/Backend_projects.git
cd Backend_projects/task_cli
```

## Features

- **Add a new task**: Add a task with a description.
- **Update an existing task**: Update the description of a task.
- **List tasks**: List all tasks or filter by status (e.g., "todo", "in-progress", "done").
- **Mark tasks**: Mark tasks as "in-progress" or "done".
- **Persistent storage**: Tasks are saved in a JSON file, so they persist between sessions.

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
| `python main.py delete <index>` | Delete a task by index.                        |

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
