# todo.py
import csv
from task import Task

class TodoList:
    def __init__(self, filename="tasks.csv"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()  # بارگذاری خودکار هنگام شروع برنامه

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
        print(f"✅ Task '{task.title}' added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("⚠️ No tasks found!")
            return

        print("\n=== Your Tasks ===")
        for index, task in enumerate(self.tasks, start=1):
            status = "✅ Completed" if task.completed else "❌ Not Completed"
            print(f"{index}. {task.title} | {task.priority} | {status}")

    def mark_task_completed(self, index):
        if 0 < index <= len(self.tasks):
            self.tasks[index - 1].mark_completed()
            self.save_tasks()
            print(f"🎉 Task '{self.tasks[index - 1].title}' marked as completed!")
        else:
            print("⚠️ Invalid task number!")

    def save_tasks(self):
        """ذخیره تسک‌ها در فایل CSV"""
        with open(self.filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for task in self.tasks:
                writer.writerow([task.title, task.description, task.priority, task.completed])

    def load_tasks(self):
        """بارگذاری تسک‌ها از فایل CSV"""
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 4:
                        title, description, priority, completed = row
                        task = Task(title, description, priority)
                        task.completed = completed == "True"
                        self.tasks.append(task)
        except FileNotFoundError:
            pass  # اگر فایل وجود نداشت، چیزی لود نمی‌کنیم
