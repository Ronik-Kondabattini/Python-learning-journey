tasks = []

try:
    with open('tasks.txt', 'r') as file:
        tasks = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    pass

while True:
    print("\nWelcome to To-Do List")
    print("1. Add Task")
    print("2. List All Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

    choice = int(input("Enter number (1-5): "))

    if choice == 1:
        task = input("Enter your task: ")
        tasks.append(f"[Pending] {task}")
        with open('tasks.txt', 'a') as file:
            file.write(f"[Pending] {task}\n")
        print("✅ Task added successfully.")

    elif choice == 2:
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, 1):
                if t.startswith("[Pending] "):
                    status = "⏳"
                    task_text = t[len("[Pending] "):]
                elif t.startswith("[Done] "):
                    status = "✅"
                    task_text = t[len("[Done] "):]
                else:
                    status = "⏳"
                    task_text = t
                print(f"{i}. {status} {task_text}")

    elif choice == 3:
        if not tasks:
            print("No tasks to delete.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, 1):
                if t.startswith("[Pending] "):
                    status = "⏳"
                    task_text = t[len("[Pending] "):]
                elif t.startswith("[Done] "):
                    status = "✅"
                    task_text = t[len("[Done] "):]
                else:
                    status = "⏳"
                    task_text = t
                print(f"{i}. {status} {task_text}")

            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                with open('tasks.txt', 'w') as file:
                    for t in tasks:
                        file.write(t + '\n')
                print(f"❌ Task '{removed[len('[Pending] '):]}' deleted.")
            else:
                print("Invalid number.")

    elif choice == 4:
        if not tasks:
            print("No tasks to mark as completed.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, 1):
                if t.startswith("[Pending] "):
                    status = "⏳"
                    task_text = t[len("[Pending] "):]
                elif t.startswith("[Done] "):
                    status = "✅"
                    task_text = t[len("[Done] "):]
                else:
                    status = "⏳"
                    task_text = t
                print(f"{i}. {status} {task_text}")

            num = int(input("Enter task number to mark as completed: "))
            if 1 <= num <= len(tasks):
                task_text = tasks[num - 1]
                if task_text.startswith("[Done] "):
                    print("🙌 Task is already completed.")
                else:
                    if task_text.startswith("[Pending] "):
                        tasks[num - 1] = task_text.replace("[Pending]", "[Done]")
                    else:
                        tasks[num - 1] = "[Done] " + task_text

                    with open('tasks.txt', 'w') as file:
                        for t in tasks:
                            file.write(t + '\n')
                    print(f"🎉 Task '{tasks[num - 1][len('[Done] '):]}' marked as completed.")
            else:
                print("Invalid number.")

    elif choice == 5:
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
