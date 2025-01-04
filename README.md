# todo_file
# To-Do List Manager

## Overview
The To-Do List Manager is a Python-based command-line application that allows users to manage their tasks efficiently. The tasks are stored in a text file, making the application persistent and simple to use.

## Features
- **Add Tasks**: Add a new task to the to-do list.
- **Remove Tasks**: Remove a specific task from the list.
- **View Tasks**: View all tasks currently in the list.
- **Clear Tasks**: Delete all tasks from the list.
- **Track Completed/Remaining Tasks**: Count and label tasks as completed or remaining.
- **Exit**: Quit the application.

## Prerequisites
- Python 3.x

## File Structure
- **todo_list.txt**: A file that stores the to-do list tasks.
- **main.py**: The Python script for the To-Do List Manager.

## How to Run
1. Ensure Python 3.x is installed on your system.
2. Copy the code to a file named `main.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `main.py`.
5. Run the application using the command:
   ```
   python main.py
   ```

## Usage
1. When you run the application, a menu with the following options will appear:
   ```
   To-Do List Manager
   1. Add Task
   2. Remove Task
   3. View Tasks
   4. Clear Tasks
   5. Exit
   ```
2. Enter the number corresponding to your desired action and follow the prompts.

### Example
#### Adding a Task:
```
Enter your choice (1-5): 1
Enter the task to add: Buy groceries
completed/remaining: remaining
1 [ Buy groceries ] : remaining
```

#### Viewing Tasks:
```
Enter your choice (1-5): 3

To-Do List:
1. Buy groceries
```

#### Removing a Task:
```
Enter your choice (1-5): 2
Enter the task to remove: Buy groceries
Task removed: Buy groceries
```

#### Clearing Tasks:
```
Enter your choice (1-5): 4
Are you sure you want to clear all tasks? (yes/no): yes
All tasks cleared!
```

#### Exiting the Application:
```
Enter your choice (1-5): 5
Exiting To-Do List Manager. Goodbye!
```

## Code Explanation
### Class: `TodoListFile`
- **`__init__`**: Initializes the file name to store tasks.
- **`add_task(task)`**: Appends a new task to the file.
- **`remove_task(task)`**: Removes a specific task from the file.
- **`view_tasks()`**: Displays all tasks in the file.
- **`clear_tasks()`**: Deletes all tasks from the file.

### Function: `main()`
- Provides a user interface for managing the to-do list.
- Handles user input and calls appropriate methods from `TodoListFile`.

## Notes
- Tasks are stored in a plain text file named `todo_list.txt`.
- Ensure proper write permissions for the file location.
- The application does not support advanced features like priorities or deadlines but can be extended to include them.

# To-Do List Manager

## Overview
The To-Do List Manager is a Python-based command-line application that allows users to manage their tasks efficiently. The tasks are stored in a text file, making the application persistent and simple to use.

## Features
- **Add Tasks**: Add a new task to the to-do list.
- **Remove Tasks**: Remove a specific task from the list.
- **View Tasks**: View all tasks currently in the list.
- **Clear Tasks**: Delete all tasks from the list.
- **Track Completed/Remaining Tasks**: Count and label tasks as completed or remaining.
- **Exit**: Quit the application.

## Prerequisites
- Python 3.x

## File Structure
- **todo_list.txt**: A file that stores the to-do list tasks.
- **main.py**: The Python script for the To-Do List Manager.

## How to Run
1. Ensure Python 3.x is installed on your system.
2. Copy the code to a file named `main.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `main.py`.
5. Run the application using the command:
   ```
   python main.py
   ```

## Usage
1. When you run the application, a menu with the following options will appear:
   ```
   To-Do List Manager
   1. Add Task
   2. Remove Task
   3. View Tasks
   4. Clear Tasks
   5. Exit
   ```
2. Enter the number corresponding to your desired action and follow the prompts.

### Example
#### Adding a Task:
```
Enter your choice (1-5): 1
Enter the task to add: Buy groceries
completed/remaining: remaining
1 [ Buy groceries ] : remaining
```

#### Viewing Tasks:
```
Enter your choice (1-5): 3

To-Do List:
1. Buy groceries
```

#### Removing a Task:
```
Enter your choice (1-5): 2
Enter the task to remove: Buy groceries
Task removed: Buy groceries
```

#### Clearing Tasks:
```
Enter your choice (1-5): 4
Are you sure you want to clear all tasks? (yes/no): yes
All tasks cleared!
```

#### Exiting the Application:
```
Enter your choice (1-5): 5
Exiting To-Do List Manager. Goodbye!
```

## Code Explanation
### Class: `TodoListFile`
- **`__init__`**: Initializes the file name to store tasks.
- **`add_task(task)`**: Appends a new task to the file.
- **`remove_task(task)`**: Removes a specific task from the file.
- **`view_tasks()`**: Displays all tasks in the file.
- **`clear_tasks()`**: Deletes all tasks from the file.

### Function: `main()`
- Provides a user interface for managing the to-do list.
- Handles user input and calls appropriate methods from `TodoListFile`.

## Notes
- Tasks are stored in a plain text file named `todo_list.txt`.
- Ensure proper write permissions for the file location.
- The application does not support advanced features like priorities or deadlines but can be extended to include them.


