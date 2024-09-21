import os
import datetime

# Task class to define a task object
class Task:
    def __init__(self, title, description, due_date, priority, status="Pending"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status

    def __str__(self):
        return f"{self.title}: {self.description} (Due: {self.due_date}, Priority: {self.priority}, Status: {self.status})"


# Task Manager to manage tasks
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date, priority):
        task = Task(title, description, due_date, priority)
        self.tasks.append(task)
        print(f"Task '{title}' added successfully.")

    def view_tasks(self, filter_by=None):
        if filter_by == "completed":
            tasks = [task for task in self.tasks if task.status == "Completed"]
        elif filter_by == "pending":
            tasks = [task for task in self.tasks if task.status == "Pending"]
        else:
            tasks = self.tasks

        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

    def mark_task_complete(self, task_index):
        try:
            self.tasks[task_index - 1].status = "Completed"
            print(f"Task '{self.tasks[task_index - 1].title}' marked as complete.")
        except IndexError:
            print("Invalid task number.")

    def remove_task(self, task_index):
        try:
            task = self.tasks.pop(task_index - 1)
            print(f"Task '{task.title}' removed successfully.")
        except IndexError:
            print("Invalid task number.")

    def save_tasks(self, filename="tasks.txt"):
        with open(filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task.title},{task.description},{task.due_date},{task.priority},{task.status}\n")
        print("Tasks saved successfully.")

    def load_tasks(self, filename="tasks.txt"):
        if not os.path.exists(filename):
            return
        with open(filename, 'r') as file:
            for line in file:
                title, description, due_date, priority, status = line.strip().split(',')
                task = Task(title, description, due_date, priority, status)
                self.tasks.append(task)
        print("Tasks loaded successfully.")


def main():
    task_manager = TaskManager()
    task_manager.load_tasks()

    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Remove Task")
        print("5. Save Tasks")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            priority = input("Enter priority (High, Medium, Low): ")
            task_manager.add_task(title, description, due_date, priority)
        elif choice == "2":
            filter_option = input("View (all/completed/pending): ").lower()
            if filter_option == "completed":
                task_manager.view_tasks(filter_by="completed")
            elif filter_option == "pending":
                task_manager.view_tasks(filter_by="pending")
            else:
                task_manager.view_tasks()
        elif choice == "3":
            task_manager.view_tasks()
            task_index = int(input("Enter task number to mark as complete: "))
            task_manager.mark_task_complete(task_index)
        elif choice == "4":
            task_manager.view_tasks()
            task_index = int(input("Enter task number to remove: "))
            task_manager.remove_task(task_index)
        elif choice == "5":
            task_manager.save_tasks()
        elif choice == "6":
            task_manager.save_tasks()
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
