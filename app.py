tasks = []

def add_task(task):
    tasks.append(task)
    return tasks

def view_tasks():
    return tasks

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        return True
    return False

def show_menu():
    print("\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")

if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Choose: ")

        if choice == "1":
            add_task(input("Enter task: "))
        elif choice == "2":
            print(view_tasks())
        elif choice == "3":
            t = input("Enter task to remove: ")
            if remove_task(t):
                print("Task removed")
            else:
                print("Task not found")
        elif choice == "4":
            break
        else:
            print("Invalid choice")
