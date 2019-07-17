def list_tasks(dict):
    if(len(dict) == 0):
        print("You dont have any tasks in your list")
    
    else:
        print(dict)

def add_task(dict):
    print("Please type the title of your task")
    key = input()
    print("Please type down your task")
    value = input()
    dict.update({key: value})
    print(dict)
    return dict

def update_task(dict):
    print("Please type in title of task you want to update")
    key = input()
    if key in dict:
        print("Type in to update current task")
        value = input()
        dict.update({key: value})
        print(dict)
        return dict
    else: 
        print("titele not found")

def delete_task(dict):
    print("Type in title of task you want to delete")
    key = input()
    if key in dict:
        del dict[key]
        print(dict)
        return dict
    else: 
        print("Task with title " + key + " not found")

tasks_dict = {}
tasks_dict.update({'taha': 'mazari'})
tasks_dict.update({'job': 'engineer'})

def main():
    print("Welcome to TODO List App!")
    print("Choose from the following options from below:")
    print("Press 1 to view your TODO List")
    print("Press 2 to add new task to your TODO List")
    print("Press 3 to update previous task")
    print("Press 4 to delete a task ")
    print("Press any other key to exit")

    action = int(input())

    if(action == 1):
        list_tasks(tasks_dict)

    elif(action == 2):
        add_task(tasks_dict)

    elif(action == 3):
        update_task(tasks_dict)

    elif(action == 4):
        delete_task(tasks_dict)

    else:
        exit()


main()