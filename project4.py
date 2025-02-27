def view_tasks():
    with open("tasks.txt" , "r") as file:
      tasks = file.readlines()
    for task in tasks:
        print(tasks.strip())
        
def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + " ")
        
def delete_task(task_number):
    with open("tasks.txt", "r") as file:
        taks = file.readlines()
    with open("tasks.txt", "w") as file:
        for i, task in enumerate(task):
            if i != task_number - 1:
                file.write(task)
                print("1. view task")
                print("2. add task")
                print("3. view task")
    choice = input("Enter choice (1/2/3): ")
    if choice == '1':
        view_tasks() 
    elif choice == '2':
        task = input("enter tasks: ")
        add_task()
    elif choice == '2':
        task_number = int(input("enter the task number to delete: "))
        
        delete_task(task_number)
        
    else:
        print("Invalid choice")    
