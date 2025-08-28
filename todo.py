# todo.py

from task import Task

class TodoList:
    def __init__(self):
        # Initialize an empty list of tasks
        self.tasks = []

    def add_task(self, task):
        # Add a new task to the list
        self.tasks.append(task)
        print(f"✅ Task '{task.title}' added successfully!")

    def view_tasks(self):
        # Display all tasks
        if not self.tasks:
            print("⚠️ No tasks found!")
            return

        for index, task in enumerate(self.tasks, start=1):
            status = "✅ Completed" if task.completed else "❌ Not Completed"
            print(f"{index}. {task.title} | {task.priority} | {status}")

    def mark_task_completed(self, index):
        # Mark a specific task as completed
        if 0 < index <= len(self.tasks):
            self.tasks[index - 1].mark_completed()
            print(f"🎉 Task '{self.tasks[index - 1].title}' marked as completed!")
        else:
            print("⚠️ Invalid task number!")
