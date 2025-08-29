2# app.py

from task import Task
from todo import TodoList

def main():
    todo = TodoList()

    while True:
        print("\n=== Todo List Menu ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            priority = input("Enter task priority (High/Medium/Low): ")
            task = Task(title, description, priority)
            todo.add_task(task)

        elif choice == "2":
            todo.view_tasks()

        elif choice == "3":
            todo.view_tasks()
            index = int(input("Enter task number to mark completed: "))
            todo.mark_task_completed(index)

        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break

        else:
            print("⚠️ Invalid choice, try again!")

if __name__ == "__main__":
    main()
