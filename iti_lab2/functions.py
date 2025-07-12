Tasks = dict()
def Add_Task():
    isexist = False
    while True:
        task = input("Enter the task you want to add : ")
        if task in Tasks.keys():
            print("This task is already exists!")
            print("Please try again ^^")
            isexist = True

        if not isexist:
            Tasks[task] = 'Not Completed'
            print("Add Task Is Done Successfully ^^")
            break

def Mark_Completed():
    isexist = True
    while True:
        view_tasks()
        task = input("Enter the task you want to mark : ")
        if task  not in Tasks.keys():
            print("This task is not exists!")
            isexist = False

        if isexist:
            if Tasks[task] == 'Completed':
                print("This task is already marked as completed!!!")
            else:
                Tasks[task] = 'Completed'
                print("The task is marked successfully ^^")
                view_tasks()
        else:
            ans = input("Do you want add it (y/n)?")
            if ans == 'y':
                Add_Task()
            else:
                print("Okay , try it later ^^")
        return

def view_tasks():
    if(len(Tasks) == 0):
        print("Yout To Do List Is Empty!!!")
        return
    c = 1
    for t in Tasks.keys():
        print(f"{c}. {t}" , end = " ")
        if Tasks[t] == "Completed":
            print('✅')
        else:
            print('❎')
        c += 1

def exit():
    print("Thank you for use our application ^^")




