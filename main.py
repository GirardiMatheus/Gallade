def add_task(tasks, task_name):
    task = {"task": task_name, "task_status": False}
    tasks.append(task)
    print(f"Task '{task_name}' has been successfully added!")
    return

def view_tasks(tasks):
    print("\nTask List:")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["task_status"] else ""
        task_name = task["task"]
        print(f"{index}. [{status}] {task_name}")
    return

def update_task(tasks, task_index, new_task_name):
    adjusted_index = task_index - 1
    if adjusted_index >= 0 and adjusted_index < len(tasks):
        tasks[adjusted_index]["task"] = new_task_name
        print(f"Task {task_index} updated to '{new_task_name}'")
    else:
        print("Invalid task index.")
    return

def complete_task(tasks, task_index):
    adjusted_index = task_index - 1
    if adjusted_index >= 0 and adjusted_index < len(tasks):
        tasks[adjusted_index]["task_status"] = True
        print(f"Task {task_index} marked as completed")
    else:
        print("Invalid task index.")
    return

def delete_completed_tasks(tasks):
    tasks[:] = [task for task in tasks if not task["task_status"]]
    print("Completed tasks have been deleted!")
    return

tasks = []

while True:
    print("\nMenu - Galled: A Simple Task Manager with Python")
    print("1. Add task")
    print("2. View tasks")
    print("3. Update task")
    print("4. Complete task")
    print("5. Delete completed tasks")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task_name = input("Enter the name of the task to add: ")
        add_task(tasks, task_name)

    elif choice == "2":
        view_tasks(tasks)

    elif choice == "3":
        view_tasks(tasks)
        task_index = int(input("Enter the task number to update: "))
        new_name = input("Enter the new task name: ")
        update_task(tasks, task_index, new_name)
    
    elif choice == "4":
        view_tasks(tasks)
        task_index = int(input("Enter the task number to mark as complete: "))
        complete_task(tasks, task_index)
    
    elif choice == "5":
        delete_completed_tasks(tasks)
        view_tasks(tasks)

    elif choice == "6":
        print("Program terminated")
        break
    else:
        print("Invalid choice. Please try again.")
