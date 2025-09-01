def todo():
    tasks = []
    while True:
        print("1. Add Task. \n2. Remove Task. \n3. Tasks list. \n4. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task = input("Enter task: ")
            tasks.append(add_task)
        elif choice == "2":
            remove_task = input("Enter which task to remove: ")
            if remove_task in tasks:
                tasks.remove(remove_task)
            else:
                print("Nope, doesnt exist")
        elif choice == "3":
            print(f"Tasks: {tasks}")
        elif choice == "4":
            break
        else:
            print("That ain't right")


todo()
