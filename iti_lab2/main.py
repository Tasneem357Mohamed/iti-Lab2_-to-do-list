import functions

while True:
    print("To-Do List Application")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. View Tasks")
    print("4. Exit")
    x = int(input("Please select an option (1 - 4):"))
    if x == 1:
        functions.Add_Task()
    elif x == 2:
        functions.Mark_Completed()
    elif x == 3:
        functions.view_tasks()
    else:
        functions.exit()
        break

    ans = input("Do you want to do another operation?(y/n): ")
    if ans == 'n':
        functions.exit()
        break