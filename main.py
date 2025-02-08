# Python To do list

task = []

def add_task():
    pass

def remove_task():
    pass

def mark_task_complete():
    pass

def view_task():
    pass

def main():

    while True:
        print("*****************************")
        print(" **Welcome to** \nTo-Do List Manager")
        print("1. Add a Task")
        print("2. Remove a Task")
        print("3. Mark a Task as Completed")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            mark_task_complete()
        elif choice == "4":
            view_task()
        elif choice == "5":
            print("Have a nice day! Bye..")
            break
        else:
            print("Invalid Choice.\n Try again........")

if __name__ == "__main__":
    main()