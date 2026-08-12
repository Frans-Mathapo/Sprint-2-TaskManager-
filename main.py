import pandas as pd
#Declare the list as an empty list.
#It will store all tasks as entered by the user
tasks = [] 

CSV_FILE = "datasets/tasks.csv" # initialize dataset path for csv file

#Define a function add_task
def add_task():
#Declate a variable title
#Whatever the user types is stored inside the variable title
    title = input("Enter the title of the Task:")

#Create a dictonary named task
#task stores information in key-value pairs
    task = {
        "task_number": len(tasks) + 1 ,#len(tasks) counts how many tasks are already in the list
        "title" : title ,#adds the title entered by the user
        "status" : "To Do"#Every task automaticaly starts with "To Do"status
    }
    tasks.append(task)
    print("Task has been added!")

def display_all():
    if not tasks:
        print("There are no tasks available")
        return

    print("All Tasks")

    df= pd.DataFrame(tasks)
    print(df)
    
    # Save data into a csv file
    df.to_csv(CSV_FILE, index=False)
    
""""
    for task in tasks:
        print(f"task number: {task['task_number']}")
        print(f"title:{task['title']}")
        print(f"Status: task['status']")
        print("-" * 20)
"""

def display_single_task():
    # First check if the list is empty
    if len(tasks) == 0:
        print("There are no tasks available to display.")
        return
        
    # Ask the user for the task number and convert it to an integer
    search_id = int(input("Enter the task number you want to view: "))
    
    # Create a variable to keep track of whether we found the task
    found = False
    
    # Search through the list
    for task in tasks:
        if task['task_number'] == search_id:
            print("\n--- Task Details ---")
            print(f"Task Number: {task['task_number']}")
            print(f"Title:       {task['title']}")
            print(f"Status:      {task['status']}")
            print("--------------------")
            found = True
            break # Exit the loop since we found what we were looking for
            
    # If the loop finishes and we didn't find it, tell the user
    if found == False:
        print("Task not found.")


# function for Updating tasks start here
def update_status():

    # Display all tasks
    display_all()

    if not tasks:
        return

    # Ask the user which task they want to update
    select_task = int(
        input("\nSelect the task number to change the status: ").strip()
    )

    # Convert user's number to Python list index
    select_task -= 1

    # Check that the selected task exists
    if select_task < 0 or select_task >= len(tasks):
        print("Invalid task number.")
        return

    # Get the selected task
    selected_task = tasks[select_task]

    # Display selected task
    print("\nSelected Task:")
    print(f"Task Number: {selected_task['task_number']}")
    print(f"Title: {selected_task['title']}")
    print(f"Current Status: {selected_task['status']}")

    # Status options
    statuses = ["To Do", "In Progress", "Done"]

    print("\nChoose a new status:")

    for i, status in enumerate(statuses, start=1):
        print(f"{i}) {status}")

    # Ask for new status
    status_choice = int(
        input("\nSelect status: ").strip()
    )

    # Validate status choice
    if status_choice < 1 or status_choice > len(statuses):
        print("Invalid status.")
        return

    # Update status
    selected_task["status"] = statuses[status_choice - 1]

    # Save updated tasks to CSV
    df = pd.DataFrame(tasks)
    df.to_csv(CSV_FILE, index=False)

    print("\nTask status updated successfully!")
# Update function end here

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
        display_all()
    elif choice == "3":
       # Call a function to display a single task
       display_single_task()
    elif choice == "4":
        # Call a function for Updating tasks"
        update_status()
    elif choice == "5":
        # Call a function for deleting tasks
        delete_task()
    elif choice == "6":
        print("\nExiting the program")
        print("Goodbye!")
        break
    else:
        # validated for a wrong input
        print("Invalid choice. Try again.\n")