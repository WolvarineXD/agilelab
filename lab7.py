# Simple To-Do List App
tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added!")

def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

while True:
    print("\nOptions: 1) Add Task 2) Show Tasks 3) Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        print("Exiting To-Do List!")
        break
    else:
        print("Invalid choice! Try again.")
