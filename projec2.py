def view_tasks():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
        for task in tasks:
            print(task.strip())

def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + " " )

def delete_task(task_number):
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    with open("tasks.txt", "w") as file:
        for i, task in enumerate(tasks):
            if i != task_number - 1:
                file.write(task)

print("1. View tasks")
print("2. Add task")
print("3. Delete task")

choice = input("Enter choice (1/2/3): ")

if choice == '1':
    view_tasks()
elif choice == '2':
    task = input("Enter task: ")
    add_task(task)
elif choice == '3':
    view_tasks()
    task_number = int(input("Enter task number to delete: "))
    delete_task(task_number)
else:
    print("Invalid choice")