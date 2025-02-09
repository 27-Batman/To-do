# Python To do list

tasks = []

def add_task(description):
    task = {"description": description,
            "completed": False,}
    tasks.append(task)
    print(f"Task added: {description}")

def remove_task(description):
    for task in tasks:
        if task["description"] == description:
            tasks.remove(task)
            print(f"Task removed: {description}")
            return
    print(f"Task not found: {description}")

def mark_task_complete(description):
    for task in tasks:
        if task["description"] == description:
            task["completed"] = True
            print(f"Task marked as completed: {description}")
            return
    print(f"Task not found: {description}")

def view_task():
    if not tasks:
        print("No tasks found.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{i}. {task['description']} - {status}")

def main():

    while True:
        print("******************")
        print(" **Welcome to** \nTo-Do List Manager")
        print("******************")
        print("******Option******")
        print("1. Add a Task")
        print("2. Remove a Task")
        print("3. Mark a Task as Completed")
        print("4. View Tasks")
        print("5. Exit")
        print("******************")
        print()

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            description = input("Enter your task description: ")
            add_task(description)
        elif choice == "2":
            description = input("Enter task description to remove: ")
            remove_task(description)
        elif choice == "3":
            description = input("Enter task description to mark as completed: ")
            mark_task_complete(description)
        elif choice == "4":
            view_task()
        elif choice == "5":
            print("Have a nice day! Bye..")
            break
        else:
            print("Invalid Choice.\n Try again........")

if __name__ == "__main__":
    main()