# To-do list manager

print()

tasks = []

i = 1

print(f"{"="*18} TO-DO LIST MANAGER {"="*18}")

while i == 1:
    # Main menu
    print('\n1. Add    2. View    3. Mark Done    4. Quit')
    command = int(input("\nChoose one: "))

    if command == 1 :
        # Add task
        add = input('Add task: ')
        tasks.append(add)
        print('Task added: ' + add)

    elif command == 2 :
        # View task
        print('=== Your Tasks ===')
        if len(tasks) == 0:
            print('No task added.')
        else: 
            for task in tasks :
                print(f"{tasks.index(task) + 1}. {task}")
            print(f"Total number of tasks: {len(tasks)}")
        
    elif command == 3 :
        # Completed tasks should be removed
        if len(tasks) == 0:
            print('No task added.\nAdd some tasks first to be mark done.')
        else: 
            for task in tasks :
                print(f"{tasks.index(task) + 1}. {task}")
            done = int(input("Which number of task has been done: "))
            print(f"{done}. {tasks.pop(done - 1)}")

    elif command == 4 :
        # quit the app
        if len(tasks) == 0:
            print('No task added.')
        else: 
            print('Pending tasks: ')
            for task in tasks :
                print(f"{tasks.index(task) + 1}. {task}")
            print(f"Total number of tasks: {len(tasks)}")

        print('\nGoodbye.')
        break

    else:
        # defense programming
        print("Invalid choice.")

print(f"{"="*25} END {"="*25}")

print()

