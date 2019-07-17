def list_tasks(list):
    if(len(list) == 0):
        print("You dont have any tasks in your list")    
    else:
        print(list)

def add_task(list):
    print(list)
    dict = {}

    print("Please type the title of your task")
    key = input()
    print("Please type down your task")
    value = input()
    dict[key] = value

    print("Do you want to choose a particular index to add to list?")
    print("Type 'y' for yes or any other key to append at last of list")
    select = input()
    if(select == 'y'):
        print("Type index")
        index = int(input())
        if(index >= len(list)):
            print("Index can't be greater than or equal to length of List\nCould not add task")
        else:
            list.insert(index, dict)
            print("New task with title " + key + " added")

    else:
        list.append(dict)
        print("New task with title " + key + " added")

def update_task(list):
    print(list)
    print("Please type in index of task you want to update")
    index = int(input())
    
    print("Please type in new title of your task")
    key = input()

    print("Type to update current task")
    value = input()
    dict = {}
    dict[key] = value
    list[index] = dict
    

def delete_task(list):
    if(len(list) == 0):
        print("Your TODO List is empty! Can't delete anything")
    else: 
        print(list)
        print("Type index of task you want to delete")
        index = int(input())
        if(index >= len(list)):
            print("Index can't be greater than or equal to length of List")
        else:
            list.pop(index)