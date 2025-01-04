class TodoListFile:

    ...:     def __init__(self, filename):

    ...:         self.filename = filename

    ...: 

    ...:     def add_task(self, task):

    ...:         """Add a task to the to-do list file."""

    ...:         with open(self.filename, "a") as file:

    ...:             file.write(task + "\n")

    ...:         print(f"Task added: {task}")

    ...: 

    ...:     def remove_task(self, task):

    ...:         """Remove a specific task from the to-do list file."""

    ...:         try:

    ...:             with open(self.filename, "r") as file:

    ...:                 tasks = file.readlines()

    ...: 

    ...:             with open(self.filename, "w") as file:

    ...:                 found = False

    ...:                 for line in tasks:

    ...:                     if line.strip() == task:

    ...:                         found = True

    ...:                     else:

    ...:                         file.write(line)

    ...: 

    ...:             if found:

    ...:                 print(f"Task removed: {task}")

    ...:             else:

    ...:                 print(f"Task not found: {task}")

    ...:         except FileNotFoundError:

    ...:             print(f"No file found: {self.filename}")

    ...: 

    ...:     def view_tasks(self):

    ...:         """View all tasks in the to-do list file."""

    ...:         try:

    ...:             with open(self.filename, "r") as file:

    ...:                 tasks = file.readlines()

    ...: 

    ...:             if tasks:

    ...:                 print("\nTo-Do List:")

    ...:                 for idx, task in enumerate(tasks, 1):

    ...:                     print(f"{idx}. {task.strip()}")

    ...:             else:

    ...:                 print("No tasks to show!")

    ...:         except FileNotFoundError:

    ...:             print(f"No file found: {self.filename}")

    ...: 

    ...:     def clear_tasks(self):

    ...:         """Clear all tasks from the to-do list file."""

    ...:         with open(self.filename, "w") as file:

    ...:             pass

    ...:         print("All tasks cleared!")

    ...: 

    ...: 

    ...: def main():

    ...:     todo_file = TodoListFile("todo_list.txt")

    ...:     count=0

    ...:     while True:

    ...:         print("\nTo-Do List Manager")

    ...:         print("1. Add Task")

    ...:         print("2. Remove Task")

    ...:         print("3. View Tasks")

    ...:         print("4. Clear Tasks")

    ...:         print("5. Exit")

    ...: 

    ...:         choice = input("Enter your choice (1-5): ")

    ...:         if choice == "1":

    ...:             task = input("Enter the task to add: ")

    ...:             todo_file.add_task(task)

    ...:             count+=1

    ...:             a=input("completed/remaining:")

    ...:             print(count,"[",task,"]",":",a)        

    ...:         elif choice == "2":

    ...:             task = input("Enter the task to remove: ")

    ...:             todo_file.remove_task(task)

    ...:         elif choice == "3":

    ...:             todo_file.view_tasks()

    ...:         elif choice == "4":

    ...:             confirm = input("Are you sure you want to clear all tasks? (yes/no): ")

    ...:             if confirm.lower() == "yes":

    ...:                 todo_file.clear_tasks()

    ...:         elif choice == "5":

    ...:             print("Exiting To-Do List Manager. Goodbye!")

    ...:             break

    ...:         else:

    ...:             print("Invalid choice. Please try again.")

    ...: 

    ...: 

    ...: if __name__ == "__main__":

    ...:     main()
