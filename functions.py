def list_tasks(all_tasks):
    if(len(all_tasks) == 0):
        print("You dont have any tasks in your list")
        return    
    show_tasks(all_tasks)

def add_task(all_tasks):
    show_tasks(all_tasks)
    task = {}

    print("Please type the title of your task")
    key = input()
    print("Please type down your task")
    value = input()
    task['TITLE: ' + key] = 'TASK: ' + value

    print("Do you want to choose a particular index to add to list?")
    print("Type 'y' for yes or any other key to append at last of list")
    select = input()
    if(select == 'y'):
        print("Type index")
        index = int(input())
        if(index >= len(all_tasks)):
            print("Index can't be greater than or equal to length of List\nCould not add task")
            return
        else:
            all_tasks.insert(index, task)
            print("New task with title " + key + " added")
            return

    else:
        all_tasks.append(task)
        print("New task with title " + key + " added")
        return

def update_task(all_tasks):
    show_tasks(all_tasks)
    print("Please type in index of task you want to update")
    index = int(input())
    
    print("Please type in new title of your task")
    key = input()

    print("Type to update current task")
    value = input()
    task = {}
    task['TITLE: ' + key] = 'TASK: ' + value
    all_tasks[index] = task
    

def delete_task(all_tasks):
    if(len(all_tasks) == 0):
        print("Your TODO List is empty! Can't delete anything")
    else: 
        pshow_tasks(all_tasks)
        print("Type index of task you want to delete")
        index = int(input())
        if(index >= len(all_tasks)):
            print("Index can't be greater than or equal to length of List")
            return
        else:
            all_tasks.pop(index)
            return

def show_tasks(tasks):
    for i in range(0, len(tasks)):
        print(str(i) + '. ' + str(tasks[i]))