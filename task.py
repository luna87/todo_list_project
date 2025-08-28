# task.py

class Task:
    def __init__(self, title, description, priority):
        # Store task details
        self.title = title          # Task title
        self.description = description  # Task description
        self.priority = priority    # Task priority: High, Medium, Low
        self.completed = False      # Default: not completed

    def mark_completed(self):
        # Mark task as completed
        self.completed = True
