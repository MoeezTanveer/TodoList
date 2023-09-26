class Task:
    def __init__(self, description, category, due_date=None):
        self.description = description
        self.category = category
        self.due_date = due_date

    def __str__(self):
        return f"{self.description} ({self.category}){' - Due: ' + self.due_date if self.due_date else ''}"


class Todo:
    def __init__(self, name):
        self.name = name
        self.tasks = []  
        self.filename = f"{name}_todo.txt"  

        try:
            with open(self.filename, 'r') as file:
                task_lines = file.readlines()
                for line in task_lines:
                    parts = line.strip().split('|')
                    if len(parts) >= 2:
                        description, category = parts[:2]
                        due_date = parts[2] if len(parts) > 2 else None
                        self.tasks.append(Task(description, category, due_date))
        except FileNotFoundError:
            pass  

    def display(self):
        print(f"Welcome to Todo List, {self.name}")
        if not self.tasks:
            print("No tasks in your todo list.")
        else:
            print("Your tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def add_task(self, description, category, due_date=None):
        self.tasks.append(Task(description, category, due_date))
        self.save_tasks()  

    def remove_task(self, task_index):
        try:
            task_index = int(task_index)
            if 1 <= task_index <= len(self.tasks):
                removed_task = self.tasks.pop(task_index - 1)
                print(f"Removed: {removed_task}")
                self.save_tasks() 
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid task number.")

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                task_line = f"{task.description}|{task.category}"
                if task.due_date:
                    task_line += f"|{task.due_date}"
                file.write(task_line + '\n')


if __name__ == '__main__':
    name = input("Enter your name: ")
    user = Todo(name)

    while True:
        print("\nOptions:")
        print("1. Display tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1': 
            user.display()
        elif choice == '2':
            description = input("Enter the task description: ")
            category = input("Enter the task category (e.g., Work, Personal): ")
            due_date = input("Enter the due date (optional): ")
            user.add_task(description, category, due_date)
        elif choice == '3':
            task_index = input("Enter the task number to remove: ")
            user.remove_task(task_index)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a valid option.")
