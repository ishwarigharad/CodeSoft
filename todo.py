def display_menu():
    """Display the menu options to the user."""
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Completed")
    print("4. Exit")

def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter the task: ").strip()
    if task:
        tasks.append({'task': task, 'completed': False})
        print(f'Task "{task}" added.')
    else:
        print("Task cannot be empty.")

def view_tasks(tasks):
    """View all tasks in the list."""
    if not tasks:
        print("No tasks to show.")
        return
    
    print("\nTasks List:")
    for index, task in enumerate(tasks, 1):
        status = '✓' if task['completed'] else '✗'
        print(f"{index}. {task['task']} [{status}]")

def mark_task_completed(tasks):
    """Mark a task as completed."""
    view_tasks(tasks)
    try:
        index = int(input("Enter the task number to mark as completed: "))
        if index < 1 or index > len(tasks):
            print("Invalid task number.")
        else:
            tasks[index - 1]['completed'] = True
            print(f"Task {index} marked as completed.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    """Main program loop."""
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
