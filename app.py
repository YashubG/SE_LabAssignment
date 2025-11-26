tasks = []

def show_menu():
    print("\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")

while True:
    show_menu()
    choice = input("Choose: ")

    if choice == "1":
        tasks.append(input("Enter task: "))
    elif choice == "2":
        print(tasks)
    elif choice == "3":
        t = input("Enter task to remove: ")
        if t in tasks:
            tasks.remove(t)
    elif choice == "4":
        break
    else:
        print("Invalid choice")
