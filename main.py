#Declare the list as an empty list.
#It will store all tasks as entered by the user
tasks = [] 

#Define a function add_task
def add_task():
#Declate a variable title
#Whatever the user types is stored inside the variable title
    title = input("Enter the title of the Task:")

#Create a dictonary named task
#task stores information in key-value pairs
    task = {
        "task number": len(tasks) + 1 ,#len(tasks) counts how many tasks are already in the list
        "title" : title ,#adds the title entered by the user
        "status" : "To Do"#Every task automaticaly starts with "To Do"status
    }
    tasks.append(task)
    print("Task has been added!")


while True:
    # Application menu

    print("\n============= CHOOSE OPTION =============\n")
    print("1) add a Task")
    print("2) Display a list of all tasks")
    print("3) Display a single task")
    print("4) Update the status of a task (To Do, In Progress, Done)")
    print("5) Delete a task")
    print("6) Exit Program")

    choice = input("\nChoose an option: ").strip()
    
    if choice == "1":
        add_task()
    elif choice == "2":
       print("# Call a function for displaying all tasks e.g display_all_takss()")
       # display_all_takss()
    elif choice == "3":
       print("# Call a function to display a single task")
       # display_single_task()
    elif choice == "4":
        print("# Call a function for Updating tasks")
        # Update_task()
    elif choice == "5":
        print("# Call a function for deleting tasks")
        # delete_task()
    elif choice == "6":
        print("\nExiting the program")
        print("Goodbye!")
        break
    else:
        # validated for a wrong input
        print("Invalid choice. Try again.\n")



