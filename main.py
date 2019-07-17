from functions import *

list = []

def main():
    while True:
        print("Choose from the following actions from below:")
        print("Press 1 to view your TODO List")
        print("Press 2 to add new task to your TODO List")
        print("Press 3 to update previous task")
        print("Press 4 to delete a task ")
        print("Press any other number to exit")

        action = int(input())

        if(action == 1):
            list_tasks(list)

        elif(action == 2):
            add_task(list)

        elif(action == 3):
            update_task(list)

        elif(action == 4):
            delete_task(list)

        else:
            exit()


main()