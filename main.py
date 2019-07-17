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
    print("New task with title" + key + "added")
    return dict

def update_task(dict):
    print("Please type in title of task you want to update")
    key = input()
    if key in dict:
        print("Type in to update current task")
        value = input()
        dict.update({key: value})
        print("Task with title " + key + " updated")
        return dict
    else: 
        print("Title not found")
    

def delete_task(dict):
    print("Type in title of task you want to delete")
    key = input()
    if(len(dict) == 0):
        print("Your TODO List is empty! Can't delete anything")
    elif key in dict:
        del dict[key]
        print("Task with title " + key + " deleted")
        return dict
    else: 
        print("Task with title " + key + " not found")

tasks_dict = {}

def main():
    while True:
        print("Choose from the following actions from below:")
        print("Press 1 to view your TODO List")
        print("Press 2 to add new task to your TODO List")
        print("Press 3 to update previous task")
        print("Press 4 to delete a task ")
        print("Press 5 to exit")

        action = int(input())

        if(action == 1):
            list_tasks(tasks_dict)

        elif(action == 2):
            add_task(tasks_dict)

        elif(action == 3):
            update_task(tasks_dict)

        elif(action == 4):
            delete_task(tasks_dict)

        elif(action == 5):
            exit()


main()