todo_list = []

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter task: ")
    todo_list.append(task)
    print(" Task added!")

def update_task():
    view_tasks()
    i = int(input("Enter task number to update: ")) - 1
    if 0 <= i < len(todo_list):
        new = input("Enter new task: ")
        todo_list[i] = new
        print(" Task updated!")
    else:
        print(" Invalid number!")

def delete_task():
    view_tasks()
    i = int(input("Enter task number to delete: ")) - 1
    if 0 <= i < len(todo_list):
        removed = todo_list.pop(i)
        print(f" Task '{removed}' deleted!")
    else:
        print(" Invalid number!")

while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print(" Exiting To-Do List App.")
        break
    else:
        print(" Invalid option.")
