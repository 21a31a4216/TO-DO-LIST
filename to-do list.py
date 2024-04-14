class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_completed(self, index):
        if index < len(self.tasks):
            self.tasks[index] = f"[COMPLETED] {self.tasks[index]}"

    def remove_completed_tasks(self):
        self.tasks = [task for task in self.tasks if not task.startswith("[COMPLETED]")]

    def display_tasks(self):
        if self.tasks:
            for index, task in enumerate(self.tasks):
                print(f"{index+1}. {task}")
        else:
            print("No tasks in the list.")

todo_list = TodoList()

while True:
    print("What would you like to do?")
    print("1. Add a task")
    print("2. Mark a task as completed")
    print("3. Remove completed tasks")
    print("4. Display tasks")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter the task: ")
        todo_list.add_task(task)
        print("Task added successfully!")
    elif choice == "2":
        index = int(input("Enter the index of the task to mark as completed: ")) - 1
        todo_list.mark_task_completed(index)
        print("Task marked as completed!")
    elif choice == "3":
        todo_list.remove_completed_tasks()
        print("Completed tasks removed!")
    elif choice == "4":
        todo_list.display_tasks()
    elif choice == "5":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")