def personal_account():
    welcomeMsg = "Welcome\nEnter a username and password to register and continue"
    print(welcomeMsg)
    userName = input("Enter a user name: ")
    return userName

def accPass():
    print("Password must be at least 8 characters")
    global createPass
    createPass = input("Password: ")
    while len(createPass) < 8:
        print("Password must be at least 8 characters. Try again!")
        createPass = input("Password: ")
    print("Please confirm password")
    confirmPass = input("Password: ")
    while confirmPass != createPass:
        print("Password does not match!")
        confirmPass = input("Password: ")

    print("whoo-hoo! Password successful created!")
    print("Your username is " + str(userName))
    print("Your password is " + createPass)
def calculator():
    print("Welcome to Calculator")
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    while num1 not in map(str, range(10)) or num2 not in map(str, range(10)):
        print("Invalid entry. Must be 0-9")
        num1 = (input("Enter first number: "))
        num2 = (input("Enter second number: "))


        sign = input("Enter add, subtract, multiply or divide: ")
        if sign == "add":
            print(num1 + num2)
        elif sign == "subtract":
            print (num1 - num2)
        elif sign == "multiply":
            print (num1 * num2)
        elif sign == "divide":
            print(num1 / num2)
        else:
            print("Invalid input")

def toDoList():
    welcomeMsg = "Welcome, you have chosen ToDoList\n"
    welcomeMsg += "See menu\n1. Add Task\n2. View Task\n3. Remove Task\n4. Exit"
    print(welcomeMsg)
    tasks = []
    t = True
    while True:
        if t:
            menu = input("What would you like to do? (add, view, remove, exit): ")
            t = False
        else:
            menu = input("What would you like to do again? (add, view, remove, exit): ")
        if menu == "1" or menu == "add":
            task = (input("Add task here: "))
            tasks.append(task)
            print("You have added " + task)
        elif menu == "2" or menu == "view":
            if not tasks:
                print("Task is empty")
            else:
                print("These are your tasks")
                for task in tasks:
                    print(f"\t{task}")
        elif menu == "3" or menu == "remove":
            if not tasks:
                print("Task is empty")
            else:
                taskRemove = (input("What would you like to remove: "))

                while taskRemove not in tasks:
                    print("Task not found, try again " + "(enter end or back to go back to menu)")
                    taskRemove = (input("What would you like to remove: "))

                    if taskRemove == "back" or taskRemove == "end":
                        break
                        menu = input("What would you like to do? (add, view, remove, exit): ")

                else:
                    tasks.remove(taskRemove)
                    print("You have successfully removed " + taskRemove)
        elif menu == "4" or menu == "exit":
            print("You have exited the app\nSee you next time!")
            break
        else:
            print("Invalid input")
            print(tasks)


userName = personal_account()
createPass = accPass()


print("What would you like to do today?")
print("1. ToDoList\n2. Calculator")
choice = input("Enter 1 to use ToDoList or 2 to use Calculator: ")
if choice == "1":
    toDoList()
else:
    calculator()