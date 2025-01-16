# Expense Tracker CLI

Sample solution for the [Expense Tracker](https://roadmap.sh/projects/expense-tracker) challenge from [roadmap.sh](https://roadmap.sh/).

## Features
- Add expenses with descriptions, types, and amounts.
- List all expenses or filter by specific types.
- View summary statistics of your expenses by type or month.
- Delete expenses by ID.


## Commands
- `add`: Add a new expense.
  - Options:
    - `--description`: Description of the expense (required).
    - `--type`: Type of the expense (optional).
    - `--amount`: Amount of the expense (required).

- `list`: Display all expenses.

- `summary`: Show a summary of expenses.
  - Options:
    - `--type`: Filter by expense type.
    - `--month`: Filter by month (1-12).

- `delete`: Delete an expense by ID.
  - Options:
    - `--id`: ID of the expense to delete (required).

## Example Workflow
1. Add expenses:
   ```bash
   python main.py add --description "Lunch" --amount 20
   python main.py add --description "Dinner" --type "Food" --amount 10
   ```

2. List expenses:
   ```bash
   python main.py list
   ```

3. Summarize expenses:
   ```bash
   python main.py summary
   python main.py summary --type "Food"
   ```

4. Delete an expense:
   ```bash
   python main.py delete --id 2
   ```

5. Summarize expenses again:
   ```bash
   python main.py summary --type "Food"
   ```