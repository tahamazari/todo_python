from functions import *

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