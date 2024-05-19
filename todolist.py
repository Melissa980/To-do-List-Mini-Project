import os

tasks = []

# Display the menu
def display_menu():
    print("""
    Welcome to the To-Do List App!
    Menu:
    1. Add a task
    2. View tasks
    3. Mark a task as complete
    4. Delete a task
    5. Quit
    """)

# Add a task with priority
def add_task(title="Incomplete", priority="Can Wait"):
    tasks.append({"title": title, "status": "Incomplete", "priority": priority})
    print("Task added successfully!")

# View tasks
def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['title']} - {task['status']} - Priority: {task['priority']}")

# Mark a task as complete
def mark_task_complete():
    view_tasks()
    try:
        task_index = int(input("Enter the task number to mark as complete: ")) - 1
        tasks[task_index]["status"] = "Complete"
        print("Task marked as complete.")
    except (ValueError, IndexError):
        print("Invalid input or task number.")
    finally:
        view_tasks() 

# Delete a task
def delete_task():
    view_tasks()
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        del tasks[task_index]
        print("Task deleted successfully.")
    except (ValueError, IndexError):
        print("Invalid input or task number.")

# Main function
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            task_title = input("Enter task title: ")
            task_priority = input("Enter task priority (Urgent, Important, Can Wait): ").capitalize()
            if task_priority not in ["Urgent", "Important", "Can Wait"]:
                print("Invalid priority. Defaulting to 'Can Wait'.")
                task_priority = "Can Wait"
            add_task(task_title, task_priority)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Thank you for using the To-Do List App!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
